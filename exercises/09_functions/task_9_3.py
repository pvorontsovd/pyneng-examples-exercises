# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(configFile):
    with open(configFile, 'r') as f:
        config = f.read().split('\n!')

    access, trunk = {}, {}

    for line in config:
        if line.strip().startswith('interface F'):
            interface = line.strip().split('\n ')
            mode = None
            for command in interface:
                if command.startswith('interface'):
                    iface = command.split()[-1]
                if command.startswith('switchport mode'):
                    mode = command.split()[-1]
                if (command.startswith('switchport access') or
                      command.startswith('switchport trunk')):
                    vlan = command.split()[-1]
            if mode == 'access':
                access[iface] = int(vlan)
            if mode == 'trunk':
                vlans = vlan.split(',')
                trunk[iface] = [ int(vlan) for vlan in vlans ]
    return access, trunk


a = get_int_vlan_map('config_sw1.txt')
print(a)
