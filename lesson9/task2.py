from ipaddress import ip_address
from random import randint
from subprocess import Popen, PIPE


def host_range_ping(ip: ip_address, range_: int = 1):
    int_ip = int(ip)
    for _ in range(range_):
        _ip = ip_address(int_ip)
        cmd = ['ping', f'{_ip}', '-w', '5']
        process = Popen(cmd, stdout=PIPE)
        process.wait()
        if process.returncode == 0:
            print(f'{_ip} - Узел доступен')
        else:
            print(f'{_ip} - Узел недоступен')

        int_ip += 1
        if not int_ip % 256:
            break


if __name__ == '__main__':
    ip = ip_address(randint(0, 2**32))  # IPv4
    host_range_ping(ip, range_=6)
