import os

def print_directory_structure(rootdir, padding=''):
    for item in os.listdir(rootdir):
        path = os.path.join(rootdir, item)
        if os.path.isdir(path):
            print(padding + '└── ' + item)
            print_directory_structure(path, padding + '    ')
        else:
            print(padding + '├── ' + item)

print_directory_structure('.')