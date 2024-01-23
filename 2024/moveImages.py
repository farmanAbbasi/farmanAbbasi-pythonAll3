import os
import shutil
source = '/users/Desktop'
destination = '/users/Desktop/ss/'

if not os.path.isdir(destination):
    os.makedirs(destination)

allfiles = os.listdir(source)
counter=0
# iterate on all files to move them to destination folder
for f in allfiles:
    if f.endswith(".png"):
      
        counter+=1
        #get month and date of screenshot
        my_dest = f[10:18]
        destination_temp=destination+my_dest
        #update destination with month folder      
        if not os.path.isdir(destination_temp):
            os.makedirs(destination_temp)
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination_temp, f)
        shutil.move(src_path, dst_path)
print(counter," .pngs moved successfully to /ss folder")
