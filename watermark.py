import PyPDF2
import sys


try:
    template = PyPDF2.PdfFileReader(open(sys.argv[1],'rb'))
    watermark = PyPDF2.PdfFileReader(open(sys.argv[2],'rb'))

    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)

except:
    print("Invalid file name!")





"""

template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage())
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)

"""

