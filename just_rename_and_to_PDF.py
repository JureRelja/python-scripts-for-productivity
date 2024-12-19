import os
import math
import win32com.client
import subprocess
from pathlib import Path
import PyPDF2

downloads = str(Path.home() / "Downloads")
txtFile = open(downloads + "\Objava.txt","w+")
filename = ""
word = win32com.client.Dispatch('Word.Application')


for every_file in os.listdir(downloads):

    filename = os.path.splitext(every_file)[0]

    if every_file.endswith(".docx")or every_file.endswith(".doc") or every_file.endswith(".DOC") or every_file.endswith(".odt") or every_file.endswith(".rtf") or every_file.endswith(".csv"):
            
        doc = word.Documents.Open(os.path.join(downloads, every_file))
        pdfname = filename + ".pdf"
        doc.SaveAs(os.path.join(downloads, pdfname), FileFormat=17)
        doc.Close()

#rotating PDF and removing empty PDF pages
for every_file in os.listdir(downloads):
    filename = os.path.splitext(every_file)[0]

    ext = os.path.splitext(every_file)[1]

    if every_file.endswith(".pdf"):
        editedPDFIndex = os.listdir(downloads).index(every_file)

        file1 = open(os.path.join(downloads, every_file), 'rb')
        ReadPDF = PyPDF2.PdfReader(file1)

        #Num of pages initially
        pages = len(ReadPDF.pages)

        #Creating new file which do not conatin any empty pages
        output = PyPDF2.PdfWriter()
        file2 = open(os.path.join(downloads, filename + "_" + ".pdf"), "wb")
        os.listdir(downloads)[editedPDFIndex] = filename + "_" + ".pdf"
        
        for i in range(pages):
            ReadPDF = PyPDF2.PdfReader(file1)
            pageObj = ReadPDF.pages[i]
            #getting the page orientation
            pageOrientation = ReadPDF.pages[i].get('/Rotate')
            
            #rotating page to make it correct
            if pageOrientation:
                pageObj.rotate(-pageOrientation)
            print(pageOrientation)

            #getting page text
            # text = pageObj.extract_text()
            # noWhiteSpaceTxt = "".join(text.split())

            # if len(noWhiteSpaceTxt) <= 5:
            #     continues

            # elif len(noWhiteSpaceTxt) < 50:
            #     action = input("Stranica " + str(i + 1) +  " PDF datoteke: " + every_file + " je kraća od 50 znakova. Je li ta stranica potrebna? d/n: ")

            #     if action == "d" or action == "D":
            #         output.add_page(pageObj)
            #     elif action == "n" or action == "N":
            #         continue
            
            # else:
            output.add_page(pageObj)

        output.write(file2)
        file2.close()
        file1.close()

        os.remove(os.path.join(downloads, every_file))
        
for every_file in os.listdir(downloads):

    filename = os.path.splitext(every_file)[0]


    
    if every_file.endswith(".xlsx") or every_file.endswith(".csv") or every_file.endswith(".docx") or every_file.endswith(".pdf") or every_file.endswith(".doc") or every_file.endswith(".ods") or every_file.endswith(".odt") or every_file.endswith(".rtf"):


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
        filename = filename.replace("!", "_")
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
        
        txtFile.write("/" + filename + ext + "\n")

        txtFile.write(ext.upper()[1:] + "\n") 
        
        kb_size = bits_size / 1024
        if kb_size > 1024:
            mb_size = round(kb_size / 1024, 1)
            txtFile.write(str(mb_size) + " MB" + "\n"*4)
        else:  
            txtFile.write(str(math.trunc(kb_size)) + " KB" + "\n"*4)
            
txtFile.close()

subprocess.call(['cmd.exe', '/c', downloads + '\Objava.txt'])
word.Quit()
