import os
import shutil

def deleteFiles(downloads, files):
    # Deleting all files in downloads folder
    for every_file in files:

        #Deleting all files in downloads folder
        if every_file.endswith(".xlsx") or every_file.endswith(".xls") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods"):
            os.remove(downloads + "\\" + every_file)

        #Deleting all files in downloads folder
        if every_file.endswith(".jpg") or every_file.endswith(".jpeg") or every_file.endswith(".png"):
            os.remove(downloads + "\\" + every_file)

        #Deleting Album folder in the downloads folder
        elif every_file == "Album":
            shutil.rmtree(downloads + "\\" + every_file)