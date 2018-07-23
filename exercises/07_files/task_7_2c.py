# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

configFile, configFileCleared = argv[1:]

with open(configFile, 'r') as f:
    with open(configFileCleared, 'w') as output:
        for command in f:
            if command.startswith(f' {ignore[0]}') or \
               command.startswith(ignore[1]) or command.startswith(ignore[2]):
                continue
            else:
                output.write(command)
