# provide the file names as command line arguments

from PyPDF2 import  PdfFileReader
import sys

try:
    pdf = PdfFileReader(sys.argv[1])

    with open('text.txt', mode='w') as output_file:
        text = ''
        for page in pdf.pages:
            text += page.extractText()
        output_file.write(text)
        print(text)

except:
    print('Invalid file name!')
















'''
# creating a pdf file object
pdfFileObject = open(sys.argv[1], 'rb')


# creating a pdf reader object
pdfReader = PdfFileReader(pdfFileObject)

text=''
for i in range(0,pdfReader.numPages):
    # creating a page object
    pageObj = pdfReader.getPage(i)
    # extracting text from page
    text+=pageObj.extractText()

    file1 = open("extracted_text.txt","w")#write mode
    file1.write(text + "\n")
    file1.close()

print(text)



'''



'''
text=''
for i in range(0,pdfReader.numPages):
    # creating a page object
    pageObj = pdfReader.getPage(i)
    # extracting text from page
    text+=pageObj.extractText()
print(text)

'''