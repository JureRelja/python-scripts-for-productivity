import os
import math
import win32com.client
import subprocess

downloads = "C:\\Users\jurer\Downloads"
txtFile = open(r"C:\Users\jurer\Desktop\NOVA OBJAVA.txt","w+")
filename = ""
word = win32com.client.Dispatch('Word.Application')


for every_file in os.listdir(downloads):

    filename = os.path.splitext(every_file)[0]

    if every_file.endswith(".doc") or every_file.endswith(".odt") or every_file.endswith(".rtf") or every_file.endswith(".csv"):
            
        doc = word.Documents.Open(os.path.join(downloads, every_file))
        pdfname = filename + ".docx"
        doc.SaveAs(os.path.join(downloads, pdfname), FileFormat=17)
        doc.Close()
        
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
        
        rename = every_file.replace(every_file, filename + ext)
        os.rename(os.path.join(downloads, every_file), os.path.join(downloads, rename))

        bits_size = os.path.getsize(os.path.join(downloads, rename))
        
        txtFile.write("/" + filename + ext + "\n") 
        
        kb_size = bits_size / 1024
        if kb_size > 1024:
            mb_size = round(kb_size / 1024, 1)
            txtFile.write(str(mb_size) + " MB" + "\n"*4)
        else:  
            txtFile.write(str(math.trunc(kb_size)) + " KB" + "\n"*4)
            
txtFile.close()

subprocess.call(['cmd.exe', '/c', r'C:\Users\jurer\Desktop\NOVA OBJAVA.txt'])
word.Quit()