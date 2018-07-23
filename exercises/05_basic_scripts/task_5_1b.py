# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

inputData = argv[1]

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
