# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/config/admin/admin.proto
# plugin: python-betterproto
import warnings
from dataclasses import dataclass
from typing import AsyncIterator, List

import betterproto
import grpclib


@dataclass(eq=False, repr=False)
class ReadOnlySubPath(betterproto.Message):
    """
    ReadOnlySubPath is an extension to the ReadOnlyPath to define the datatype
    of the subpath
    """

    # sub_path is the relative path of a child object e.g. /list2b/index
    sub_path: str = betterproto.string_field(1)
    # value_type is the datatype of the read only path
    value_type: "_v2__.ValueType" = betterproto.enum_field(2)
    type_opts: List[int] = betterproto.uint64_field(3)
    description: str = betterproto.string_field(4)
    units: str = betterproto.string_field(5)
    is_a_key: bool = betterproto.bool_field(6)
    attr_name: str = betterproto.string_field(7)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ReadOnlyPath(betterproto.Message):
    """
    ReadOnlyPath extracted from the model plugin as the definition of a tree of
    read only items. In YANG models items are defined as ReadOnly with the
    `config false` keyword. This can be applied to single items (leafs) or
    collections (containers or lists). When this `config false` is applied to
    an object every item beneath it will also become readonly - here these are
    shown as subpaths. The complete read only path then will be a concatenation
    of both e.g. /cont1a/cont1b-state/list2b/index and the type is defined in
    the SubPath as UInt8.
    """

    # path of the topmost `config false` object e.g. /cont1a/cont1b-state
    path: str = betterproto.string_field(1)
    # ReadOnlySubPath is a set of children of the path including an entry for the
    # type of the topmost object with subpath `/` An example is /list2b/index
    sub_path: List["ReadOnlySubPath"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ReadWritePath(betterproto.Message):
    """
    ReadWritePath is extracted from the model plugin as the definition of a
    writeable attributes. In YANG models items are writable by default unless
    they are specified as `config false` or have an item with `config false` as
    a parent. Each configurable item has metadata with meanings taken from the
    YANG specification RFC 6020.
    """

    # path is the full path to the attribute (leaf or leaf-list)
    path: str = betterproto.string_field(1)
    # value_type is the data type of the attribute
    value_type: "_v2__.ValueType" = betterproto.enum_field(2)
    # units is the unit of measurement e.g. dB, mV
    units: str = betterproto.string_field(3)
    # description is an explaination of the meaning of the attribute
    description: str = betterproto.string_field(4)
    # mandatory shows whether the attribute is optional (false) or required
    # (true)
    mandatory: bool = betterproto.bool_field(5)
    # default is a default value used with optional attributes. Replaced by
    # 'defaults' below
    default: str = betterproto.string_field(6)
    # range is definition of the range of values a value is allowed
    range: List[str] = betterproto.string_field(7)
    # length is a defintion of the length restrictions for the attribute
    length: List[str] = betterproto.string_field(8)
    type_opts: List[int] = betterproto.uint64_field(9)
    is_a_key: bool = betterproto.bool_field(10)
    attr_name: str = betterproto.string_field(11)
    # defaults is a default value(s) used with optional attributes. For leaf-list
    # can have repeated values replaces the 'default' attribute above
    defaults: List[str] = betterproto.string_field(12)

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.default:
            warnings.warn("ReadWritePath.default is deprecated", DeprecationWarning)


@dataclass(eq=False, repr=False)
class Namespace(betterproto.Message):
    """
    Namespace is a mapping between a module name and its shorthand prefix
    """

    module: str = betterproto.string_field(1)
    prefix: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ModelInfo(betterproto.Message):
    """ModelInfo is general information about a model plugin."""

    # name is the name given to the model plugin - no spaces and title case.
    name: str = betterproto.string_field(1)
    # version is the semantic version of the Plugin e.g. 1.0.0.
    version: str = betterproto.string_field(2)
    # model_data is a set of metadata about the YANG files that went in to
    # generating the model plugin. It includes name, version and organization for
    # each YANG file, similar to how they are represented in gNMI Capabilities.
    model_data: List["___gnmi__.ModelData"] = betterproto.message_field(3)
    # module is no longer used
    module: str = betterproto.string_field(4)
    # getStateMode is flag that defines how the "get state" operation works.  0)
    # means that no retrieval of state is attempted  1) means that the
    # synchronizer will make 2 requests to the device - one for      Get with
    # State and another for Get with Operational.  2) means that the synchronizer
    # will do a Get request comprising of each      one of the ReadOnlyPaths and
    # their sub paths. If there is a `list`      in any one of these paths it
    # will be sent down as is, expecting the      devices implementation of gNMI
    # will be able to expand wildcards.  3) means that the synchronizer will do a
    # Get request comprising of each      one of the ReadOnlyPaths and their sub
    # paths. If there is a `list`      in any one of these paths, a separate call
    # will be made first to find      all the instances in the list and a Get
    # including these expanded wildcards      will be sent down to the device.
    get_state_mode: int = betterproto.uint32_field(5)
    # read_only_path is all of the read only paths for the model plugin.
    read_only_path: List["ReadOnlyPath"] = betterproto.message_field(7)
    # read_write_path is all of the read write paths for the model plugin.
    read_write_path: List["ReadWritePath"] = betterproto.message_field(8)
    supported_encodings: List["___gnmi__.Encoding"] = betterproto.enum_field(9)
    # namespace_mappings is a set of all prefix to module name mapping in the
    # model
    namespace_mappings: List["Namespace"] = betterproto.message_field(10)
    # southboundUsePrefix indicates that the southbound should add prefixes in
    # gNMI paths
    southbound_use_prefix: bool = betterproto.bool_field(11)

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.module:
            warnings.warn("ModelInfo.module is deprecated", DeprecationWarning)


@dataclass(eq=False, repr=False)
class ModelPlugin(betterproto.Message):
    id: str = betterproto.string_field(1)
    endpoint: str = betterproto.string_field(2)
    info: "ModelInfo" = betterproto.message_field(3)
    status: str = betterproto.string_field(10)
    error: str = betterproto.string_field(11)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListModelsRequest(betterproto.Message):
    """
    ListModelsRequest carries data for querying registered model plugins.
    """

    # verbose option causes all of the ReadWrite and ReadOnly paths to be
    # included.
    verbose: bool = betterproto.bool_field(1)
    # An optional filter on the name of the model plugins to list.
    model_name: str = betterproto.string_field(2)
    # An optional filter on the version of the model plugins to list
    model_version: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RollbackRequest(betterproto.Message):
    """
    RollbackRequest carries the index of the configuration change transaction
    to rollback.
    """

    # index of the transaction that should be rolled back
    index: int = betterproto.uint64_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RollbackResponse(betterproto.Message):
    """RollbackResponse carries the response of the rollback operation"""

    # ID of the rollback transaction
    id: str = betterproto.string_field(1)
    # index of the rollback transaction
    index: int = betterproto.uint64_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ModelInfoRequest(betterproto.Message):
    """ModelInfoRequest carries request for the model information"""

    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ModelInfoResponse(betterproto.Message):
    """ModelInfoResponse carries response for the model information query"""

    model_info: "ModelInfo" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ValidateConfigRequest(betterproto.Message):
    """
    ValidateConfigRequest carries configuration data to be validated as a JSON
    blob
    """

    json: bytes = betterproto.bytes_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ValidateConfigResponse(betterproto.Message):
    """ValidateConfigResponse carries the result of the validation"""

    valid: bool = betterproto.bool_field(1)
    message: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class PathValuesRequest(betterproto.Message):
    """PathValuesRequest carries configuration change as a JSON blob"""

    path_prefix: str = betterproto.string_field(1)
    json: bytes = betterproto.bytes_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class PathValuesResponse(betterproto.Message):
    """PathValuesResponse carries a list of typed path values"""

    path_values: List["_v2__.PathValue"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ValueSelectionRequest(betterproto.Message):
    """
    ValueSelectionRequest carries the necessary parts to form a selection
    context
    """

    # selectionPath is a configuration path to a leaf in the format:
    # /a/b[key1=index][key2=index2]/c/d where d is a leaf node
    selection_path: str = betterproto.string_field(1)
    # configJson is a JSON tree view of the complete Configuration for a Target
    config_json: bytes = betterproto.bytes_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ValueSelectionResponse(betterproto.Message):
    """
    ValueSelectionResponse returns the result of applying the selection rules
    to the selection context
    """

    # selection is an array of string values
    selection: List[str] = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetTransactionRequest(betterproto.Message):
    # ID of transaction to get
    id: str = betterproto.string_field(1)
    # index of transaction to get; leave 0 for lookup by ID; if specified takes
    # precedence
    index: int = betterproto.uint64_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetTransactionResponse(betterproto.Message):
    transaction: "_v2__.Transaction" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListTransactionsRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListTransactionsResponse(betterproto.Message):
    transaction: "_v2__.Transaction" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchTransactionsRequest(betterproto.Message):
    id: str = betterproto.string_field(1)
    noreplay: bool = betterproto.bool_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchTransactionsResponse(betterproto.Message):
    event: "_v2__.TransactionEvent" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetConfigurationRequest(betterproto.Message):
    configuration_id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetConfigurationResponse(betterproto.Message):
    configuration: "_v2__.Configuration" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListConfigurationsRequest(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListConfigurationsResponse(betterproto.Message):
    configuration: "_v2__.Configuration" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchConfigurationsRequest(betterproto.Message):
    configuration_id: str = betterproto.string_field(1)
    noreplay: bool = betterproto.bool_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchConfigurationsResponse(betterproto.Message):
    event: "_v2__.ConfigurationEvent" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


class ConfigAdminServiceStub(betterproto.ServiceStub):
    """
    ConfigAdminService provides means for enhanced interactions with the
    configuration subsystem.
    """

    async def list_registered_models(
        self, *, verbose: bool = False, model_name: str = "", model_version: str = ""
    ) -> AsyncIterator["ModelPlugin"]:
        """ListRegisteredModels returns a stream of registered models."""

        request = ListModelsRequest()
        request.verbose = verbose
        request.model_name = model_name
        request.model_version = model_version

        async for response in self._unary_stream(
            "/onos.config.admin.ConfigAdminService/ListRegisteredModels",
            request,
            ModelPlugin,
        ):
            yield response

    async def rollback_transaction(self, *, index: int = 0) -> "RollbackResponse":
        """
        RollbackTransaction rolls back the specified configuration change
        transaction.
        """

        request = RollbackRequest()
        request.index = index

        return await self._unary_unary(
            "/onos.config.admin.ConfigAdminService/RollbackTransaction",
            request,
            RollbackResponse,
        )


class ModelPluginServiceStub(betterproto.ServiceStub):
    """ModelPluginService is to be implemented by model plugin sidecar"""

    async def get_model_info(self) -> "ModelInfoResponse":
        """GetModelInfo provides information about the model"""

        request = ModelInfoRequest()

        return await self._unary_unary(
            "/onos.config.admin.ModelPluginService/GetModelInfo",
            request,
            ModelInfoResponse,
        )

    async def validate_config(self, *, json: bytes = b"") -> "ValidateConfigResponse":
        """
        ValidateConfig validates the provided configuration data against the
        model
        """

        request = ValidateConfigRequest()
        request.json = json

        return await self._unary_unary(
            "/onos.config.admin.ModelPluginService/ValidateConfig",
            request,
            ValidateConfigResponse,
        )

    async def get_path_values(
        self, *, path_prefix: str = "", json: bytes = b""
    ) -> "PathValuesResponse":
        """
        GetPathValues produces list of typed path value entries from the
        specified configuration change JSON tree
        """

        request = PathValuesRequest()
        request.path_prefix = path_prefix
        request.json = json

        return await self._unary_unary(
            "/onos.config.admin.ModelPluginService/GetPathValues",
            request,
            PathValuesResponse,
        )

    async def get_value_selection(
        self, *, selection_path: str = "", config_json: bytes = b""
    ) -> "ValueSelectionResponse":
        """
        GetValueSelection gets a list of valid options for a leaf by applying
        selection rules in YANG. The selection rules should be defined as an
        XPath expression, as an argument to a `leaf-selection` extension in the
        YANG model (Used to support the ROC GUI)
        """

        request = ValueSelectionRequest()
        request.selection_path = selection_path
        request.config_json = config_json

        return await self._unary_unary(
            "/onos.config.admin.ModelPluginService/GetValueSelection",
            request,
            ValueSelectionResponse,
        )


class TransactionServiceStub(betterproto.ServiceStub):
    """
    TransactionService provides means to inspect the contents of the internal
    transactions store.
    """

    async def get_transaction(
        self, *, id: str = "", index: int = 0
    ) -> "GetTransactionResponse":
        """Get transaction by its ID or index"""

        request = GetTransactionRequest()
        request.id = id
        request.index = index

        return await self._unary_unary(
            "/onos.config.admin.TransactionService/GetTransaction",
            request,
            GetTransactionResponse,
        )

    async def list_transactions(self) -> AsyncIterator["ListTransactionsResponse"]:
        """List returns all configuration transactions"""

        request = ListTransactionsRequest()

        async for response in self._unary_stream(
            "/onos.config.admin.TransactionService/ListTransactions",
            request,
            ListTransactionsResponse,
        ):
            yield response

    async def watch_transactions(
        self, *, id: str = "", noreplay: bool = False
    ) -> AsyncIterator["WatchTransactionsResponse"]:
        """
        Watch returns a stream of configuration transaction change
        notifications
        """

        request = WatchTransactionsRequest()
        request.id = id
        request.noreplay = noreplay

        async for response in self._unary_stream(
            "/onos.config.admin.TransactionService/WatchTransactions",
            request,
            WatchTransactionsResponse,
        ):
            yield response


class ConfigurationServiceStub(betterproto.ServiceStub):
    """
    ConfigurationService provides means to inspect the contents of the internal
    configurations store.
    """

    async def get_configuration(
        self, *, configuration_id: str = ""
    ) -> "GetConfigurationResponse":
        """Get configuration by its target ID"""

        request = GetConfigurationRequest()
        request.configuration_id = configuration_id

        return await self._unary_unary(
            "/onos.config.admin.ConfigurationService/GetConfiguration",
            request,
            GetConfigurationResponse,
        )

    async def list_configurations(self) -> AsyncIterator["ListConfigurationsResponse"]:
        """List returns all target configurations"""

        request = ListConfigurationsRequest()

        async for response in self._unary_stream(
            "/onos.config.admin.ConfigurationService/ListConfigurations",
            request,
            ListConfigurationsResponse,
        ):
            yield response

    async def watch_configurations(
        self, *, configuration_id: str = "", noreplay: bool = False
    ) -> AsyncIterator["WatchConfigurationsResponse"]:
        """Watch returns a stream of configuration change notifications"""

        request = WatchConfigurationsRequest()
        request.configuration_id = configuration_id
        request.noreplay = noreplay

        async for response in self._unary_stream(
            "/onos.config.admin.ConfigurationService/WatchConfigurations",
            request,
            WatchConfigurationsResponse,
        ):
            yield response


from .. import v2 as _v2__
from .... import gnmi as ___gnmi__
