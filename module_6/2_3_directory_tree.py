import pathlib

# relative_to() to represent a path relative to the root directory
# count the number of directories (using the .parts property) 
def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

tree(pathlib.Path.cwd())