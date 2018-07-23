# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open('ospf.txt', 'r') as f:
    for ospfRoute in f:
        protocol    = ospfRoute.split()[0].replace('O', 'OSPF')
        prefix      = ospfRoute.split()[1]
        metric      = ospfRoute.split()[2].strip('[]')
        nexthop     = ospfRoute.split()[4].rstrip(',')
        lastupdate  = ospfRoute.split()[5].rstrip(',')
        interface   = ospfRoute.split()[6]

        print(f'''
        Protocol:              {protocol}
        Prefix:                {prefix}
        AD/Metric:             {metric}
        Next-Hop:              {nexthop}
        Last update:           {lastupdate}
        Outbound Interface:    {interface}
        ''')
