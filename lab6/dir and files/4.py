import os

path = r'/Users/ihlasova75icloud.com/py39/share/jupyter/lab/static/1909.7487a09fefbe7f9eabb6.js.LICENSE.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))
