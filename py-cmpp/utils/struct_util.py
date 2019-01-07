import struct


class Unpack(object):
    @staticmethod
    def get_unsigned_long_data(source_data):
        return struct.unpack("!L", source_data)

    @staticmethod
    def get_unsigned_char_data(source_data):
        return struct.unpack("!B", source_data)

    @staticmethod
    def get_unsigned_long_long_data(source_data):
        return struct.unpack("!Q", source_data)


class Pack(object):
    @staticmethod
    def get_unsigned_long_data(source_data):
        return struct.pack("!L", source_data)

    @staticmethod
    def get_unsigned_char_data(source_data):
        return struct.pack("!B", source_data)
