from response_instances.response_instance import ResponseInstance
from utils import Unpack


class ConnectResponseInstance(ResponseInstance):
    def __init__(self, message):
        super(ConnectResponseInstance, self).__init__(message)
        message_body = message[12:]
        self.raw_status = message_body[0:4]
        self.status, = Unpack.get_unsigned_long_data(self.raw_status)
        self.authenticator_ISMG = message_body[4:20]
        self.version, = Unpack.get_unsigned_char_data(message_body[20:21])


class TerminateResponseInstance(ResponseInstance):
    def __init__(self, message):
        super(TerminateResponseInstance, self).__init__(message)


class SubmitResponseInstance(ResponseInstance):
    def __init__(self, message):
        super(SubmitResponseInstance, self).__init__(message)
        message_body = message[12:]
        self.msg_id, = Unpack.get_unsigned_long_long_data(message_body[0:8])
        self.result, = Unpack.get_unsigned_long_data(message_body[8:12])
