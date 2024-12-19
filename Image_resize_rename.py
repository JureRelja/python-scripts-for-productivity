from PIL import Image
from pathlib import Path
import os
import shutil

#Function for removing files that are not images¸¸  
def removeFiles(array):
    filesLenght = len(array) #Getting the number of files in the downloads folder
    i = 0
    #or os.path.isdir(downloads + "/" + array[i]) or array[i].endswith(".ini")
    while i < filesLenght:
        if array[i].endswith(".xlsx") or array[i] == "Album" or array[i] == "naslovna.jpg" or array[i] == "desktop.ini" or array[i].endswith(".zip") or array[i].endswith(".rar") or array[i].endswith(".xls") or array[i].endswith(".csv") or array[i].endswith(".docx") or array[i].endswith(".pdf") or array[i].endswith(".doc") or array[i].endswith(".ods") or array[i].endswith(".odt") or array[i].endswith(".rtf"):
            array.pop(i)
            i -= 1
            filesLenght -= 1
        i += 1
    return array

downloads = str(Path.home() / "Downloads")
imgFile = str(Path.home() / "Downloads/Album")

if imgFile is True:
    shutil.rmtree(imgFile)
os.mkdir(imgFile)
i = ["%03d" % x for x in range(1, 200)]
b = 0

images = os.listdir(downloads)

removeFiles(images)

try:
    images.sort(key=lambda x: int(x.split(".")[0])) #Sort
except ValueError or IndexError: 
    images.sort(key=lambda x: x.split(".")[0]) #Sorts

for image in images:
    
    if image.endswith(".jpg") or image.endswith(".JPG") or image.endswith(".png"):
        ime = i[b]
        img = Image.open(os.path.join(downloads, image))
        size = img.size
        name = "/" + str(ime) + ".jpg"
        img_destination_name = imgFile + str(name)
        print(img_destination_name)
        img.thumbnail((1000, 1000))
        img.save(img_destination_name)
        b = b + 1
        
        