import os

def rename(file):
    file = file.replace("  ", " ")
    file = file.replace("   ", " ")
    file = file.replace("    ", " ")
    file = file.replace("     ", " ")
    file = file.replace(" ", "_")
    file = file.replace(".", "_")
    file = file.replace("-", "_")
    file = file.replace("–", "_")
    file = file.replace(",", "_")
    file = file.replace(";", "_")
    file = file.replace(":", "_")
    file = file.replace("Č", "C")
    file = file.replace("č", "c")
    file = file.replace("Ć", "C")
    file = file.replace("ć", "c")
    file = file.replace("Đ", "D")
    file = file.replace("đ", "d")
    file = file.replace("Š", "S")
    file = file.replace("š", "s")
    file = file.replace("Ž", "Z")
    file = file.replace("ž", "z")
    file = file.replace("_–", "_")
    file = file.replace("__", "_")
    file = file.replace("__", "_")
    file = file.replace("___", "_")
    file = file.replace('"', "")
    file = file.replace("(", "")
    file = file.replace(")", "")
    file = file.replace("?", "")
    #file = file[0].upper() + file[1:]
        
    if file[-1] == "_":
        file = file[:-1]
        
    
    rename = file.replace(file, file)
    
    return rename