# -*- encoding: utf-8 -*-

import os.path
import copy
import logging
from typing import List
from datetime import datetime

from datahub.emitter.mce_builder import make_tag_urn, make_user_urn
from datahub.metadata.schema_classes import (
    MLModelPropertiesClass, MLMetricClass, VersionTagClass, MLHyperParamClass, 
)

from metadata.ensure import ensure_timestamp
from metadata.entity.model import Model

logger = logging.getLogger(__name__)


class ModelMixin:

    def create_model(self,  model: Model, upsert=True):
        properties = copy.deepcopy(model.properties)
        properties['display_name'] = model.display_name
        properties['uri'] = model.uri
        model_properties = MLModelPropertiesClass(
            customProperties=properties,
            description=model.description,
            type=model.algorithm,
            version=VersionTagClass(model.version) if model.version else None,
            date=ensure_timestamp(model.created_at) if model.created_at else int(datetime.now().timestamp() * 1000),
            groups=model.groups,
            trainingMetrics=[
                MLMetricClass(name=key, vlaue=str(value) if value else None) for key, value in (model.training_metrics or {}).items()
            ],
            hyperParams=[
                MLHyperParamClass(name=key, vlaue=str(value) if value else None) for key, value in (model.training_params or {}).items()
            ],
            mlFeatures=model.training_features,
            deployments=model.deployments,
            trainingJobs=model.training_jobs,
            downstreamJobs=model.downstream_jobs,
        )
        global_tags = self._get_tags_aspect(model.tags)
        owner_aspect = self._get_ownership_aspect(model.owners or [self.context.user_email])
        context = self.context
        browse_paths = self._get_browse_paths_aspect(model.browse_paths or [f'Projects/{context.project}/Models'])
        self._emit_aspects(Model.entity_type, model.urn, [model_properties, global_tags, owner_aspect, browse_paths])
        return model.urn

    def update_model(self, model: Model):
        return self.create_model(model, upsert=True)

    def get_model(self, urn: str):
        if not self.check_entity_exists(urn):
            return
        r = self._query_graphql(Model.entity_type, urn=urn)['data']['mlModel']
        properties = r['properties']
        custom_properties = {e['key']: e['value'] for e in properties.get('customProperties', {})}
        display_name = custom_properties.pop('display_name', r['name'])
        uri = custom_properties.pop('uri', None)
        tags = [t['tag']['urn'].split(':', maxsplit=3)[-1] for t in r.get('tags', {}).get('tags', [])]
        model = Model(
            urn=urn,
            display_name=display_name,
            uri=uri,
            tags=tags,
            description=properties.get('description', r.get('description', '')),
            browse_paths=list(filter(None, [os.path.join(*path['path']) if path['path'] else None for path in r.get('browsePaths', [])])),
            properties=custom_properties,
            algorithm=properties.get('type'),
            created_at=properties.get('date'),
            version=properties.get('version'),
            owners=[o['owner']['urn'].split(':', maxsplit=3)[-1] for o in r.get('ownership', {}).get('owners')],
            groups=[group['urn'] for group in properties.get('groups', [])],
            training_metrics={item['name']: item['value'] for item in properties.get('trainingMetrics', [])},
            training_params={item['name']: item['value'] for item in properties.get('hyperParams', [])},
            training_features=properties.get('mlFeatures', []),
        )
        return model

    def delete_model(self, urn: str):
        return self._delete_entity(urn)

    def get_models_by_facts(self, *, owner: str=None, group: str=None, tags: List[str]=None, search: str=""):
        facts = []
        # TODO group
        if tags:
            facts.append(('tags', [make_tag_urn(tag) for tag in tags], False, 'CONTAIN'))
        if owner:
            facts.append(('owners', [make_user_urn(self.context.user_email if owner == 'me' else owner)], False, 'CONTAIN'))
        return self._get_entities_by_facts(Model.entity_type, facts, search=search) 