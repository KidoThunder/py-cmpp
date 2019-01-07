from utils import Unpack


class ResponseInstance(object):
    def __init__(self, message):
        self.length, = Unpack.get_unsigned_long_data(message[0:4])
        self.command_id, = Unpack.get_unsigned_long_data(message[4:8])
        self.sequence, = Unpack.get_unsigned_long_data(message[8:12])
        self.message_body = message[12:self.length]
