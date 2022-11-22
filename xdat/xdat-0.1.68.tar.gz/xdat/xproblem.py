import numpy as np
import pandas as pd
from collections import namedtuple
from sklearn import model_selection, pipeline, metrics
from sklearn.base import clone
from tqdm import tqdm
from joblib import Parallel, delayed
from . import xutils


Metric = namedtuple('Metric', ['name', 'func', 'args'])
METRICS = {
    'AUC': Metric(name='AUC', func=metrics.roc_auc_score, args=['target', 'prob_1']),
    'R2': Metric(name='R2', func=metrics.r2_score, args=['pred', 'target']),
    'MAPE': Metric(name='MAPE', func=metrics.mean_absolute_percentage_error, args=['pred', 'target']),
    'MAE': Metric(name='MAE', func=metrics.mean_absolute_error, args=['pred', 'target']),
    'MSE': Metric(name='MSE', func=metrics.mean_squared_error, args=['pred', 'target']),
    'MSLE': Metric(name='MSLE', func=metrics.mean_squared_log_error, args=['pred', 'target']),
}

for k,v in list(METRICS.items()):
    METRICS[k.lower()] = v


CVSplit = namedtuple("CVSplit", ['df_train', 'df_test', 'df_val'])


def cv_split(df, n_splits=12, stratify_on=None, group_on=None, val_size=0.0):
    df = df.sample(frac=1.).reset_index(drop=True)
    groups = df[group_on] if group_on else None
    y = df[stratify_on] if stratify_on else None

    if group_on is None:
        if n_splits == 'max':
            n_splits = len(df)

        if stratify_on:
            kfold = model_selection.StratifiedKFold(n_splits=n_splits)

        else:
            kfold = model_selection.KFold(n_splits=n_splits)

    else:
        num_groups = len(np.unique(groups))
        if n_splits == 'max':
            n_splits = num_groups

        n_splits = min(n_splits, num_groups)

        if stratify_on:
            kfold = model_selection.StratifiedGroupKFold(n_splits=n_splits)

        else:
            kfold = model_selection.GroupKFold(n_splits=n_splits)

    for train_index, test_index in kfold.split(df, y=y, groups=groups):
        df_train = df.iloc[train_index].reset_index(drop=True)
        df_test = df.iloc[test_index].reset_index(drop=True)
        df_val = None

        if val_size:
            assert not group_on, "Not yet implemented"

            stratify = df_train[stratify_on] if stratify_on else None
            df_train, df_val = model_selection.train_test_split(df_train, test_size=val_size, stratify=stratify)

        yield CVSplit(df_train=df_train, df_test=df_test, df_val=df_val)


CVFold = namedtuple("CVFold", ['clf', 'df_train', 'df_test', 'feature_names', 'df_val'])


