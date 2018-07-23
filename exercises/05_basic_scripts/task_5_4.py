# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]

num = int(input('число из списка num_list: '))

num_list.reverse()
index = (num_list.index(num))
num_list.pop(num_list.index(num))
num_list.insert(index, 'boo')
num_list.reverse()
print(num_list.index('boo'))

word = (input('слово из word_list: '))

word_list.reverse()
index = (word_list.index(word))
word_list.pop(word_list.index(word))
word_list.insert(index, 'boo')
word_list.reverse()
print(word_list.index('boo'))
