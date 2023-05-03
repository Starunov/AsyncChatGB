from tabulate import tabulate
from ipaddress import ip_address
from random import randint
from subprocess import Popen, PIPE
from itertools import zip_longest


def host_range_ping_tab(ip: ip_address, range_: int = 1):
    head = ['Reachable', 'Unreachable']
    reachable = []
    unreachable = []
    body = []
    int_ip = int(ip)
    for _ in range(range_):
        _ip = ip_address(int_ip)
        cmd = ['ping', f'{_ip}', '-w', '1']
        process = Popen(cmd, stdout=PIPE)
        process.wait()
        if process.returncode == 0:
            reachable.append(_ip)
        else:
            unreachable.append(_ip)

        int_ip += 1
        if not int_ip % 256:
            break

    for item in zip_longest(reachable, unreachable):
        body.append(item)

    print(tabulate(body, headers=head, tablefmt='grid'))


if __name__ == '__main__':
    ip = ip_address(randint(0, 2**32))  # IPv4
    host_range_ping_tab(ip, range_=5)
