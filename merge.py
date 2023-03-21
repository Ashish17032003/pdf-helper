# provide the file names as command line arguments

import PyPDF2
import sys

try:
    inputs = sys.argv[1:]
    def pdf_combiner(pdf_list):
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            print(pdf)
            merger.append(pdf)
        merger.write('merged_output.pdf')

    pdf_combiner(inputs)

except FileNotFoundError:
    print("Invalid file name!")

except:
    print("Please try again!")