import os
entries = os.listdir('.')
print(entries)

# List all files in a directory using os.listdir
basepath = '.'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)


from pathlib import Path

basepath = Path('.')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)


# get the time the files

from datetime import datetime
from os import scandir
"""
scandir Returns an iterator of all the objects in a directory including file attribute information
"""


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files():
    dir_entries = scandir('.')
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')

get_files()