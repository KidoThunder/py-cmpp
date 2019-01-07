import logging
import socket

from request_instances import ConnectRequestInstance, TerminateRequestInstance
from response_instances import parse_to_response_instance
from utils import Unpack


class Cmpp(object):
    def __init__(self, host: str, port: int, sp_id: str, sp_secret: str):
        """
        :param host: Gateway IP
        :param port: Gateway port
        :param sp_id: Service provider id
        :param sp_secret: Service provider secret
        """
        self._host = host
        self._port = port
        self._sp_id = sp_id
        self._sp_secret = sp_secret
        self._so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_request(self, request_obj):
        if not self._commence():
            self._close()
        self._send(request_obj.message)
        resp_msg = self._receive()
        resp = parse_to_response_instance(resp_msg)
        self._terminate()
        return resp

    def _commence(self):
        self._connect()
        conn_req = ConnectRequestInstance(self._sp_id, self._sp_secret)
        self._send(conn_req.message)
        resp_msg = self._receive()
        if not resp_msg:
            logging.info("Connect response message empty.")
            return
        conn_res = parse_to_response_instance(resp_msg)
        if conn_res.status == 0:
            return True
        logging.info(
            "Connect response status({}) wrong.".format(str(conn_res.status)))

    def _terminate(self):
        self._send(TerminateRequestInstance().message)

    def _connect(self):
        self._so.connect((self._host, self._port))

    def _send(self, message):
        self._so.send(message)

    def _receive(self):
        receive_data = self._so.recv(4)
        if receive_data:
            msg_length, = Unpack.get_unsigned_long_data(receive_data)
            response_data = receive_data + self._so.recv(msg_length)
            return response_data
        return None

    def _close(self):
        self._so.close()

