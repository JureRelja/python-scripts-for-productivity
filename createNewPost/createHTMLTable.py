import os
import math
import win32com.client

from rename import rename #Importing the function from rename.py

word = win32com.client.Dispatch('Word.Application')

def createHTMLTable(files, date, tempFile, selectedWebsite, downloads, categoryName):
    tableExist = False

    if (len(files) == 0):
        return

    folder = str(date["month"]).rjust(2, '0') + "_" + str(date["day"]).rjust(2, '0') #Adding leading zeros to the day and month
    year = str(date["year"]) #Getting the year
    
    broj_datoteke = 1

    #Creating the header of the table
        # Djecji vrtić Drniš tablica 
    if selectedWebsite == 'djecji-vrtic-drnis.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #bc0101; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 60px;" + '"' + ">" + "Veličina" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 60px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
        tempFile.writelines("</tr>\n")

        #Grad Drniš tablica
    elif selectedWebsite == 'drnis.hr':
        tempFile.writelines("<table class=" + '"' + "privitak_table" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td class=" + '"' + "privitak_td_dokumenti_za_preuzimanje" + '"' + " " + "colspan=" + '"' + str("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE" + "</td>\n")
        tempFile.writelines("</tr>\n")

        #Promina tablica
    elif selectedWebsite == "promina.hr":
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-top: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #0071a5; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #cccccc; border: solid 1px #bbbbbb; color: #444444; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # Kalun tablica
    elif selectedWebsite == 'kalun.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%;  color: #dd001a; margin-bottom: 30px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px; width: 50px;" + '"' + ">" + "Tip" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #1187d1; border: solid 1px #ebebeb; color: #fff; font-weight: normal; font-size: 12px; width: 80px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # Vrtic Trogir tablica
    elif selectedWebsite == 'vrtic-trogir.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # Gradski muzej Drniš tablica
    elif selectedWebsite == 'gradski-muzej-drnis.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # Gradska čistoća Drniš tablica
    elif selectedWebsite == 'gradskacistoca-drnis.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # Osnovna glazbena škola Krsto Odak tablica 
    elif selectedWebsite == 'ogsko.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #2d7d9a; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #2d7d9a; border: solid 1px #766f8e; color: #ffffff; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # JVP Drniš tablica
    elif selectedWebsite == 'jvp-drnis.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # Općina Biskupija tablica
    elif selectedWebsite == 'biskupija.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #666666; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # Komunalno Društvo Biskupija tablica
    elif selectedWebsite == 'komunalno-drustvo-biskupija.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # SS Ivana Meštrovića Drniš tablica 
    elif selectedWebsite == 'ss-ivana-mestrovica-drnis.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #895a78; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #e3bfd9; border: solid 1px #d6aaca; color: #333333; font-weight: normal; font-size: 11px; width: 70px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # LAG Krka tablica
    elif selectedWebsite == 'lag-krka.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 35px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td colspan=" + '"' + ("4") + '"' + ">\n")
        tempFile.writelines("<h3 class=" + '"' + "uk-h4 uk-heading-bullet" + '"'  + ">" + "Dokumenti za preuzimanje" + "</h3>\n")
        tempFile.writelines("</td>\n")
        tempFile.writelines("</tr>\n")

    # Pučko otvoreno učilište tablica 
    elif selectedWebsite == 'pucko-otvoreno-uciliste-drnis.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #2a506d; font-weight: normal; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("5") + '"' + ">" + "PRILOŽENI DOKUMENTI:" + "</td>\n")
        tempFile.writelines("</tr>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px; width: 30px; margin: 0px 3px 3px 0px;" + '"' + ">" + "Br." + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px;" + '"' + ">" + "Opis datoteke" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px; width: 40px;" + '"' + ">" + "Tip" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px; width: 70px;" + '"' + ">" + "Veličina" + "</td>\n")
        tempFile.writelines("<td style=" + '"' + "background-color: #f9f9f9; border: solid 1px #cccccc; color: #2a506d; font-weight: bold; font-size: 11px; width: 70px;" + '"' + ">" + "Preuzimanje" + "</td>\n")
        tempFile.writelines("</tr>\n")


    # Žena Drniš tablica
    elif selectedWebsite == 'zena-drnis.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")

    # Ljekarna Drniš tablica
    elif selectedWebsite == 'ljekarna-drnis.hr':
        tempFile.writelines("<table style=" + '"' + "text-align: center; width: 100%; margin-bottom: 10px;" + '"' + ">\n")
        tempFile.writelines("<tbody>\n")
        tempFile.writelines("<tr>\n")
        tempFile.writelines("<td style=" + '"' + "text-align: left; color: #444; font-weight: bold; font-size: 12px;" + '"' + " " + "colspan=" + '"' + ("4") + '"' + ">" + "DOKUMENTI ZA PREUZIMANJE:" + "</td>\n")
        tempFile.writelines("</tr>\n")

    filesLocation = "images/" + categoryName + "/" + str(year) + "/" + folder # Location of the files

    index = 0
    tempIndex = 0

    #Going through all files in the folder and converting them to PDF if needed
    for every_file in files:
        filename = os.path.splitext(every_file)[0]

        if every_file.endswith(".xlsx") or every_file.endswith(".zip") or every_file.endswith(".rar") or every_file.endswith(".xls") or every_file.endswith(".csv") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods") or every_file.endswith(".odt") or every_file.endswith(".rtf"):

            if index - tempIndex == 1:
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

    #Going through all file in the folder and renaming them
    for every_file in files:

        filename = os.path.splitext(every_file)[0]
        
        if every_file.endswith(".xlsx") or every_file.endswith(".zip") or every_file.endswith(".rar") or every_file.endswith(".xls") or every_file.endswith(".csv") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods") or every_file.endswith(".odt") or every_file.endswith(".rtf"):

            ext = os.path.splitext(every_file)[1]

            rename(filename) #Renaming the file

            filename = filename[0].upper() + filename[1:]
            
            if filename[-1] == "_":
                filename = filename[:-1]

            renamedFile = every_file.replace(every_file, filename + ext)
            os.rename(os.path.join(downloads, every_file), os.path.join(downloads, renamedFile))

            bits_size = os.path.getsize(os.path.join(downloads, renamedFile))
            
            kb_size = bits_size / 1024
            if kb_size > 1024:
                mb_size = round(kb_size / 1024, 1)
                velicina = str(mb_size) + " MB"
            else:  
                velicina = str(math.trunc(kb_size)) + " KB"


            name_of_the_file =  filename + ext #Name of the file

            naslov_dokumenta = input("Unesi naslov dokumenta " + '"' + name_of_the_file + '": ') #Asking the user for the name of the file

            #Writing the main body of the table

                #Djecji vrtić Drniš tablica
            if selectedWebsite == "djecji-vrtic-drnis.hr":
                if ext == ".rar" or ext == ".zip":
                    ekstenzija = "images/05_DOCUMENT_ICONS/rar.png"
                elif ext == ".pdf":
                    ekstenzija = "images/05_DOCUMENT_ICONS/pdf.png"
                elif ext== ".xlsx" or ext == ".xls":
                    ekstenzija = "images/05_DOCUMENT_ICONS/xls.png"
                else:
                    ekstenzija = "images/05_DOCUMENT_ICONS/doc.png"

                privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #bbbbbb;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + ">" + "<img src=" + '"' + "images/05_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "border=" + '"' + "0" + '"' + "/></a></td>\n"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #bbbbbb;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #bbbbbb;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #bbbbbb;" + '"' + ">" + naslov_dokumenta + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #bbbbbb;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines(privitak_poveznica)
                tempFile.writelines("</tr>\n")

            elif selectedWebsite == "drnis.hr":
                ext_upper = ext.upper()[1:]

                privitak_poveznica = "<td class=" + '"' + "privitak_td_poveznica" + '"' + "><a class=" + '"' + "privitak_a" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + " rel=" + '"' + "noopener noreferrer" + '"' + ">" + str(naslov_dokumenta) +  "</a></td>\n"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td class=" + '"' + "privitak_td_redni_broj" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines(privitak_poveznica)
                tempFile.writelines("<td class=" + '"' + "privitak_td_tip_dokumenta" + '"' + ">" + ext_upper + "</td>\n")
                tempFile.writelines("<td class=" + '"' + "privitak_td_velicina" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("</tr>\n")

            elif selectedWebsite == "promina.hr":
                ekstenzija = ""

                if ext == ".rar" or ext == ".zip":
                    ekstenzija = "images/11_IKONE_DOKUMENATA/rar.png"
                elif ext == ".pdf":
                    ekstenzija = "images/11_IKONE_DOKUMENATA/pdf.png"
                elif ext== ".xlsx" or ext == ".xls":
                    ekstenzija = "images/11_IKONE_DOKUMENATA/xls.png"
                else:
                    ekstenzija = "images/11_IKONE_DOKUMENATA/doc.png"

                privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #bbbbbb;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + " rel=" + '"' + "noopener noreferrer" + '"' + ">" + "<img src=" + '"' + "images/11_IKONE_DOKUMENATA/download.png" + '"' +  " alt=" + '"' + '"' + " /></a></td>\n"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #bbbbbb;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #bbbbbb;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #bbbbbb;" + '"' + ">" + naslov_dokumenta + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #bbbbbb;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines(privitak_poveznica)
                tempFile.writelines("</tr>\n")

            #Kalun tablica
            elif selectedWebsite == "kalun.hr":
                if ext == ".rar" or ext == ".zip":
                    ekstenzija = "images/06_DOCUMENT_ICONS/rar.png"
                elif ext == ".pdf":
                    ekstenzija = "images/06_DOCUMENT_ICONS/pdf.png"
                elif ext== ".xlsx" or ext == ".xls":
                    ekstenzija = "images/06_DOCUMENT_ICONS/xls.png"
                else:
                    ekstenzija = "images/06_DOCUMENT_ICONS/doc.png"

                privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #ebebeb; padding: 2px 5px 2px 5px;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">" + "<img src=" + '"' + "images/06_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "/></a></td>\n"

                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #ebebeb; padding: 2px 5px 2px 5px; background-color: #ffffff;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #ebebeb; padding: 2px 5px 2px 5px; background-color: #ffffff;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 2px 5px 2px 5px; border: solid 1px #ebebeb; background-color: #ffffff;" + '"' + ">" + naslov_dokumenta + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #ebebeb; padding: 2px 5px 2px 5px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines(privitak_poveznica)
                tempFile.writelines("</tr>\n")

            # Vrtic Trogir tablica
            elif selectedWebsite == "vrtic-trogir.hr":
                ext_upper = ext.upper()[1:]

                privitak_poveznica = "<a style=" + '"' + "color: #de5543; font-weight: 500; font-style: normal; text-transform: uppercase; letter-spacing: 1px; text-decoration: none;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #fff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
                tempFile.writelines("</tr>\n")

            # Gradski muzej Drniš tablica
            elif selectedWebsite == "gradski-muzej-drnis.hr":
                ext_upper = ext.upper()[1:]

                privitak_poveznica = "<a style=" + '"' + "color: #c81342; font-family: 'Raleway', Helvetica, Arial, sans-serif; font-weight: 500; font-style: normal; text-transform: uppercase; letter-spacing: 1px; text-decoration: none;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #fff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
                tempFile.writelines("</tr>\n")

            # Gradska čistoća Drniš tablica
            elif selectedWebsite == "gradskacistoca-drnis.hr":
                ext_upper = ext.upper()[1:]

                privitak_poveznica = "<a style=" + '"' + "color: #39b54a; text-decoration: none;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"

                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #fff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #fff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
                tempFile.writelines("</tr>\n")

            # Osnovna glazbena škola Krsto Odak tablica
            elif selectedWebsite == "ogsko.hr":
                if ext == ".rar" or ext == ".zip":
                    ekstenzija = "images/01_SLIKE/03_DOCUMENT_ICONS/rar.png"
                elif ext == ".pdf":
                    ekstenzija = "images/01_SLIKE/03_DOCUMENT_ICONS/pdf.png"
                elif ext== ".xlsx" or ext == ".xls":
                    ekstenzija = "images/01_SLIKE/03_DOCUMENT_ICONS/xls.png"
                else:
                    ekstenzija = "images/01_SLIKE/03_DOCUMENT_ICONS/doc.png"

                privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + ">" + "<img src=" + '"' + "images/01_SLIKE/03_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "/></a></td>\n"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + naslov_dokumenta + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines(privitak_poveznica)
                tempFile.writelines("</tr>\n")

            # JVP Drniš tablica
            elif selectedWebsite == "jvp-drnis.hr":
                if ext == ".rar" or ext == ".zip":
                    ekstenzija = "images/01_slike/04_document_icons/rar.png"
                elif ext == ".pdf":
                    ekstenzija = "images/01_slike/04_document_icons/pdf.png"
                elif ext== ".xlsx" or ext == ".xls":
                    ekstenzija = "images/01_slike/04_document_icons/xls.png"
                else:
                    ekstenzija = "images/01_slike/04_document_icons/doc.png"

                privitak_poveznica = "<a href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + "/></td>\n")
                tempFile.writelines("</tr>\n")

            # Općina Biskupija tablica
            elif selectedWebsite == "biskupija.hr":
                ext_upper = ext.upper()[1:]

                privitak_poveznica = "<a style=" + '"' + "color: #d40e08; text-decoration: none;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
                tempFile.writelines("</tr>\n")

            # Komunalno društvo Biskupija tablica
            elif selectedWebsite == "komunalno-drustvo-biskupija.hr":
                ext_upper = ext.upper()[1:]

                privitak_poveznica = "<a style=" + '"' + "color: #078d39; text-decoration: none; font-weight: bold;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
                tempFile.writelines("</tr>\n")

            # SS Ivana Meštrovića Drniš tablica
            elif selectedWebsite == "ss-ivana-mestrovica-drnis.hr":
                if ext == ".rar" or ext == ".zip":
                    ekstenzija = "images/04_DOCUMENT_ICONS/rar.png"
                elif ext == ".pdf":
                    ekstenzija = "images/04_DOCUMENT_ICONS/pdf.png"
                elif ext== ".xlsx" or ext == ".xls":
                    ekstenzija = "images/04_DOCUMENT_ICONS/xls.png"
                else:
                    ekstenzija = "images/04_DOCUMENT_ICONS/doc.png"

                privitak_poveznica = "<td style=" + '"' + "text-align: center; background-color: #f7eff5; border: solid 1px #d6aaca; color: #333333;" + '"' + "><a style=" + '"' + "font-size: 14px; font-weight: bold;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + ">" + "<img src=" + '"' + "images/04_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "/></a></td>\n"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #d6aaca; background-color: #f7eff5; color: #333333;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #d6aaca; background-color: #f7eff5; color: #333333;" + '"' + ">" +  "<img src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 5px 5px 5px 5px; border: solid 1px #d6aaca; background-color: #f7eff5; color: #333333;" + '"' + ">" + naslov_dokumenta + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #f7eff5; border: solid 1px #d6aaca; color: #333333;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines(privitak_poveznica)
                tempFile.writelines("</tr>\n")

            # LAG Krka tablica
            elif selectedWebsite == "lag-krka.hr":
                ext_upper = ext.upper()[1:]

                privitak_poveznica = "<a class=" + '"' "uk-h4 uk-heading" + '"' + "style=" + '"' + "color: #f9591e; font-weight: 400; line-height: 1.5;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #eee; background-color: #fff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td class=" + '"' + "uk-h4 uk-heading" + '"' + "style=" + '"' + "text-align: left; background-color: #fff; border: solid 1px #eee; vertical-align: middle; padding: 3px 5px 3px 5px;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #eee; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #fff; border: solid 1px #eee; color: #666666; width: 50px;" + '"' + ">" + ext_upper + "</td>\n")
                tempFile.writelines("</tr>\n")

            # SS Ivana Meštrovića Drniš tablica
            elif selectedWebsite == "pucko-otvoreno-uciliste-drnis.hr":
                if ext == ".rar" or ext == ".zip":
                    ekstenzija = "images/06_DOCUMENT_ICONS/rar.png"
                elif ext == ".pdf":
                    ekstenzija = "images/06_DOCUMENT_ICONS/pdf.png"
                elif ext== ".xlsx" or ext == ".xls":
                    ekstenzija = "images/06_DOCUMENT_ICONS/xls.png"
                else:
                    ekstenzija = "images/06_DOCUMENT_ICONS/doc.png"

                privitak_poveznica = "<td style=" + '"' + "text-align: center; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + "><a style=" + '"' + "color: #2a506d; font-weight: bold; font-size: 13px;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + ">" + "<img style=" + '"' + "border: solid 0px #fff;" + '"' +  "src=" + '"' + "images/06_DOCUMENT_ICONS/download.png" + '"' +  " alt=" + '"' + "/></a></td>\n"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 3px 3px 3px 6px; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + ">" + naslov_dokumenta + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + ">" +  "<img style=" + '"' "border: solid 0px #fff;" '"' + " src=" + '"' + ekstenzija + '"' + " alt=" + '"' + '" ' + "/></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #cccccc; background-color: #f9f9f9; color: #2a506d;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines(privitak_poveznica)
                tempFile.writelines("</tr>\n")

            # Žena Drniš tablica
            elif selectedWebsite == "zena-drnis.hr":
                ext_upper = ext.upper()[1:]

                privitak_poveznica = "<a style=" + '"' + "color: #e77918; text-decoration: none;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
                tempFile.writelines("</tr>\n")

            # Ljekarna Drniš tablica
            elif selectedWebsite == "ljekarna-drnis.hr":
                ext_upper = ext.upper()[1:]

                privitak_poveznica = "<a style=" + '"' + "color: #02813e; text-decoration: none;" + '"' + " href=" + '"' + (filesLocation) + '"'  + " target=" + '"' + "_blank" + '"' + "rel=" + '"' + "noopener noreferrer" + '"' + '"' + ">"
                tempFile.writelines("<tr>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #000; width: 40px;" + '"' + ">" + str(broj_datoteke) + "." + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: left; padding: 3px 5px 3px 5px; border: solid 1px #dddddd; background-color: #ffffff; color: #666666;" + '"' + ">" + privitak_poveznica + naslov_dokumenta + "</a></td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; background-color: #ffffff; border: solid 1px #dddddd; color: #666666; width: 80px;" + '"' + ">" + velicina + "</td>\n")
                tempFile.writelines("<td style=" + '"' + "text-align: center; border: solid 1px #dddddd; background-color: #ffffff; color: #666666; width: 50px; vertical-align: middle;" + '"' + ">" + ext_upper + "</td>\n")
                tempFile.writelines("</tr>\n")

            broj_datoteke = broj_datoteke + 1

    tempFile.writelines("</tbody>\n")
    tempFile.writelines("</table>\n")

    word.Quit() #Closing the Word application

    tableExist = True

    return tableExist