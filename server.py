import select
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
import time
import json
import argparse
import ipaddress

from global_vars import *
from logs.server_log_config import server_logger, stream_logger, log


@log
def start(address: str, port: int):
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((address, port))

    members = []

    while True:

        msg, addr = s.recvfrom(BUFFERSIZE)
        if addr not in members:
            members.append(addr)

        if not msg:
            continue

        client_id = addr[1]
        msg_text = msg.decode(ENCODING)

        if msg_text == '__join':
            stream_logger.info(f'Client {client_id} joined chat')
            continue

        if msg_text == '__members':
            stream_logger.info(f'Client {client_id} requested members')
            active_clients = [f'client{m[1]}' for m in members if m != addr]
            s.sendto(f'active members: {"; ".join(active_clients)}'.encode(ENCODING), addr)
            continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='port', type=int, default=7777,
                        help='TCP-порт для работы (по умолчанию использует 7777)')
    parser.add_argument('-a', dest='address',
                        help='IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)')
    args = parser.parse_args()

    address = args.address or ''
    if address:
        try:
            ipaddress.ip_address(address)
        except ValueError:
            parser.error(f'Введен не корректный ip адрес "{address}"')

    start(address, args.port)
