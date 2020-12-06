import os
import pathlib

for root, dir, file in os.walk ('.'):
  #filename, file_extension = os.path.splitext(file)
  for singleFile in file:
    filename, file_extension = os.path.splitext(singleFile)
    if file_extension == '.mp4':
      print(filename, file_extension)
  
print('XEGA')
filename, file_extension = os.path.splitext('./aaaa/aaa.mp4')
print(filename, file_extension)
