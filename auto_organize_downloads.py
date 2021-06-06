import os
import shutil

destination = 'D:\downloads\mp4s'

if not os.path.exists(destination):
    os.mkdir(destination)

for root, dirs, file in os.walk('.'):
    for singleFile in file:
        filename, file_extension = os.path.splitext(singleFile)
        if file_extension == '.mp4':
            root = root.split('\\')
            root = root[1]
            final_destination = destination + '\\' + singleFile
            if(os.path.exists(final_destination)):
                singleFile = '2' + singleFile
                final_destination = destination + '\\' + singleFile
            print(os.path.abspath(singleFile))
            splitedPath = os.path.abspath(singleFile).split('\\')
            src = os.path.join(
                '\\', splitedPath[0],
                splitedPath[1],
                splitedPath[2],
                splitedPath[3],
                root,
                splitedPath[4])
            src = src.split(':')
            src = src[0] + ':\\' + src[1]
            print(dirs)
            print(src)

            shutil.move(src, final_destination)

print('DONE')
