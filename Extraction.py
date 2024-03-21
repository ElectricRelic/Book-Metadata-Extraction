import csv
import ebooklib
from ebooklib import epub
import os 

#Extracting metadata from epub files

pdf_count = 0
epub_count = 0
other_files = 0

def extraction(path):
    

    book = epub.read_epub(path)
    title  = book.get_metadata("DC", 'title')
    author = book.get_metadata("DC", 'creator')
    date = book.get_metadata("DC", 'date')
    language = book.get_metadata("DC", 'language')

    return title, author, date, language

def IfList(variable):

    if isinstance(variable, list) and len(variable) > 0 :

        variable = variable[0][0]
    
    return variable

def Nullification(a):

    if len(a) == 0:
        a = "Unknown"
    
    return a

path = r"C:\Users\carlo\Downloads\Libros"

with open('Book list.csv', 'w', newline='', encoding = 'utf-8') as csvfile:

    write = csv.writer(csvfile)
    write.writerow(["Title", "Author", "Date", "Language", "Size (Mg)"])

    for genero in os.listdir(path):

        path_folder = os.path.join(path, genero)

        if genero != "desktop.ini" :

            for filename in os.listdir(path_folder):

                if filename.endswith(".epub"):
                    epub_count += 1
                    file_path = os.path.join(path_folder, filename)
                    size = os.path.getsize(file_path)
                    size = (size / 1000000)
                    title, author, date, language = extraction(file_path)
                    date = IfList(date)
                    author = IfList(author)
                    date = Nullification(date)
                    author = Nullification(author)
                    write.writerow([IfList(title), author, date[:10] , IfList(language), size])
                

                if filename.endswith(".pdf"):
                    pdf_count += 1
                
                else: 
                    other_files += 1

print(" \n" + "PDFs = "+ str(pdf_count) + "\nEPUBs = " + str(epub_count) + "\nOther files: " + str(other_files))