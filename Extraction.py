import csv
from ebooklib import epub
import os 
import PyPDF2

# El programa importa informacion de pdfs y epubs en una carpeta(puede tener mas carpetas dentro).

#Extracting metadata from epub files

pdf_count = 0
epub_count = 0
other_files = 0

def extraction_epub(epub_path):
    

    book = epub.read_epub(epub_path)
    title  = book.get_metadata("DC", 'title')
    author = book.get_metadata("DC", 'creator')
    date = book.get_metadata("DC", 'date')
    language = book.get_metadata("DC", 'language')

    return title, author, date, language

def extraction_pdf(pdf_path):
        
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        meta = pdf_reader.metadata

        return meta


def IfList(variable):

    if isinstance(variable, list) and len(variable) > 0 :

        variable = variable[0][0]
    
    return variable

def Nullification(a):

    if len(a) == 0:
        a = "Unknown"
    
    return a

def values_epub(file_path):
    size = os.path.getsize(file_path)
    size = (size / 1000000)
    title, author, date, language = extraction_epub(file_path)
    date = IfList(date)
    author = IfList(author)
    date = Nullification(date)
    author = Nullification(author)
    

    return title, author, date, language, size

path = r"C:\Users\carlo\Downloads\Libros"

with open('Book list.csv', 'w', newline='', encoding = 'latin1') as csvfile:

    write = csv.writer(csvfile)
    write.writerow(["Title", "Author", "Date", "Language", "Size (Mg)", "File"])

    for genero in os.listdir(path):

        path_folder = os.path.join(path, genero)

        if genero != "desktop.ini" :

            for filename in os.listdir(path_folder):

                file_path = os.path.join(path_folder, filename)

                if filename.endswith(".epub"):
                    epub_count += 1
                    title, author, date, language, size = values_epub(file_path)
                    try:
                        write.writerow([IfList(title), author, date[:10] , IfList(language), size, "epub"])
                    except:
                        write.writerow(["Written in another alphabet", "Error", "Error", "Error", "Error", "Error"])
                

                if filename.endswith(".pdf"):
                    pdf_count += 1
                    meta = extraction_pdf(file_path)

                    try:
                        date = meta.creation_date
                    except:
                        date = "unknown"

                    try:
                        title = meta.title
                    except:
                        title = filename

                    if not title : title = filename

                    try:
                        author = meta.author
                    except:
                        author = "Unknown"
                    
                    if not author : author = "Unavailable"
                    
                    size_pdf = os.path.getsize(file_path)
                    size_pdf = size_pdf / 1000000

                    try:
                        write.writerow([title, author, date, "unavailable", size_pdf, "pdf"])
                    except:
                        write.writerow(["Written in another alphabet", "Error", "Error", "Error", "Error", "Error"])
                
                else: 
                    other_files += 1
            

print(" \n" + "PDFs = "+ str(pdf_count) + "\nEPUBs = " + str(epub_count) + "\nOther files: " + str(other_files))
