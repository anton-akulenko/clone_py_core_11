'''
Читаємо файл за допомогою бібліотеки pathlib
'''

from pathlib import Path

folder = Path('./Temp')
filename = folder / 'temp.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

except OSError as err:
    print(f'Помилка доступу до файлу: {err}')
finally:
    print('')
    print('File operation completed')