import os
import pathlib
string = 'hello world'
found = []
for letter in string:
    next_entry = False
    for root, dirs, files in os.walk(os.getenv('HOME')):
        for file in files:
            if letter in pathlib.Path(root, file).name and file not in found:
                found.append(file)
                next_entry = True
                print(f'{letter} found in {root}/{file}')
            if next_entry:
                break
        if next_entry:
            break
    if next_entry:
        continue
