# Задача №27. 
# Пользователь вводит текст(строка). Словом считается последовательность непробельных 
# символов идущих подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

import ast
import imp
import sys
import os.path
import types
import string

# liter_list = 'sea shells on the sea shore Im sure that the shells are sea shore shells'
# liter_list = liter_list.lower()
# print(liter_list)
# words = liter_list.split()
# liter_set = set(words)
# print(liter_set)
# print(f'Количество различных слов: {len(liter_set)}')

my_text = '''She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea shore shells'''
print(my_text)
punct = list(string.punctuation) + ['n', '\t']
for char in punct:
    my_text = my_text.replace(char, ' ')
my_text = my_text.lower().split()
dict_count = {}
for key in my_text:
    dict_count[key] = dict_count.get(key, 0) + 1
print(*dict_count.items(), sep='\n')
print(len(set(dict_count)))
