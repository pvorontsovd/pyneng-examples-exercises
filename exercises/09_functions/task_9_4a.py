# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)


def get_subcommands(commands, key, level):
    '''
    Функция возвращает список всех "сабкоманд" от конкретной команды
    commands - список команд
    key - команда, от которой нужно найти сабкоманды
    level - уровень вложенности (один пробел или два пробела)
    '''
    subcommands = []
    index = commands.index(key)
    while True:
        try:
            elem = commands[index + 1]
            if elem.startswith(level):
                subcommands.append(elem)
                index += 1
            else:
                return subcommands
        except IndexError:
            return subcommands


def config_to_dict(config_file):
    commands = []
    with open(config_file, 'r') as f:
        for line in f:
            if line.startswith('!') or check_ignore(line, ignore):
                continue
            commands.append(line.rstrip())

    dict_config = {key: None for key in commands if not key.startswith(' ')}

    for key in dict_config:
        subcommands = get_subcommands(commands, key, ' ')
        if not subcommands:
            dict_config[key] = []
        elif subcommands[-1].startswith('  '):
            sub_dict = {key: [] for key in subcommands if not key.startswith('  ')}
            for sub_key in sub_dict:
                sub_subcom = get_subcommands(subcommands, sub_key, '  ')
                sub_dict[sub_key] = sub_subcom
            dict_config[key] = sub_dict
        else: # if subcommands[-1].startswith(' '):
            dict_config[key] = []
            for command in subcommands:
                dict_config[key].append(command)

    return dict_config


print(config_to_dict('config_r1.txt'))