def train_cv(df, target_col, clf, n_splits=12, stratify_on=None, group_on=None, ordered_split=False, del_cols=tuple(), uid_col=None, sample_weight_col=None, eval_size=0.0, eval_type=None, fit_params=None, n_jobs=1):
    if eval_size:
        assert eval_type in ['lightgbm'], "need to specify proper eval_type param"
    else:
        eval_type = None

    fit_params = dict() if fit_params is None else fit_params

    del_cols = set(del_cols)
    if uid_col:
        del_cols.add(uid_col)
    if sample_weight_col:
        del_cols.add(sample_weight_col)
    del_cols = sorted(del_cols)

    def calc_fold(fold_num, split_data: CVSplit):
        clf_fold = clone(clf)
        df_train = split_data.df_train
        df_train_data = df_train.copy()
        df_val = split_data.df_val
        df_val_data = None
        if df_val is not None:
            df_val_data = df_val.copy()

        df_test = split_data.df_test
        df_test_data = df_test.copy()
        test_tmp_uid = df_test[uid_col] if uid_col else None
        sample_weight_train = df_train[sample_weight_col] if sample_weight_col else None
        sample_weight_eval = df_val[sample_weight_col] if sample_weight_col else None

        if ordered_split and group_on:
            assert n_splits == 'max'
            test_group = df_test[group_on].min()
            df_train = df_train[df_train[group_on] < test_group].reset_index(drop=True)
            assert (df_train[group_on] >= test_group).sum() == 0
            if len(df_train) == 0:
                return

        if del_cols:
            df_train_data = df_train.drop(columns=del_cols, errors='ignore')
            df_test_data = df_test.drop(columns=del_cols, errors='ignore')
            if df_val_data is not None:
                df_val_data = df_val_data.drop(columns=del_cols, errors='ignore')

        X_train, y_train = xutils.split_X_y(df_train_data, target_col)
        X_eval, Y_eval = None, None
        if df_val_data is not None:
            X_eval, Y_eval = xutils.split_X_y(df_val_data, target_col)

        if sample_weight_train is not None:
            if eval_type == 'lightgbm':
                eval_set = [[X_eval, Y_eval]]
                clf_fold.fit(X_train, y_train, sample_weight=sample_weight_train, eval_set=eval_set, eval_sample_weight=sample_weight_eval, **fit_params)
            else:
                clf_fold.fit(X_train, y_train, sample_weight=sample_weight_train, **fit_params)

        else:
            if eval_type == 'lightgbm':
                eval_set = [[X_eval, Y_eval]]
                clf_fold.fit(X_train, y_train, eval_set=eval_set, **fit_params)
            else:
                clf_fold.fit(X_train, y_train, **fit_params)

        pred_train = clf_fold.predict(X_train)
        df_train['pred'] = pred_train
        if hasattr(clf_fold, "predict_proba"):
            prob_1 = clf_fold.predict_proba(X_train)[:, 1]
            df_train['prob_1'] = prob_1

        if eval_type:
            pred_eval = clf_fold.predict(X_eval)
            df_val['pred'] = pred_eval
            if hasattr(clf_fold, "predict_proba"):
                prob_1 = clf_fold.predict_proba(X_eval)[:, 1]
                df_val['prob_1'] = prob_1

        X_test, y_test = xutils.split_X_y(df_test_data, target_col)
        pred = clf_fold.predict(X_test)
        df_test['pred'] = pred

        if hasattr(clf_fold, "predict_proba"):
            prob_1 = clf_fold.predict_proba(X_test)[:, 1]
            df_test['prob_1'] = prob_1

        df_test['fold_num'] = fold_num
        if uid_col:
            df_test[uid_col] = test_tmp_uid

        fold = CVFold(clf=clf_fold, df_train=df_train, df_test=df_test, feature_names=X_train.columns, df_val=df_val)

        return fold

    splits = cv_split(df, n_splits=n_splits, stratify_on=stratify_on, group_on=group_on, val_size=eval_size)
    total = len(df) if n_splits == 'max' else n_splits
    tqdm_splits = tqdm(enumerate(splits), total=total)

    if n_jobs == 1:
        all_folds = [calc_fold(fold_num, split_data) for fold_num, split_data in tqdm_splits]

    else:
        all_folds = Parallel(n_jobs=n_jobs)(delayed(calc_fold)(fold_num, split_data) for fold_num, split_data in tqdm_splits)

    all_folds = [fold for fold in all_folds if fold is not None]

    df_test = pd.concat([i[2] for i in all_folds], ignore_index=True)
    df_test = df_test.reset_index(drop=True)
    return df_test, all_folds


def eval_test(df_test, eval_per=None, metric_list=None):
    """

    :type metrics: list[Metric|str]
    """

    df_test = df_test.copy()
    df_test['none'] = 'none'

    metric_list = [m if isinstance(m, Metric) else METRICS[m] for m in metric_list]

    if not isinstance(eval_per, list) and not isinstance(eval_per, tuple):
        eval_per = [eval_per]

    rows = []
    for curr_group in eval_per:
        if not curr_group:
            curr_group = 'none'

        for gval in df_test[curr_group].unique():
            df_g = df_test[df_test[curr_group] == gval]
            row = {m.name: m.func(*(df_g[arg] for arg in m.args)) for m in metric_list}
            row['cv_grouping'] = curr_group
            row['cv_group_key'] = str(gval)
            row['cv_group_size'] = len(df_g)
            rows.append(row)

    df_res = pd.DataFrame(rows)
    return df_res


def calc_feature_importances(folds, flat=False):
    rows = []
    fi_var = None
    for fold in folds:
        clf = fold.clf
        if isinstance(clf, pipeline.Pipeline):
            clf = clf[-1]

        if fi_var is None:
            for var in ['feature_importances_', 'coef_']:
                if hasattr(clf, var):
                    fi_var = var
                    break

            if not fi_var:
                print("Can't find in clf")
                return

        fi = getattr(clf, fi_var).flatten()
        fi_dict = dict(zip(fold.feature_names, fi))
        if flat:
            for k, v in fi_dict.items():
                rows.append({'feature_name': k, 'feature_importance': v})

        else:
            rows.append(fi_dict)

    df = pd.DataFrame(rows)
    return df


class ModelEnsemble:
    def __init__(self, clfs):
        self.clfs = clfs

    @classmethod
    def from_all_folds(cls, all_folds):
        clfs = [f.clf for f in all_folds]
        return cls(clfs)

    def predict(self, X):
        all_y = [clf.predict(X) for clf in self.clfs]
        all_y = [y.reshape(y.shape + (1,)) for y in all_y]
        Y = np.concatenate(all_y, axis=1)
        pred = [np.bincount(y).argmax() for y in Y]
        pred = np.array(pred)
        return pred

    def predict_binary(self, X, threshold=0.5):
        prob_1 = self.predict_proba(X)[:, 1]
        pred = prob_1 >= threshold
        return pred.astype(int)

    def predict_proba(self, X):
        all_y = [clf.predict_proba(X) for clf in self.clfs]
        all_y = [y.reshape(y.shape + (1,)) for y in all_y]
        y = np.concatenate(all_y, axis=2)
        proba = y.mean(axis=2)
        return proba

