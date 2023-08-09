import os
import math
import win32com.client

from rename import rename #Importing the function from rename.py

word = win32com.client.Dispatch('Word.Application')

def manipulateFiles(files, downloads, selectedWebsite):
    filesExist = False


    if (len(files) == 0):
        return filesExist

    broj_datoteke = 1

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
        else:
            files.remove(every_file)

        index = index + 1
        tempIndex = tempIndex + 1

    #Going through all file in the folder and renaming them
    for every_file in files:

        filename = os.path.splitext(every_file)[0]

        ext = os.path.splitext(every_file)[1]

        filename = rename(filename) #Renaming the file

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

        index = files.index(every_file)

        files.remove(every_file)


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
        elif uppercased_filename.split("_")[-1] == "POZIV":
            naslov_dokumenta == "POZIV - DNEVNI RED"
        elif uppercased_filename.split("_")[-1] == "ZAPISNIK":
            naslov_dokumenta == "ZAPISNIK"
            
        #drnis.hr file names
        elif uppercased_filename.split("_")[-1] == "AKTI" and selectedWebsite == "drnis.hr":
            naslov_dokumenta == "AKTI"

        #promina.hr file names
        elif uppercased_filename.split("_")[-1] == "AKATA" and selectedWebsite == "promina.hr":
            naslov_dokumenta == "USVOJENI AKTI"
        elif uppercased_filename.split("_")[-1] == "AKATA" and selectedWebsite == "promina.hr":
            naslov_dokumenta == "PRIJEDLOZI AKATA"
        
        else:
            naslov_dokumenta = input("Unesi naslov dokumenta " + '"' + name_of_the_file + '": ')

        files.insert(index, {"fileName": name_of_the_file, "fileSize": velicina, "kbSize": math.ceil(kb_size), "fileLocation": "", "fileTitle": naslov_dokumenta, "fileNumber": broj_datoteke, "ext": ext})

        broj_datoteke = broj_datoteke + 1

    word.Quit() #Closing the Word application

    filesExist = True

    return filesExist