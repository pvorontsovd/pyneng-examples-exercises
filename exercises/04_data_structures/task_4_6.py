# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

protocol    = ospf_route.split()[0].replace('O', 'OSPF')
prefix      = ospf_route.split()[1]
metric      = ospf_route.split()[2].strip('[]')
nexthop     = ospf_route.split()[4].rstrip(',')
lastupdate  = ospf_route.split()[5].rstrip(',')
interface   = ospf_route.split()[6]

print(f'''
Protocol:              {protocol}
Prefix:                {prefix}
AD/Metric:             {metric}
Next-Hop:              {nexthop}
Last update:           {lastupdate}
Outbound Interface:    {interface}
''')
