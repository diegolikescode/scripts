import os

depth = 1

stuff = os.path.abspath(os.path.expanduser(os.path.expandvars('.')))
allDirs = ['null']
for root, dirs, files in os.walk(stuff):
    if root[len(stuff):].count(os.sep) < depth:
        allDirs = dirs

for directory in allDirs:
    os.system('cd {0} & call git status & call git pull"'.format(directory))
