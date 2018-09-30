# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv
from subprocess import run, PIPE

ip_list = argv[1:]


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


print(check_ip_addresses(ip_list))
