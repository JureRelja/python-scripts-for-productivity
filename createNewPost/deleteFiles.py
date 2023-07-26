import os
import shutil

def deleteFiles(downloads):
    # Deleting all files in downloads folder
    for every_file in os.listdir(downloads):

        #Deleting all files in downloads folder
        if every_file.endswith(".xlsx") or every_file.endswith(".xls") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods"):
            os.remove(os.path.join(downloads, every_file))

        #Deleting all files in downloads folder
        if every_file.endswith(".jpg") or every_file.endswith(".jpeg") or every_file.endswith(".png"):
            os.remove(os.path.join(downloads, every_file))

        #Deleting Album folder in the downloads folder
        elif every_file == "Album":
            shutil.rmtree(downloads + "\\" + every_file)