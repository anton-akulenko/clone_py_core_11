import shutil
from pathlib import Path

P = Path('.')

def foo(name: str) -> str:
    return f'Hello {name}'

def make():
    shutil.make_archive('arch', 'zip', P)


def grab(a):
    print(a)


# print(__name__)
if __name__ == '__main__':
    print(foo('Alex'))