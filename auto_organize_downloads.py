import os
import shutil

destination = 'D:\downloads\mp4s'
src = ''

if not os.path.exists(destination):
  os.mkdir(destination)

for root, dir, file in os.walk ('.'):
  #filename, file_extension = os.path.splitext(file)
  for singleFile in file:
    filename, file_extension = os.path.splitext(singleFile)
    if file_extension == '.mp4':
      # HERE I GET THE MP4
      print(filename, file_extension)

  
print('XEGA')
filename, file_extension = os.path.splitext('./aaaa/aaa.mp4')
print(filename, file_extension)
