import os

def rename(file):
    filename = file.replace("  ", " ")
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
    #filename = filename[0].upper() + filename[1:]
        
    if filename[-1] == "_":
        filename = filename[:-1]
        
    
    rename = file.replace(file, filename)
    
    return rename