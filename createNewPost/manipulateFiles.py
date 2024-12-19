import os
import math
import win32com.client
import PyPDF2

from rename import rename #Importing the function from rename.py

word = win32com.client.Dispatch('Word.Application')

def manipulateFiles(files, downloads, selectedWebsite, categoryName, postTitle):
    filesExist = False


    if (len(files) == 0):
        return filesExist

    broj_datoteke = 1

    index = 0
    tempIndex = 0
    
    #Going through all files in the folder and converting them to PDF if needed
    for file in files:
        filename = os.path.splitext(file)[0]

        ext = os.path.splitext(file)[1]

        if file.endswith(".xlsx") or file.endswith(".zip") or file.endswith(".rar") or file.endswith(".xls") or file.endswith(".csv") or file.endswith(".docx") or file.endswith(".pdf") or file.endswith(".doc") or file.endswith(".ods") or file.endswith(".odt") or file.endswith(".rtf"):

            if index - tempIndex == 1:
                tempIndex = tempIndex + 1
                continue

            if ext == ".pdf" or ext == ".zip" or ext == "rar":
                index = index + 1
                tempIndex = tempIndex + 1
                continue

            #User inputs the operation for the file
            operation = input("Unesi naredbu za datoteku " + '"' + file + '"' + " o/p/d: ")
                
            if operation == "p" or operation == "P":
                print("Prebacujem datoteku u PDF format...")
                doc = word.Documents.Open(os.path.join(downloads, file))
                pdfname = filename + ".pdf"
                doc.SaveAs(os.path.join(downloads, pdfname), FileFormat=17)
                doc.Close()
                os.remove(os.path.join(downloads, file))   
                files.remove(file) 
                files.insert(index, pdfname)

            elif operation == "d" or operation == "D":
                print("Prebacujem datoteku " + '"' + file + '"' + " u PDF i WORD format...")
                doc = word.Documents.Open(os.path.join(downloads, file))
                pdfname = filename + ".pdf"
                doc.SaveAs(os.path.join(downloads, pdfname), FileFormat=17)
                doc.Close()
                files.insert(index + 1, pdfname)
                index = index + 1
        else:
            files.remove(file)

        index = index + 1
        tempIndex = tempIndex + 1

    #rotating PDF and removing empty PDF pages

    for file in files:
        filename = os.path.splitext(file)[0]
        
        ext = os.path.splitext(file)[1]

        if file.endswith(".pdf"):
            editedPDFIndex = files.index(file)

            file1 = open(os.path.join(downloads, file), 'rb')
            ReadPDF = PyPDF2.PdfReader(file1)

            #Num of pages initially
            pages = len(ReadPDF.pages)

            #Creating new file which does not contain any empty pages
            output = PyPDF2.PdfWriter()
            file2 = open(os.path.join(downloads, filename + "_" + ".pdf"), "wb")
            files[editedPDFIndex] = filename + "_" + ".pdf"

            ReadPDF = PyPDF2.PdfReader(file1)

            noWhiteSpaceText = "".join(ReadPDF.pages[0].extract_text().split())

            if len(noWhiteSpaceText) == 0:
                print("Dokument " + "'" + file + "'" + " sadrzi skenirane dokumente. Provjerite ga da budete sigurni da je sve u redu")

                file2.close()
                file1.close()

                os.remove(os.path.join(downloads, filename + "_" + ".pdf"))
                files[editedPDFIndex] = filename + ".pdf"
                continue
            
            for i in range(pages):
                
                pageObj = ReadPDF.pages[i]
                #getting the page orientation
                pageOrientation = ReadPDF.pages[i].get('/Rotate')
                
                #rotating page to make it correct
                if pageOrientation:
                    pageObj.rotate(-pageOrientation)

                #getting page text
                text = pageObj.extract_text()
                
                noWhiteSpaceTxt = "".join(text.split())

                if len(noWhiteSpaceTxt) < 130:
                    action = input("Stranica " + str(i + 1) +  " PDF datoteke: " + file + " je kraća od 130 znakova. Zelite li ukloniti tu stranicu? d/n: ")

                    if action == "d" or action == "D":
                        continue
                    else:
                        output.add_page(pageObj)
                
                else:
                    output.add_page(pageObj)

            output.write(file2)
            file2.close()
            file1.close()

            os.remove(os.path.join(downloads, file))

    #Going through all file in the folder and renaming them
    for file in files:

        filename = os.path.splitext(file)[0]

        ext = os.path.splitext(file)[1]

        filename = rename(filename) #Renaming the file

        filename = filename[0].upper() + filename[1:]
        
        if filename[-1] == "_":
            filename = filename[:-1]

        renamedFile = file.replace(file, filename + ext)
        os.rename(os.path.join(downloads, file), os.path.join(downloads, renamedFile))

        bits_size = os.path.getsize(os.path.join(downloads, renamedFile))
       
        kb_size = bits_size / 1024

        if kb_size > 1024:
            mb_size = round(kb_size / 1024, 1)
            if mb_size.is_integer():
                mb_size = round(mb_size)
            velicina = str(mb_size) + " MB"
        else:  
            velicina = str(math.trunc(kb_size)) + " KB"

        velicina = velicina.replace(".", ",")

        name_of_the_file = renamedFile #Name of the file

        index = files.index(file)

        files.remove(file)


        naslov_dokumenta = "" #Asking the user for the name of the file
        default_value = ""

        uppercased_filename = filename.upper()

        #Universal names
        if uppercased_filename == "POZIV_NA_DOSTAVU_PONUDA":
            naslov_dokumenta = "POZIV NA DOSTAVU PONUDA"
        elif uppercased_filename == "TROSKOVNIK" or uppercased_filename == "PRILOG_2_TROSKOVNIK":
            naslov_dokumenta = "TROŠKOVNIK"
        elif uppercased_filename == "PONUDBENI_LIST" or uppercased_filename == "PRILOG_1_PONUDBENI_LIST":
            naslov_dokumenta = "PONUDBENI LIST"
        elif uppercased_filename.split("_")[-1] == "NEKAZNJAVANJU" and uppercased_filename.split("_")[-2] == "O" and uppercased_filename.split("_")[-3] == "IZJAVA":
            naslov_dokumenta = "IZJAVA O NEKAŽNJAVANJU"
        elif uppercased_filename == "ODLUKA_O_ODABIRU":
            naslov_dokumenta = "ODLUKA O ODABIRU"
        elif uppercased_filename == "ODLUKA_O_PONISTENJU":
            naslov_dokumenta = "ODLUKA O PONIŠTENJU"
        elif uppercased_filename.split("_")[-1] == "ZAPISNIK":
            naslov_dokumenta = "ZAPISNIK"
        elif uppercased_filename == "DODATAK_PONUDBENOM_LISTU_1_A":
            naslov_dokumenta = "DODATAK PONUDBENOM LISTU U SLUČAJU ZAJEDNICE PONUDITELJA"
        elif uppercased_filename == "DODATAK_PONUDBENOM_LISTU_1_b":
            naslov_dokumenta = "DODATAK PONUDBENOM LISTU U SLUČAJU PODUGOVARATELJA"

        #biskupija.hr file names
        if selectedWebsite == "biskupija.hr" and len(uppercased_filename.split("_")) > 1:
            
            if uppercased_filename.split("_")[-1] == "POZIV" and uppercased_filename.split("_")[-2] == "OV":
                naslov_dokumenta = "POZIV - DNEVNI RED"
            elif uppercased_filename.split("_")[-1] == "AKTI":
                naslov_dokumenta = "AKTI"
        
        #drnis.hr file names
        elif selectedWebsite == "drnis.hr":
            if uppercased_filename.split("_")[-1] == "AKTI":
                naslov_dokumenta = "AKTI"
            elif uppercased_filename.split("_")[-1] == "RED" and uppercased_filename.split("_")[-2] == "DNEVNI":
                naslov_dokumenta = "DNEVNI RED"
            elif uppercased_filename == "DODATAK_PONUDBENOM_LISTU_1A" or uppercased_filename == "DODATAK_PONUDBENOM_LISTU_1":
                naslov_dokumenta = "DODATAK PONUDBENOM LISTU U SLUČAJU ZAJEDNICE PONUDITELJA"
            elif uppercased_filename == "DODATAK_PONUDBENOM_LISTU_1B" or uppercased_filename == "DODATAK_PONUDBENOM_LISTU_2":
                naslov_dokumenta = "DODATAK PONUDBENOM LISTU U SLUČAJU PODUGOVARATELJA"
            elif "Izvješće o provedenom javnom savjetovanju" in postTitle:
                naslov_dokumenta = "IZVJEŠĆE"

        #eko-promina.hr file names
        elif selectedWebsite == "eko-promina.hr":
            if uppercased_filename == "OGLAS" and "Oglas za dodjelu grobnog mjesta na korištenje" in postTitle:
                naslov_dokumenta = "OGLAS"
            elif uppercased_filename.split("_")[0] == "PROSTORNI" and "Oglas za dodjelu grobnog mjesta na korištenje" in postTitle:
                naslov_dokumenta = "PROSTORNI PLAN GROBLJA S OZNAČENIM MJESTIMA ZA PRODAJU"

        #promina.hr file names  
        elif selectedWebsite == "promina.hr":
            if uppercased_filename.split("_")[-1] == "AKTI":
                naslov_dokumenta = "USVOJENI AKTI"
            elif uppercased_filename.split("_")[-1] == "AKATA":
                naslov_dokumenta = "PRIJEDLOZI AKATA"
            elif uppercased_filename == "TROSKOVNIK_S_POJASNJENJIMA":
                naslov_dokumenta = "TROŠKOVNIK S POJAŠNJENJIMA"
            elif uppercased_filename.split("_")[-1] == "RED" and uppercased_filename.split("_")[-2] == "DNEVNI":
                naslov_dokumenta = "DNEVNI RED"
            elif uppercased_filename == "OBAVIJEST_KANDIDATIMA_UZ_NATJECAJ":
                naslov_dokumenta = "OBAVIJEST KANDIDATIMA UZ NATJEČAJ"
            elif uppercased_filename.count("ZAKLJUCAK") and categoryName == "08_OBJAVE_NACELNIKA":
                default_value = "ZAKLJUČAK"
            elif uppercased_filename.count("JAVNI_NATJECAJ"):
                default_value = "JAVNI NATJEČAJ"
        

        #ss-ivana-mestrovica-drnis.hr file names
        if selectedWebsite == "ss-ivana-mestrovica-drnis.hr":
            if "Rang lista" in postTitle:
                naslov_dokumenta = "RANG LISTA"
            elif "Odluka o izboru kandidata" in postTitle:
                naslov_dokumenta = "ODLUKA O IZBORU KANDIDATA"
        
        if (default_value != ""):
            naslov_dokumenta = input("Unesi naslov dokumenta " + '"' + name_of_the_file + '" ' + f"(default: {default_value}): ") or default_value
        elif (naslov_dokumenta == ""):
            naslov_dokumenta = input("Unesi naslov dokumenta " + '"' + name_of_the_file + '": ')

        files.insert(index, {"fileName": name_of_the_file, "fileSize": velicina, "kbSize": math.ceil(kb_size), "fileLocation": "", "fileTitle": naslov_dokumenta, "fileNumber": broj_datoteke, "ext": ext})

        broj_datoteke = broj_datoteke + 1

    word.Quit() #Closing the Word application

    filesExist = True

    return filesExist