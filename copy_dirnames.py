import os

for root, dirs, file in os.walk('.'):
    print(dirs)