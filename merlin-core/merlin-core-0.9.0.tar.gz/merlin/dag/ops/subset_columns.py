#
# Copyright (c) 2022, NVIDIA CORPORATION.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from merlin.core.protocols import Transformable
from merlin.dag.base_operator import BaseOperator
from merlin.dag.selector import ColumnSelector


class SubsetColumns(BaseOperator):
    """
    This operator class provides an implementation for the `[]` operator
    used in constructing graphs.
    """

    def __init__(self, label=None):
        self._label = label or self.__class__.__name__
        super().__init__()

    def transform(
        self, col_selector: ColumnSelector, transformable: Transformable
    ) -> Transformable:
        """Simply returns the selected output columns from the input dataframe

        The main functionality of this operator has to do with computing the schemas
        for `-` nodes in the Workflow graph, so very little has to happen in the
        `transform` method.

        Parameters
        -----------
        columns: list of str or list of list of str
            The columns to apply this operator to
        transformable: Transformable
            A pandas or cudf dataframe that this operator will work on

        Returns
        -------
        DataFrame
            Returns a transformed dataframe for this operator
        """
        return super()._get_columns(transformable, col_selector)

    @property
    def label(self) -> str:
        return self._label
