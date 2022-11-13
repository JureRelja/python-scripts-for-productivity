from PIL import Image
from pathlib import Path
import os
import shutil

downloads = str(Path.home() / "Downloads")
imgFile = str(Path.home() / "Downloads/Novi album")
if imgFile is True:
    shutil.rmtree(imgFile)
os.mkdir(imgFile)
i = ["%02d" % x for x in range(1, 200)]
b = 0

for image in os.listdir(downloads):
    
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
        
        