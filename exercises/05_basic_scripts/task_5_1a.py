# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

inputData = input('введите IP-сеть в формате network/mask: ')

host = list(int(i) for i in (inputData.split('/')[0]).split('.'))
mask = int(inputData.split('/')[1])

bitMask = ('1' * mask + '0' * (32 - mask))
bitNet = (f'{host[0]:08b}{host[1]:08b}{host[2]:08b}{host[3]:08b}'[0:mask] + '0' * (32 - mask))

print(f'''\
host:
{host[0]:<8}  {host[1]:<8}  {host[2]:<8}  {host[3]:<8}
{host[0]:08b}  {host[1]:08b}  {host[2]:08b}  {host[3]:08b}

network:
{int(bitNet[0:8], 2):<8}  {int(bitNet[8:16], 2):<8}  \
{int(bitNet[16:24], 2):<8}  {int(bitNet[24:32], 2):<8}
{bitNet[0:8]}  {bitNet[8:16]}  {bitNet[16:24]}  {bitNet[24:32]}

mask:
/{mask}
{int(bitMask[0:8], 2):<8}  {int(bitMask[8:16], 2):<8}  \
{int(bitMask[16:24], 2):<8}  {int(bitMask[24:32], 2):<8}
{bitMask[0:8]}  {bitMask[8:16]}  {bitMask[16:24]}  {bitMask[24:32]}\
''')
