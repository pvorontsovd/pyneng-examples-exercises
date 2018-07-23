# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

inputData = input('введите IP-сеть в формате network/mask: ')

network = list(int(i) for i in (inputData.split('/')[0]).split('.'))
mask = int(inputData.split('/')[1])

bitMask = ('1' * mask + '0' * (32 - mask))

print(f'''\
network:
{network[0]:<8}  {network[1]:<8}  {network[2]:<8}  {network[3]:<8}
{network[0]:08b}  {network[1]:08b}  {network[2]:08b}  {network[3]:08b}

mask:
/{mask}
{int(bitMask[0:8], 2):<8}  {int(bitMask[8:16], 2):<8}  \
{int(bitMask[16:24], 2):<8}  {int(bitMask[24:32], 2):<8}
{bitMask[0:8]}  {bitMask[8:16]}  {bitMask[16:24]}  {bitMask[24:32]}\
''')
