# This one will walk through the root dir and commiting every repo that is in the dir that this file is.
import os

depth = 1

stuff = os.path.abspath(os.path.expanduser(os.path.expandvars('.')))
allDirs = ['null']
for root, dirs, files in os.walk(stuff):
  if root[len(stuff):].count(os.sep) < depth:
    allDirs = dirs

print(allDirs)
for directory in allDirs:
  os.system('cd {0} & call git status & git add . & git commit -m "test: script to commit everything & git push"'.format(directory))
