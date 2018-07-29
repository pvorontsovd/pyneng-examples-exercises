# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию, которая обрабатывает конфигурационный файл коммутатора
и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки можно оставлять).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def config_to_dict(config_file):
    config = []
    with open(config_file, 'r') as f:
        for line in f:
            if line.startswith('!') or ignore_command(line, ignore):
                continue
            config.append(line.rstrip())

    dict_config = {key: [] for key in config if not key.startswith(' ')}

    for key in dict_config:
        index = config.index(key)
        while True:
            try:
                elem = config[index + 1]
                if elem.startswith(' '):
                    dict_config[key].append(elem)
                    index += 1
                else:
                    break
            except IndexError:
                break

    return dict_config


print(config_to_dict('config_sw1.txt'))
