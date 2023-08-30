import os
import math
import win32com.client
import subprocess
from pathlib import Path
import inquirer

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

sveStranice = [
  inquirer.List('tablica',
                message="Za koju stranicu želiš napraviti tablicu",
                choices=['drnis.hr', 'djecji-vrtic-drnis.hr',  'ss-ivana-mestrovica-drnis.hr', 'ogsko.hr', 'zena-drnis.hr', 'vrtic-trogir.hr', 'djecji-vrtic-marina.hr', 'pucko-otvoreno-uciliste-drnis.hr', 'promina.hr', 'dv-seget.hr', "eko-promina.hr", 'narodna-knjiznica-drnis.hr', 'gmd.hr', 'biskupija.hr', 'ligaprotivrakadrnis.hr', "nkdosk.hr", 'kalun.hr', 'gradskacistoca-drnis.hr',  'jvp-drnis.hr',  'komunalno-drustvo-biskupija.hr',  'lag-krka.hr', 'silvijasunara.com', 'ljekarna-drnis.hr'],
            ),
]

odabranaStranica = inquirer.prompt(sveStranice)


# Djecji vrtić Drniš tablica 
if odabranaStranica['tablica'] == 'djecji-vrtic-drnis.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #bc0101; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 60px;" + '"' + ">" + "Veličina" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 60px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
    txtFile.write("</tr>\n")

# Kalun tablica
elif odabranaStranica['tablica'] == 'kalun.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%;  color: #dd001a; margin-bottom: 30px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px; width: 50px;" + '"' + ">" + "Tip" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px; width: 80px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
    txtFile.write("</tr>\n")

    #New websites table
