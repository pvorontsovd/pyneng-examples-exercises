# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

configFile = argv[1]

with open(configFile, 'r') as f:
    with open('config_sw1_cleared.txt', 'w') as output:
        for command in f:
            if command.startswith(f' {ignore[0]}') or \
               command.startswith(ignore[1]) or command.startswith(ignore[2]):
                continue
            else:
                output.write(command)
