# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

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

if validIP:
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
else:
    print('Incorrect IPv4 address')
