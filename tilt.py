# provide the file name as command line arguments
# One indexed pages 

import PyPDF2
import sys


try:
    with open(sys.argv[1], 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        pageno = int(input("Enter the page number that is to be rotated : "))

        if(pageno == 0):
            print("Page 0 doesn't exist! Try again")

        else:
            pageno -=  1
            try:
                page = reader.getPage(int(pageno)) 

                rotation = input("Press R to rotate Clockwise and A to rotate Counter-Clock Clockwise : ")
                if rotation == 'R':
                    degree = input("Enter the degree of rotation: ")
                    page.rotateClockwise(int(degree))
                    writer = PyPDF2.PdfFileWriter()
                    writer.addPage(page)
                    with open('tilt.pdf', 'wb') as new_file:
                        writer.write(new_file)

                elif rotation == 'A':
                    degree = input("Enter the degree of rotation")
                    page.rotateCounterClockwise(int(degree))
                    writer = PyPDF2.PdfFileWriter()
                    writer.addPage(page)
                    with open('tilt.pdf', 'wb') as new_file:
                        writer.write(new_file)

                else:
                    print("Invalid input")

            except AssertionError:
                print("Angle should be a multiple of 90")

            except:
                print("Page not found! Please Try again with a valid page number")

except:
    print("Invalid file name!")