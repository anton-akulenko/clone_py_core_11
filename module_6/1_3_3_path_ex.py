'''
Більше можливостей pathlib
'''
from pathlib import Path

current_dir = Path('.')

# Перевірка властивостей файлів
# for el in current_dir.iterdir():
#     print(f'{el.name}. Dir: {el.is_dir()}. File: {el.is_file()}. Exist: {el.exists()}')

# Перевірка неіснуючого файлу
file = current_dir / 'bin' / 'utils' / 'paint.drawio.svg'
# print(file.exists())

#  Пошук за шаблоном
for el in current_dir.glob('**/*.jpg'):
    print(el)

# Видалення файлу
tmp = Path('empty.txt')
if tmp.exists():
    tmp.unlink()