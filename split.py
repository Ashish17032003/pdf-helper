# provide the file name as command line arguments
# Zero indexed pages 


import PyPDF2
import sys


"""
chapter1 = list (range(0,3))
chapter2 = [3, 4]
chapter3 = [5]

and create writers accordingly

"""

pages = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
print("Enter which page/pages you want to split : ")
# iterating till the range
for i in range(0, n):
    ele = int(input())  
    pages.append(ele) # adding the element
      
print(pages)

with open(sys.argv[1], "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()
    rest_writer = PyPDF2.PdfFileWriter()

    for page in range(len(reader.pages)):
        if page in pages:
            writer.addPage(reader.getPage(page))
        else:
            rest_writer.addPage(reader.getPage(page))


    with open("selected.pdf", "wb") as f2:
        writer.write(f2)

    with open("rest.pdf", "wb") as f2:
        rest_writer.write(f2) 