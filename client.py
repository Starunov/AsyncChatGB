import random
import sys
from socket import *
import time
import json
import argparse
import ipaddress
import threading

from global_vars import *
from logs.client_log_config import client_logger, log


COMMANDS = (
    '/members',
    '/connect',
    '/exit',
    '/help'
)

HELP_TEXT = """
/members - get active clients
/connect <client> - connect to client
/exit - disconnect from client
/help - show this message
"""


def listen(s: socket, host: str, port: int):
    while True:
        msg, addr = s.recvfrom(BUFFERSIZE)
        msg_port = addr[-1]
        msg = msg.decode(ENCODING)
        allowed_ports = threading.current_thread().allowed_ports

        if msg_port not in allowed_ports:
            continue

        if not msg:
            continue

        if '__' in msg:
            command, content = msg.split('__')
            if command == 'members':
                for n, member in enumerate(content.split('; '), start=1):
                    print('\r\r' + f'{n}) {member}' + '\n' + 'you: ', end='')
        else:
            peer_name = f'client{msg_port}'
            print('\r\r' + f'{peer_name}: ' + msg + '\n' + 'you: ', end='')


def start_listen(target, socket, host, port):
    th = threading.Thread(target=target, args=(socket, host, port), daemon=True)
    th.start()
    return th


@log
def start(address, port):
    own_port = random.randint(8000, 9000)

    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((address, own_port))

    listen_thread = start_listen(listen, s, address, port)
    allowed_ports = [port]
    listen_thread.allowed_ports = allowed_ports
    sendto = (address, port)

    s.sendto('__join'.encode(ENCODING), sendto)

    while True:
        msg = input('you: ')
        command = msg.split()[0]

        if command in COMMANDS:
            if msg == '/members':
                s.sendto('__members'.encode(ENCODING), sendto)

            if msg == '/exit':
                # Удаляем из разрешенных порт клиента и продолжаем работу с сервером
                peer_port = sendto[-1]
                allowed_ports.remove(peer_port)
                sendto = (address, port)
                print(f'Disconnect from client{peer_port}')

            if msg.startswith('/connect'):
                # Добавляем порт клиента в список разрешенных, сообщения будем отправлять ему
                peer = msg.split()[-1]
                peer_port = int(peer.replace('client', ''))
                allowed_ports.append(peer_port)
                sendto = (address, peer_port)
                print(f'Connect to client{peer_port}')

            if msg == '/help':
                print(HELP_TEXT)
        else:
            s.sendto(msg.encode(ENCODING), sendto)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('address', type=str, help='IP-адрес сервера')
    parser.add_argument('-p', dest='port', type=int, default=7777, help='TCP-порт на сервере (по умолчанию 7777)')
    args = parser.parse_args()

    try:
        ipaddress.ip_address(args.address)
    except ValueError:
        parser.error('Введен не корректный ip адрес')

    start(args.address, args.port)
