from utils import Pack

_global_sep_no = 1


class RequestInstance(object):
    def __init__(self, command_id, message_body):
        self.command_id = command_id
        self._message_body = message_body

        global _global_sep_no
        _global_sep_no += 1
        self.sequence_no = _global_sep_no

    @property
    def message(self):
        return Pack.get_unsigned_long_data(
            len(self._message_body)) + Pack.get_unsigned_long_data(
            self.command_id) + Pack.get_unsigned_long_data(
            self.sequence_no) + self._message_body
