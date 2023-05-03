from ipaddress import ip_address
from random import randint
from subprocess import Popen, PIPE


def host_ping(hosts: list):
    for ip in hosts:
        cmd = ['ping', f'{ip}', '-w', '5']
        process = Popen(cmd, stdout=PIPE)
        process.wait()
        if process.returncode == 0:
            print(f'{ip} - Узел доступен')
        else:
            print(f'{ip} - Узел недоступен')


if __name__ == '__main__':
    hosts = [ip_address(randint(0, 2**32)) for i in range(10)]  # IPv4
    host_ping(hosts)
