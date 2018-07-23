# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

vlan = input('введите номер VLAN: ')

with open('CAM_table.txt', 'r') as f:
    table = f.readlines()[6:]
    table.sort()
    for line in table:
        if line.startswith(f' {vlan}'):
            print(line.strip())
