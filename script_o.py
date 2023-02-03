import os
import math
import win32com.client
import subprocess
from pathlib import Path

downloads = str(Path.home() / "Downloads")
txtFile = open(downloads + "\Objava.txt","w+")
filename = ""
word = win32com.client.Dispatch('Word.Application')

os.chdir(downloads)
files = filter(os.path.isfile, os.listdir(downloads))
files = os.listdir(downloads) # add path to each file
files.sort(key=lambda x: os.path.getmtime(os.path.join(downloads, x)))

files.remove("desktop.ini")
if ("Objava.txt") in files:
    files.remove("Objava.txt")

index = 0
tempIndex = 0

txtFile.write("NASLOV CLANKA: " + "\n"*3)
location = input("Lokacija datoteka: ")


for every_file in files:
    filename = os.path.splitext(every_file)[0]

    if every_file.endswith(".xlsx") or every_file.endswith(".zip") or every_file.endswith(".rar") or every_file.endswith(".xls") or every_file.endswith(".csv") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods") or every_file.endswith(".odt") or every_file.endswith(".rtf"):

        if index - tempIndex == 1:
            tempIndex = tempIndex + 2
            index = index + 1
            continue

        #User inputs the operation for the file
        operation = input("Unesi naredbu za datoteku " + '"' + every_file + '"' + " o/p/d: ")
        if operation == "p":
            print("Prebacujem datoteku u PDF format...")
            doc = word.Documents.Open(os.path.join(downloads, every_file))
            pdfname = filename + ".pdf"
            doc.SaveAs(os.path.join(downloads, pdfname), FileFormat=17)
            doc.Close()
            os.remove(os.path.join(downloads, every_file))   
            files.remove(every_file) 
            files.insert(index, pdfname)

        elif operation == "d":
            print("Prebacujem datoteku " + '"' + every_file + '"' + " u PDF i WORD format...")
            doc = word.Documents.Open(os.path.join(downloads, every_file))
            pdfname = filename + ".pdf"
            doc.SaveAs(os.path.join(downloads, pdfname), FileFormat=17)
            doc.Close()
            files.insert(index + 1, pdfname)
            index = index + 1

    index = index + 1
    tempIndex = tempIndex + 1


for every_file in files:

    filename = os.path.splitext(every_file)[0]

    
    if every_file.endswith(".xlsx") or every_file.endswith(".zip") or every_file.endswith(".rar") or every_file.endswith(".xls") or every_file.endswith(".csv") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods") or every_file.endswith(".odt") or every_file.endswith(".rtf"):


        ext = os.path.splitext(every_file)[1]

        filename = filename.replace("  ", " ")
        filename = filename.replace("   ", " ")
        filename = filename.replace("    ", " ")
        filename = filename.replace("     ", " ")
        filename = filename.replace(" ", "_")
        filename = filename.replace("–", "_")
        filename = filename.replace(".", "_")
        filename = filename.replace("-", "_")
        filename = filename.replace(",", "_")
        filename = filename.replace(";", "_")
        filename = filename.replace(":", "_")
        filename = filename.replace("Č", "C")
        filename = filename.replace("č", "c")
        filename = filename.replace("Ć", "C")
        filename = filename.replace("ć", "c")
        filename = filename.replace("Đ", "D")
        filename = filename.replace("đ", "d")
        filename = filename.replace("Š", "S")
        filename = filename.replace("š", "s")
        filename = filename.replace("!", "_")
        filename = filename.replace("Ž", "Z")
        filename = filename.replace("ž", "z")
        filename = filename.replace("__", "_")
        filename = filename.replace("__", "_")
        filename = filename.replace("___", "_")
        filename = filename.replace("(", "")
        filename = filename.replace(")", "")
        filename = filename[0].upper() + filename[1:]
        if filename[-1] == "_":
            filename = filename[:-1]
        
        rename = every_file.replace(every_file, filename + ext)
        os.rename(os.path.join(downloads, every_file), os.path.join(downloads, rename))

        bits_size = os.path.getsize(os.path.join(downloads, rename))
        
        txtFile.write(location + "/" + filename + ext + "\n")

        txtFile.write(ext.upper()[1:] + "\n") 
        
        kb_size = bits_size / 1024
        if kb_size > 1024:
            mb_size = round(kb_size / 1024, 1)
            txtFile.write(str(mb_size) + " MB" + "\n"*4)
        else:  
            txtFile.write(str(math.trunc(kb_size)) + " KB" + "\n"*4)

txtFile.write("\n"*4)
txtFile.write("1. Naslov clanka" + "\n"*2)
txtFile.write("2. Datum objave\n")
txtFile.write("3. Kategorija clanka" + "\n"*2)
txtFile.write("4. Naslovna slika\n")
txtFile.write("5. Album" + "\n"*2)
txtFile.write("6. Tekst" + "\n"*2)
txtFile.write("7. Naslovi dokumenata\n")
txtFile.write("8. Velicine dokumenata\n")
txtFile.write("9. Vrsta dokumenta" + "\n"*2)
txtFile.write("10. Radi li link za dokument\n")
txtFile.write("11. Je li dokument tocno imenovan\n")

txtFile.close()

subprocess.call(['cmd.exe', '/c', downloads + '\Objava.txt'])
subprocess.call(["taskkill","/F","/IM","notepad.exe"])

# Deleting all files in downloads folder
for every_file in os.listdir(downloads):
    if every_file.endswith(".xlsx") or every_file.endswith(".xls") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods"):
        os.remove(os.path.join(downloads, every_file))
        
word.Quit()
