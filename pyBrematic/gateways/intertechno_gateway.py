# -*- coding: utf-8 -*-
import socket

from pyBrematic.gateways.gateway import Gateway


class IntertechnoGateway(Gateway):
    """Gateway class for the Intertechno Gateway ITGW-433"""

    def __init__(self, ip, port=49880):
        super().__init__(ip, port)

    def send_request(self, device, action):
        """Sends the UDP request to the gateway"""
        data = device.get_signal(self, action)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(data.encode(), (self._ip, self._port))
        s.close()