elif odabranaStranica['tablica'] == "drnis.hr" or odabranaStranica['tablica'] == "eko-promina.hr" or odabranaStranica['tablica'] == "djecji-vrtic-marina.hr" or odabranaStranica['tablica'] == "dv-seget.hr" or odabranaStranica['tablica'] == "nkdosk.hr" or odabranaStranica['tablica'] == "narodna-knjiznica-drnis.hr":
    txtFile.write("<table class=" + '"' + "privitak_table" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    if odabranaStranica['tablica'] != "djecji-vrtic-marina.hr":
        txtFile.write("<tr>\n")
        txtFile.write("<td class=" + '"' + "privitak_td_dokumenti_za_preuzimanje" + '"' + " " + "colspan=" + '"' + str("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE" + "</td>\n")
        txtFile.write("</tr>\n")

# Vrtic Trogir tablica
elif odabranaStranica['tablica'] == 'vrtic-trogir.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")

# Gradski muzej Drniš tablica
elif odabranaStranica['tablica'] == 'gradski-muzej-drnis.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")

# Gradska čistoća Drniš tablica
elif odabranaStranica['tablica'] == 'gradskacistoca-drnis.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")

# Osnovna glazbena škola Krsto Odak tablica 
elif odabranaStranica['tablica'] == 'ogsko.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #2d7d9a; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
    txtFile.write("</tr>\n")

# JVP Drniš tablica
elif odabranaStranica['tablica'] == 'jvp-drnis.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")

# Općina Biskupija tablica
elif odabranaStranica['tablica'] == 'biskupija.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #666666; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")

# Komunalno Društvo Biskupija tablica
elif odabranaStranica['tablica'] == 'komunalno-drustvo-biskupija.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")

# SS Ivana Meštrovića Drniš tablica 
elif odabranaStranica['tablica'] == 'ss-ivana-mestrovica-drnis.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #895a78; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
    txtFile.write("</tr>\n")

# LAG Krka tablica
elif odabranaStranica['tablica'] == 'lag-krka.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 35px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td colspan=" + '"' + ("4") + '"' + ">\n")
    txtFile.write("<h3 class=" + '"' + "uk-h4 uk-heading-bullet" + '"'  + ">" + "Dokumenti za preuzimanje" + "</h3>\n")
    txtFile.write("</td>\n")
    txtFile.write("</tr>\n")

# Pučko otvoreno učilište tablica 
elif odabranaStranica['tablica'] == 'pucko-otvoreno-uciliste-drnis.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #2a506d; font-weight: normal; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "PRILOŽENI DOKUMENTI:" + "</td>\n")
    txtFile.write("</tr>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
    
    txtFile.write("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
    txtFile.write("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px; width: 70px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
    txtFile.write("</tr>\n")

    #Promina tablica
elif odabranaStranica['tablica'] == "promina.hr":
    txtFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-top: 10px;" + '"' + ">\n")
    txtFile.writelines("<tbody>\n")
    txtFile.writelines("<tr>\n")
    txtFile.writelines("<td style=" + '"' + "text-align: left; color: #0071a5; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.writelines("</tr>\n")
    txtFile.writelines("<tr>\n")
    txtFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
    txtFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
    txtFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
    txtFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
    txtFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
    txtFile.writelines("</tr>\n")


# Žena Drniš tablica
elif odabranaStranica['tablica'] == 'zena-drnis.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")

 #New websites table
elif odabranaStranica['tablica'] == "drnis.hr" or odabranaStranica['tablica'] == "eko-promina.hr" or odabranaStranica['tablica'] == "djecji-vrtic-marina.hr" or odabranaStranica['tablica'] == "dv-seget.hr" or odabranaStranica['tablica'] == "nkdosk.hr" or odabranaStranica['tablica'] == "narodna-knjiznica-drnis.hr":

    txtFile.write("<table class=" + '"' + "privitak_table" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td class=" + '"' + "privitak_td_dokumenti_za_preuzimanje" + '"' + " " + "colspan=" + '"' + str("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE" + "</td>\n")
    txtFile.write("</tr>\n")

# Ljekarna Drniš tablica
elif odabranaStranica['tablica'] == 'ljekarna-drnis.hr':

    txtFile.write("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
    txtFile.write("<tbody>\n")
    txtFile.write("<tr>\n")
    txtFile.write("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
    txtFile.write("</tr>\n")

for every_file in files:
    filename = os.path.splitext(every_file)[0]
    ext = os.path.splitext(every_file)[1]

    if every_file.endswith(".xlsx") or every_file.endswith(".zip") or every_file.endswith(".rar") or every_file.endswith(".xls") or every_file.endswith(".csv") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods") or every_file.endswith(".odt") or every_file.endswith(".rtf"):

        if index - tempIndex == 1:
            tempIndex = tempIndex + 1
            continue

        if ext == ".pdf" or ext == ".zip":
            index = index + 1
            tempIndex = tempIndex + 1
            continue

        #User inputs the operation for the file
        operation = input("Unesi naredbu za datoteku " + '"' + every_file + '"' + " o/p/d: ")
            
        if operation == "p" or operation == "P":
            print("Prebacujem datoteku u PDF format...")
            doc = word.Documents.Open(os.path.join(downloads, every_file))
            pdfname = filename + ".pdf"
            doc.SaveAs(os.path.join(downloads, pdfname), FileFormat=17)
            doc.Close()
            os.remove(os.path.join(downloads, every_file))   
            files.remove(every_file) 
            files.insert(index, pdfname)

        elif operation == "d" or operation == "D":
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
    
    if every_file.endswith(".xlsx") or every_file.endswith(".xls") or every_file.endswith(".zip") or every_file.endswith(".rar") or every_file.endswith(".csv") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods") or every_file.endswith(".odt") or every_file.endswith(".rtf"):


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


        naslov_dokumenta = "" #Asking the user for the name of the file

        uppercased_filename = filename.upper()

        #Universal names
        if uppercased_filename == "POZIV_NA_DOSTAVU_PONUDA":
            naslov_dokumenta = "POZIV NA DOSTAVU PONUDA"
        elif uppercased_filename == "TROSKOVNIK":
            naslov_dokumenta = "TROŠKOVNIK"
        elif uppercased_filename == "PONUDBENI_LIST":
            naslov_dokumenta = "PONUDBENI LIST"
        elif uppercased_filename == "ODLUKA_O_ODABIRU":
            naslov_dokumenta = "ODLUKA O ODABIRU"
        elif uppercased_filename == "ODLUKA_O_PONISTENJU":
            naslov_dokumenta = "ODLUKA O PONIŠTENJU"
        elif uppercased_filename.split("_")[-1] == "POZIV":
            naslov_dokumenta == "POZIV - DNEVNI RED"
        elif uppercased_filename == "DODATAK_PONUDBENOM_LISTU_1A" or uppercased_filename == "DODATAK_PONUDBENOM_LISTU_1":
            naslov_dokumenta = "DODATAK PONUDBENOM LISTU U SLUČAJU ZAJEDNICE PONUDITELJA"
        elif uppercased_filename == "DODATAK_PONUDBENOM_LISTU_1B" or uppercased_filename == "DODATAK_PONUDBENOM_LISTU_2":
            naslov_dokumenta = "DODATAK PONUDBENOM LISTU U SLUČAJU PODUGOVARATELJA"
        elif uppercased_filename.split("_")[-1] == "ZAPISNIK":
            naslov_dokumenta == "ZAPISNIK"
            
        #drnis.hr file names
        elif uppercased_filename.split("_")[-1] == "AKTI" and odabranaStranica["tablica"] == "drnis.hr":
            naslov_dokumenta == "AKTI"
        elif uppercased_filename.split("_")[-1] == "RED" and uppercased_filename.split("_")[-2] == "DNEVNI" and odabranaStranica["tablica"] == "drnis.hr":
            naslov_dokumenta == "DNEVNI RED"

        #promina.hr file names
        elif uppercased_filename.split("_")[-1] == "AKATA" and odabranaStranica["tablica"] == "promina.hr":
            naslov_dokumenta == "USVOJENI AKTI"
        elif uppercased_filename.split("_")[-1] == "AKATA" and odabranaStranica["tablica"] == "promina.hr":
            naslov_dokumenta == "PRIJEDLOZI AKATA"
        
        else:
            naslov_dokumenta = input("Unesi naslov dokumenta " + '"' + name_of_the_file + '": ')


        #Djecji vrtić Drniš tablica
        if odabranaStranica["tablica"] == "djecji-vrtic-drnis.hr":
            if ext == ".rar" or ext == ".zip":
                ekstenzija = "images/05_DOCUMENT_ICONS/rar.png"
            elif ext == ".pdf":
                ekstenzija = "images/05_DOCUMENT_ICONS/pdf.png"
            elif ext== ".xlsx" or ext == ".xls":
                ekstenzija = "images/05_DOCUMENT_ICONS/xls.png"
            else:
                ekstenzija = "images/05_DOCUMENT_ICONS/doc.png"

            privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #bbbbbb;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + ">" + "<img src=" + '"' + "images/05_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "border=" + '"' + "0" + '"' + "/></a></td>\n"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #bbbbbb;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #bbbbbb;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #bbbbbb;" + '"' + ">" + naslov_dokumenta + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #bbbbbb;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write(privitak_poveznica)
            txtFile.write("</tr>\n")

         #Kalun tablica
        elif odabranaStranica["tablica"] == "kalun.hr":
            if ext == ".rar" or ext == ".zip":
                ekstenzija = "images/06_DOCUMENT_ICONS/rar.png"
            elif ext == ".pdf":
                ekstenzija = "images/06_DOCUMENT_ICONS/pdf.png"
            elif ext== ".xlsx" or ext == ".xls":
                ekstenzija = "images/06_DOCUMENT_ICONS/xls.png"
            else:
                ekstenzija = "images/06_DOCUMENT_ICONS/doc.png"

            privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #ebebeb; padding: 2px 5px 2px 5px;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">" + "<img src=" + '"' + "images/06_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "/></a></td>\n"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #ebebeb; padding: 2px 5px 2px 5px; background-color: #ffffff;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #ebebeb; padding: 2px 5px 2px 5px; background-color: #ffffff;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 2px 5px 2px 5px; border: solid 1px #ebebeb; background-color: #ffffff;" + '"' + ">" + naslov_dokumenta + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #ebebeb; padding: 2px 5px 2px 5px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write(privitak_poveznica)
            txtFile.write("</tr>\n")

        #New websites table
        elif odabranaStranica["tablica"] == "drnis.hr" or odabranaStranica["tablica"] == "eko-promina.hr" or odabranaStranica["tablica"] == "djecji-vrtic-marina.hr" or odabranaStranica["tablica"] == "dv-seget.hr" or odabranaStranica["tablica"] == "nkdosk.hr" or odabranaStranica["tablica"] == "narodna-knjiznica-drnis.hr":
            ext_upper = ext.upper()[1:]

            privitak_poveznica = "<td class=" + '"' + "privitak_td_poveznica" + '"' + "><a class=" + '"' + "privitak_a" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + " rel=" + '"' + "noopener noreferrer" + '"' + ">" + naslov_dokumenta +  "</a></td>\n"
            txtFile.write("<tr>\n")
            txtFile.write("<td class=" + '"' + "privitak_td_redni_broj" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write(privitak_poveznica)
            txtFile.write("<td class=" + '"' + "privitak_td_tip_dokumenta" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("<td class=" + '"' + "privitak_td_velicina" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("</tr>\n")

        # Vrtic Trogir tablica
        elif odabranaStranica["tablica"] == "vrtic-trogir.hr":
            ext_upper = ext.upper()[1:]

            privitak_poveznica = "<a style=" + '"' + "color: #de5543; font-weight: 500; font-style: normal; text-transform: uppercase; letter-spacing: 1px; text-decoration: none;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #fff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("</tr>\n")

 #New websites table
        elif odabranaStranica["tablica"] == "drnis.hr" or odabranaStranica["tablica"] == "eko-promina.hr" or odabranaStranica["tablica"] == "djecji-vrtic-marina.hr" or odabranaStranica["tablica"] == "dv-seget.hr" or odabranaStranica["tablica"] == "nkdosk.hr" or odabranaStranica["tablica"] == "narodna-knjiznica-drnis.hr":
            ext_upper = ext.upper()[1:]
            
            privitak_poveznica = "<td class=" + '"' + "privitak_td_poveznica" + '"' + "><a class=" + '"' + "privitak_a" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + " rel=" + '"' + "noopener noreferrer" + '"' + ">" + str(naslov_dokumenta) +  "</a></td>\n"

            txtFile.write("<tr>\n")
            txtFile.write("<td class=" + '"' + "privitak_td_redni_broj" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write(privitak_poveznica)
            txtFile.write("<td class=" + '"' + "privitak_td_tip_dokumenta" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("<td class=" + '"' + "privitak_td_velicina" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("</tr>\n")

        elif odabranaStranica["tablica"] == "promina.hr":
            privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #bbbbbb;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + " rel=" + '"' + "noopener noreferrer" + '"' + ">" + "<img src=" + '"' + "images/11_IKONE_DOKUMENATA/download.png" + '"' +  " alt=" + '"' + '"' + " /></a></td>\n"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #bbbbbb;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #bbbbbb;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #bbbbbb;" + '"' + ">" + naslov_dokumenta + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #bbbbbb;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write(privitak_poveznica)
            txtFile.write("</tr>\n")


        # Gradski muzej Drniš tablica
        elif odabranaStranica["tablica"] == "gradski-muzej-drnis.hr":
            ext_upper = ext.upper()[1:]

            privitak_poveznica = "<a style=" + '"' + "color: #c81342; font-family: 'Raleway', Helvetica, Arial, sans-serif; font-weight: 500; font-style: normal; text-transform: uppercase; letter-spacing: 1px; text-decoration: none;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #fff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("</tr>\n")

         # Gradska čistoća Drniš tablica
        elif odabranaStranica["tablica"] == "gradskacistoca-drnis.hr":
            ext_upper = ext.upper()[1:]

            privitak_poveznica = "<a style=" + '"' + "color: #39b54a; text-decoration: none;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #fff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("</tr>\n")

        # Osnovna glazbena škola Krsto Odak tablica
        elif odabranaStranica["tablica"] == "ogsko.hr":
            if ext == ".rar" or ext == ".zip":
                ekstenzija = "images/01_SLIKE/03_DOCUMENT_ICONS/rar.png"
            elif ext == ".pdf":
                ekstenzija = "images/01_SLIKE/03_DOCUMENT_ICONS/pdf.png"
            elif ext== ".xlsx" or ext == ".xls":
                ekstenzija = "images/01_SLIKE/03_DOCUMENT_ICONS/xls.png"
            else:
                ekstenzija = "images/01_SLIKE/03_DOCUMENT_ICONS/doc.png"

            privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + ">" + "<img src=" + '"' + "images/01_SLIKE/03_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "/></a></td>\n"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + naslov_dokumenta + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write(privitak_poveznica)
            txtFile.write("</tr>\n")

        # JVP Drniš tablica
        elif odabranaStranica["tablica"] == "jvp-drnis.hr":
            if ext == ".rar" or ext == ".zip":
                ekstenzija = "images/01_slike/04_document_icons/rar.png"
            elif ext == ".pdf":
                ekstenzija = "images/01_slike/04_document_icons/pdf.png"
            elif ext== ".xlsx" or ext == ".xls":
                ekstenzija = "images/01_slike/04_document_icons/xls.png"
            else:
                ekstenzija = "images/01_slike/04_document_icons/doc.png"

            privitak_poveznica = "<a href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + "<img style=" + '"' + "padding: 5px 0px; float:none;" + '"' + "src=" + '"' + ekstenzija + '"' + " alt=" + '"' + "/></td>\n")
            txtFile.write("</tr>\n")

         # Općina Biskupija tablica
        elif odabranaStranica["tablica"] == "biskupija.hr":
            ext_upper = ext.upper()[1:]

            privitak_poveznica = "<a style=" + '"' + "color: #d40e08; text-decoration: none;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("</tr>\n")

         # Komunalno društvo Biskupija tablica
        elif odabranaStranica["tablica"] == "komunalno-drustvo-biskupija.hr":
            ext_upper = ext.upper()[1:]

            privitak_poveznica = "<a style=" + '"' + "color: #078d39; text-decoration: none; font-weight: bold;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("</tr>\n")

        # SS Ivana Meštrovića Drniš tablica
        elif odabranaStranica["tablica"] == "ss-ivana-mestrovica-drnis.hr":
            if ext == ".rar" or ext == ".zip":
                ekstenzija = "images/04_DOCUMENT_ICONS/rar.png"
            elif ext == ".pdf":
                ekstenzija = "images/04_DOCUMENT_ICONS/pdf.png"
            elif ext== ".xlsx" or ext == ".xls":
                ekstenzija = "images/04_DOCUMENT_ICONS/xls.png"
            else:
                ekstenzija = "images/04_DOCUMENT_ICONS/doc.png"

            privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #f7eff5; border: solid 1px #d6aaca; color: #333333;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + ">" + "<img src=" + '"' + "images/04_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "/></a></td>\n"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #d6aaca; background-color: #f7eff5; color: #333333;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #d6aaca; background-color: #f7eff5; color: #333333;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #d6aaca; background-color: #f7eff5; color: #333333;" + '"' + ">" + naslov_dokumenta + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #f7eff5; border: solid 1px #d6aaca; color: #333333;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write(privitak_poveznica)
            txtFile.write("</tr>\n")

        # LAG Krka tablica
        elif odabranaStranica["tablica"] == "lag-krka.hr":
            ext_upper = ext.upper()[1:]

            privitak_poveznica = "<a class=" + '"' "uk-h4 uk-heading" + '"' + "style=" + '"' + "color: #f9591e; font-weight: 400; line-height: 1.5;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #eee; background-color: #fff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td class=" + '"' + "uk-h4 uk-heading" + '"' + "style=" + '"' + "text-align: left; background-color: #fff; border: solid 1px #eee; vertical-align: middle; padding: 3px 5px 3px 5px;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #eee; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #eee; color: #666666; width: 50px;" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("</tr>\n")

        # SS Ivana Meštrovića Drniš tablica
        elif odabranaStranica["tablica"] == "pucko-otvoreno-uciliste-drnis.hr":
            if ext == ".rar" or ext == ".zip":
                ekstenzija = "images/06_DOCUMENT_ICONS/rar.png"
            elif ext == ".pdf":
                ekstenzija = "images/06_DOCUMENT_ICONS/pdf.png"
            elif ext== ".xlsx" or ext == ".xls":
                ekstenzija = "images/06_DOCUMENT_ICONS/xls.png"
            else:
                ekstenzija = "images/06_DOCUMENT_ICONS/doc.png"

            privitak_poveznica = "<td style=" + '"' + "text-align: center; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + "><a style=" + '"' + "color: #2a506d; font-weight: bold; font-size: 13px;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + ">" + "<img style=" + '"' + "border: solid 0px #fff;" + '"' +  "src=" + '"' + "images/06_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "/></a></td>\n"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 3px 3px 3px 6px; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + ">" + naslov_dokumenta + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + ">" +  "<img style=" + '"' "border: solid 0px #fff;" '"' + " src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
            
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write(privitak_poveznica)
            txtFile.write("</tr>\n")

        # Žena Drniš tablica
        elif odabranaStranica["tablica"] == "zena-drnis.hr":
            ext_upper = ext.upper()[1:]

            privitak_poveznica = "<a style=" + '"' + "color: #e77918; text-decoration: none;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("</tr>\n")

        # Ljekarna Drniš tablica
        elif odabranaStranica["tablica"] == "ljekarna-drnis.hr":
            ext_upper = ext.upper()[1:]

            privitak_poveznica = "<a style=" + '"' + "color: #02813e; text-decoration: none;" + '"' + " href=" + '"' + (location + "/" + name_of_the_file) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

            txtFile.write("<tr>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
            txtFile.write("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
            txtFile.write("</tr>\n")

        broj_datoteke = broj_datoteke + 1

txtFile.write("</tbody>\n")
txtFile.write("</table>\n")

txtFile.close()

subprocess.call(['cmd.exe', '/c', downloads + '\Objava.txt'])
subprocess.call(["taskkill","/F","/IM","notepad.exe"])

# Deleting all files in downloads folder
for every_file in os.listdir(downloads):
    if every_file.endswith(".xlsx") or every_file.endswith(".xls") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods") or every_file == "Objava.txt":
        os.remove(os.path.join(downloads, every_file))

        
word.Quit()



