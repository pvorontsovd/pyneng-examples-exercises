# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

validIP = False
while not validIP:
    try:
        ipAdress = input('введите ip адрес: ')

        ipAdressList = ipAdress.split('.')

        if len(ipAdressList) == 4:
            validIP = True
            try:
                for octet in ipAdressList:
                    if not 0 <= int(octet) <= 255:
                        validIP = False
                        break
            except ValueError:
                validIP = False
        else:
            validIP = False
    except KeyboardInterrupt:
        print('\nbye!')
        break
else:
    firstOctet = int(ipAdressList[0])
    if 1 <= firstOctet <= 223:
        print('unicast')
    elif 224 <= firstOctet <= 239:
        print('multicast')
    elif ipAdress == '255.255.255.255':
        print('local broadcast')
    elif ipAdress == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
