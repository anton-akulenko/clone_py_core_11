'''
Метод: sub
'''

import re

string = "The best language is Java"

print(re.sub(r'Java', 'Python', string))

'''

Дано рядок символів.
Виключити з цього рядка групи символів між дужками [, ].
Самі дужки теж мають бути виключені.

'''

import re

string = "Виключити із цієї [рядки групи] символів, [розташовані між] дужками [, ]."

# Квантифікатор ? повторення змінює поведінку пошуку на не жадібне
print(re.findall(r'\[.*?\]', string))

sanitize_string = re.sub(r'\[.*?\]', '', string)
print(sanitize_string)

sanitize_string = re.sub(r'\[|\]', '', string)
print(sanitize_string)

sanitize_string = re.sub(r'\[.*?\]', '[]', string)
print(sanitize_string)