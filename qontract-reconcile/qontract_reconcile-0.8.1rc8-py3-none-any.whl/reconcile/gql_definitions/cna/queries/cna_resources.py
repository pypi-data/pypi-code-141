"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Callable,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)


DEFINITION = """
query CNAssets {
  namespaces: namespaces_v1 {
    name
    externalResources {
      provider
      provisioner {
        name
      }
      ... on NamespaceCNAsset_v1 {
        resources {
          provider
          ... on CNANullAsset_v1 {
            name: identifier
            addr_block
          }
        }
      }
    }
  }
}
"""


class ExternalResourcesProvisionerV1(BaseModel):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceExternalResourceV1(BaseModel):
    provider: str = Field(..., alias="provider")
    provisioner: ExternalResourcesProvisionerV1 = Field(..., alias="provisioner")

    class Config:
        smart_union = True
        extra = Extra.forbid


class CNAssetV1(BaseModel):
    provider: str = Field(..., alias="provider")

    class Config:
        smart_union = True
        extra = Extra.forbid


class CNANullAssetV1(CNAssetV1):
    name: str = Field(..., alias="name")
    addr_block: Optional[str] = Field(..., alias="addr_block")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceCNAssetV1(NamespaceExternalResourceV1):
    resources: list[Union[CNANullAssetV1, CNAssetV1]] = Field(..., alias="resources")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceV1(BaseModel):
    name: str = Field(..., alias="name")
    external_resources: Optional[
        list[Union[NamespaceCNAssetV1, NamespaceExternalResourceV1]]
    ] = Field(..., alias="externalResources")

    class Config:
        smart_union = True
        extra = Extra.forbid


class CNAssetsQueryData(BaseModel):
    namespaces: Optional[list[NamespaceV1]] = Field(..., alias="namespaces")

    class Config:
        smart_union = True
        extra = Extra.forbid


def query(query_func: Callable, **kwargs: Any) -> CNAssetsQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        CNAssetsQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return CNAssetsQueryData(**raw_data)
