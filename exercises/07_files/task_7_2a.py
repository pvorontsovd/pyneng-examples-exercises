# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

configFile = argv[1]

with open(configFile, 'r') as f:
    for command in f:
        if command.startswith('!') or command.startswith(f' {ignore[0]}') or \
           command.startswith(ignore[1]) or command.startswith(ignore[2]):
            continue
        else:
            print(command.rstrip())
