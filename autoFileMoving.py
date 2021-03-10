import os
import shutil
import time

sp='C:\\Users\moabbasi\Downloads'
dp='C:\\Users\moabbasi\Downloads\DownloadsMe'

while True:
    print('looping')
    time.sleep(2)
    files=os.listdir(sp)
    for f in files:
        try:
            #if f is not a file but is a directory then we won't move it
            path=os.path.join(sp,f)
            if os.path.isdir(path):
                continue
            #else find the file extension
            extension=f.split('.')[-1]
            if f.endswith(extension):
                directory = os.path.join(dp,extension)
                #if inside target directory that ext. folder exists or not check
                if not os.path.exists(directory):
                    os.mkdir(directory)
                shutil.move(os.path.join(sp,f),os.path.join(directory,f))
        except:
            print('file being used by another package')
            time.sleep(2*60)
