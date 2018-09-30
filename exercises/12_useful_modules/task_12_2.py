# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''

from sys import argv
from subprocess import run, PIPE

data = argv[1:]


def parse_arguments(data):
    try:
        net, host = data[0].split('-')
        first = net[-1]
        net = net[:-1]
        ip_list = [net+str(x) for x in range(int(first), int(host)+1)]
        return ip_list
    except ValueError:
        return data


def check_ip_addresses(ip_list):
    ok = []
    nok = []
    for ip in ip_list:
        res = run(f'ping {ip} -c 3', shell=True, stdout=PIPE, encoding='utf-8')
        for line in res.stdout.split('\n'):
            if line.startswith('3 packets'):
                loss = line.split()[-3]
                ok.append(ip) if loss == '0.0%' else nok.append(ip)
    return ok, nok


if __name__ == '__main__':
    print(check_ip_addresses(parse_arguments(data)))
