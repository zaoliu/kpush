# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))

from netkit.contrib.tcp_client import TcpClient
from netkit.box import Box
from web.application import create_app
from share import proto
from share.utils import pack_data


worker_client = TcpClient(Box, '115.28.224.64', 29000)


def test_register():
    req = dict(
        device_id=2,
        appkey="7d357c9b4ce1414fb27f077b54fb5a8f",
        channel="MAIN",
    )
    worker_client.write(dict(
        cmd=proto.CMD_REGISTER,
        body=pack_data(req)
    ))

    box = worker_client.read()
    if box:
        print box
    else:
        return

    worker_client.write(dict(
        cmd=proto.CMD_SET_ALIAS_AND_TAGS,
        body=pack_data(dict(
            alias='dante',
        ))
    ))

    box = worker_client.read()
    if box:
        print box
    else:
        return


def main():
    worker_client.connect()
    test_register()

if __name__ == '__main__':
    app = create_app()
    with app.test_request_context():
        main()
