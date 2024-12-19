import os
from PIL import Image, ImageOps
import os
import shutil
from os.path import exists

#Function for removing files that are not images¸¸  
def removeFiles(array, downloads):
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

#Function for resizing images
def resize(downloads, imgFile, websiteGen):

    if os.path.isdir(imgFile) is True:
        shutil.rmtree(imgFile) #Deletes the folder if it exists

    os.mkdir(imgFile) #Creates the folder
    i = ["%03d" % x for x in range(1, 200)] #Creates a list of numbers from 1 to 200
    b = 0
    second_album_type = ""

    images = os.listdir(downloads)
    
    removeFiles(images, downloads)

    try:
        images.sort(key=lambda x: int(x.split(".")[0])) #Sort
    except ValueError or IndexError: 
        images.sort(key=lambda x: x.split(".")[0]) #Sorts


    if "naslovna.jpg" not in os.listdir(downloads) and "1.jpg" in os.listdir(downloads) and len(removeFiles(os.listdir(downloads), downloads)) > 2 and (websiteGen == 2 or websiteGen == 3):
        action = input("Zelite li kreirati objavu takvu da je slika pod nazivom '1.jpg' na vrhu kao album te da se ispod prikazuje dodatan album sa svim slikama? U protivnom ce se prikazivati samo jedan album na dnu sa svim slikama. d/n: ")

        if action == "D" or action == "d":
            second_album_type = "main_img_album_and_galery"

    if "naslovna.jpg" not in os.listdir(downloads) and "1.jpg" in os.listdir(downloads) and "2.jpg" in os.listdir(downloads) and len(removeFiles(os.listdir(downloads), downloads)) == 4 and (websiteGen == 2 or websiteGen == 3):
        action = input("Zelite li kreirati objavu takvu da se na vrhu bude album sa slikom '1.jpg', a na dnu album sa slikom '2.jpg'? d/n: ")

        if action == "D" or action == "d":
            second_album_type = "two_albums"

    for image in images:
        #Checks if the file is an image
        if (image == "naslovna.jpg"):
            continue

        if  second_album_type == "two_albums":
            b = 1
            break

        if  image == "1.jpg" and second_album_type == "main_img_album_and_galery":
            continue
            
        if (image == "1.jpg" or image == "1.webp") and (len(removeFiles(os.listdir(downloads), downloads)) == 3 or len(removeFiles(os.listdir(downloads), downloads)) == 2):
            b = 1
            if image == "1.webp":
                action = input("Zelite li sliku '1.webp' pretvoriti u '1.jpg'? Odaberite 'd' jedino ako '1.webp' već ima točne timenzije. d/n: ")

                if action == "D" or action == "d":
                    img = Image.open(os.path.join(downloads, image)).convert("RGB")
                    img.save("1.jpg", "jpeg")
            break        
    
        if image.endswith(".jpg") or image.endswith(".JPG") or image.endswith(".png") or image.endswith(".PNG") or image.endswith(".jpeg") or image.endswith(".JPEG"):
            ime = i[b]
            img = Image.open(os.path.join(downloads, image))
            img = img.convert("RGB")
            name = "/" + str(ime) + ".jpg"
            img_destination_name = imgFile + str(name)

            img = ImageOps.exif_transpose(img)
            img.thumbnail((1000, 1000))
            img.save(img_destination_name)
            b = b + 1
    return [b, second_album_type];