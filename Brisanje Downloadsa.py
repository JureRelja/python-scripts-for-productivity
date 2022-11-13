import os


downloads = "C:\\Users\jurer\Downloads"


for every_file in os.listdir(downloads):
    if every_file.endswith(".xlsx") or every_file.endswith(".xls") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods"):
        os.remove(os.path.join(downloads, every_file))
