# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''

from task_12_2 import check_ip_addresses, parse_arguments
from sys import argv
from tabulate import tabulate

data = argv[1:]


def ip_table(reacheble, unreacheble):
    print(tabulate({'Reachable': reacheble, 'Unreachable': unreacheble},
                    headers='keys'))


reacheble, unreacheble = check_ip_addresses(parse_arguments(data))
ip_table(reacheble, unreacheble)
