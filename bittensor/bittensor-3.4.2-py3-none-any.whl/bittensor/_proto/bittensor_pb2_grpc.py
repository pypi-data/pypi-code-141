# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bittensor._proto import bittensor_pb2 as bittensor_dot___proto_dot_bittensor__pb2


class BittensorStub(object):
    """Service definition for tensor processing servers.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Forward = channel.unary_unary(
                '/Bittensor/Forward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.FromString,
                )
        self.Backward = channel.unary_unary(
                '/Bittensor/Backward',
                request_serializer=bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.SerializeToString,
                response_deserializer=bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.FromString,
                )


class BittensorServicer(object):
    """Service definition for tensor processing servers.
    """

    def Forward(self, request, context):
        """Forward tensor request. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Backward(self, request, context):
        """Backward tensor request i.e. gradient.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BittensorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.SerializeToString,
            ),
            'Backward': grpc.unary_unary_rpc_method_handler(
                    servicer.Backward,
                    request_deserializer=bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.FromString,
                    response_serializer=bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Bittensor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bittensor(object):
    """Service definition for tensor processing servers.
    """

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bittensor/Forward',
            bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Backward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bittensor/Backward',
            bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.SerializeToString,
            bittensor_dot___proto_dot_bittensor__pb2.TensorMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
