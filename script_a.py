import os
import math
import win32com.client
import subprocess
from pathlib import Path

downloads = str(Path.home() / "Downloads")
txtFile = open(downloads + "\Objava.txt","w+", encoding=("utf-8"))
filename = ""
word = win32com.client.Dispatch('Word.Application')

broj_datoteke = 1

os.chdir(downloads)
files = filter(os.path.isfile, os.listdir(downloads))
files = os.listdir(downloads) 
files.sort(key=lambda x: os.path.getmtime(os.path.join(downloads, x)))


files.remove("desktop.ini")
if ("Objava.txt") in files:
    files.remove("Objava.txt")

index = 0
tempIndex = 0

naslov_clanka = input("Unesi naslov članka: ")
txtFile.write("NASLOV CLANKA: " + naslov_clanka + "\n"*3)
location = input("Lokacija datoteka: ")

txtFile.write("<table class=" + '"' + "privitak_table" + '"' + ">\n")
txtFile.write("<tbody>\n")
txtFile.write("<tr>\n")
txtFile.write("<td class=" + '"' + "privitak_td_dokumenti_za_preuzimanje" + '"' + " " + "colspan=" + '"' + str("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE" + "</td>\n")
txtFile.write("</tr>\n")

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
        name_of_the_file =  filename + ext

    
        
        kb_size = bits_size / 1024
        if kb_size > 1024:
            mb_size = round(kb_size / 1024, 1)
            velicina = str(mb_size) + " MB"
        else:  
            velicina = str(math.trunc(kb_size)) + " KB"

        ext_upper = ext.upper()[1:]
        naslov_dokumenta = input("Unesi naslov dokumenta " + '"' + name_of_the_file + '": ')
        privitak_poveznica = "<td class=" + '"' + "privitak_td_poveznica" + '"' + "><a class=" + '"' + "privitak_a" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + " rel=" + '"' + "noopener noreferrer" + '"' + ">" + str(naslov_dokumenta) +  "</a></td>\n"

        txtFile.write("<tr>\n")
        txtFile.write("<td class=" + '"' + "privitak_td_redni_broj" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
        txtFile.write(privitak_poveznica)
        txtFile.write("<td class=" + '"' + "privitak_td_tip_dokumenta" + '"' + ">" + ext_upper + "</td>\n")
        txtFile.write("<td class=" + '"' + "privitak_td_velicina" + '"' + ">" + velicina + "</td>\n")
        txtFile.write("</tr>\n")


        broj_datoteke = broj_datoteke + 1

txtFile.write("</tbody>\n")
txtFile.write("</table>\n")
            
txtFile.close()

subprocess.call(['cmd.exe', '/c', downloads + '\Objava.txt'])
subprocess.call(["taskkill","/F","/IM","notepad.exe"])

# Deleting all files in downloads folder
for every_file in os.listdir(downloads):
    if every_file.endswith(".xlsx") or every_file.endswith(".xls") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods"):
        os.remove(os.path.join(downloads, every_file))
        
word.Quit()