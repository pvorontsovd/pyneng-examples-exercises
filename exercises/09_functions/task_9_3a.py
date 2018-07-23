# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(configFile):
    with open(configFile, 'r') as f:
        config = f.read().split('\n!')

    access, trunk = {}, {}

    for line in config:
        if line.strip().startswith('interface F'):
            interface = line.strip().split('\n ')
            mode, vlan = None, 1
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


a = get_int_vlan_map('config_sw2.txt')
print(a)
