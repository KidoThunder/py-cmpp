from cmpp_defines import CMPP_CONNECT_RESP, CMPP_TERMINATE_RESP, \
    CMPP_SUBMIT_RESP

from response_instances import *

_RESPONSE_MAPPING = {
    CMPP_CONNECT_RESP: ConnectResponseInstance,
    CMPP_TERMINATE_RESP: TerminateResponseInstance,
    CMPP_SUBMIT_RESP: SubmitResponseInstance
}


def parse_to_response_instance(message):
    command_id, = Unpack.get_unsigned_long_data(message[4:8])
    return _RESPONSE_MAPPING[command_id](message)
