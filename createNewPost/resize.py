import os
from PIL import Image, ImageOps
import os
import shutil
from os.path import exists

#Function for resizing images
def resize(downloads, imgFile):

    if os.path.isdir(imgFile) is True:
        shutil.rmtree(imgFile) #Deletes the folder if it exists

    os.mkdir(imgFile) #Creates the folder
    i = ["%02d" % x for x in range(1, 200)] #Creates a list of numbers from 1 to 200
    b = 0

    for image in os.listdir(downloads):
        #Checks if the file is an image
        if (image == "naslovna.jpg"):
            continue

        if  "1.jpg" in os.listdir(downloads) and "2.jpg" in os.listdir(downloads) and len(os.listdir(downloads)) == 4:
            b = "two_albums"
            return b;
        
        if (image == "1.jpg") and (len(os.listdir(downloads)) == 4 or len(os.listdir(downloads)) == 3):
            b = 1
            return b
        
       # if len(os.listdir(downloads)) == 4 and "naslovna.jpg" in os.listdir(downloads):
       #     b = 0
       #     return b

        if image.endswith(".jpg") or image.endswith(".JPG") or image.endswith(".png") or image.endswith(".PNG") or image.endswith(".jpeg") or image.endswith(".JPEG"):
            ime = i[b]
            img = Image.open(os.path.join(downloads, image))
            img = img.convert("RGB")
            name = "/" + str(ime) + ".jpg"
            img_destination_name = imgFile + str(name)
            print(img_destination_name)
            img = ImageOps.exif_transpose(img)
            img.thumbnail((1000, 1000))
            img.save(img_destination_name)
            b = b + 1

    return b;