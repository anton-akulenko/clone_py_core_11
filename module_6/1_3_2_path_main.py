'''
Основні можливості pathlib
'''

from pathlib import Path

current_path = Path('.')
# print(current_path)
# print(current_path.cwd())

# Шлях
file = current_path / 'bin' / 'utils' / 'paint.drawio.svg'
print(file)
# print(current_path.joinpath('bin', 'utils', 'paint.drawio.svg'))

# Частини файлу
print(file.parts)

# ім'я файлу
print(file.name)
print(file.name.split('.')[0])

# Батьківська папка
print(file.parent)

# Суфікс
print(file.suffix)
print(file.suffixes)