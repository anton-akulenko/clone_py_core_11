import pathlib
pathlib.Path.cwd()

pathlib.Path(r'C:\Users\gahjelle\realpython\file.txt')

pathlib.Path.home() / 'python' / 'scripts' / 'test.py'
pathlib.Path.home().joinpath('python', 'scripts', 'test.py')

# find full path
path = pathlib.Path('test.md')
path.resolve()

path.resolve().parent == pathlib.Path.cwd()
path.parent == pathlib.Path.cwd()

path.parent.parent

# count files

import collections

collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir())