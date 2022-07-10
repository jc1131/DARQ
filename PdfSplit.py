# Get Large Dollar Notice

# Developed By Jordan Crist | Updated 2021-09-14

 

# Import Modules

import os, PyPDF2, re, shutil, time

 

# Function to extract each page found in PDF

def split_pdf(extract_folder, split_file):

                opened_pdf = PyPDF2.PdfFileReader(open(split_file,"rb"))

                                # for each page in the pdf

                for i in range(opened_pdf.numPages):

                                # write the page to a new pdf

                output = PyPDF2.PdfFileWriter()

                output.addPage(opened_pdf.getPage(i))

                with open (extract_folder + "\\" + "Notice of Delayed Availability-%s.pdf" % i, "wb") as output_file:

                  output.write(output_file)

 

def rename_pdf(extract_folder, rename_folder):

                for root, dirs, files in os.walk(extract_folder):

                for filename in files:

                  basename, extension = os.path.splitext(filename)

                                # if a file is a pdf

                  if extension == ".pdf":

                                # create a reference to the full filename path

                   fullpath = root + "\\" + basename + extension

                # open the individual pdf

                   pdf_file_obj = open(fullpath, "rb")

                   pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

                # access the individual page

                   page_obj = pdf_reader.getPage(0)

                # extract the text

                   pdf_text = page_obj.extractText()

                #Find account holder name

                   timestr = time.strftime("%Y-%m-%d")

                   AccountName = re.compile('(Account Holder):\s*(.*)')

                   newFileName = AccountName.search(pdf_text).group(2)+"-"+timestr

                   shutil.copy(fullpath, rename_folder + "\\" + newFileName + ".pdf")

                   pdf_file_obj.close

 

# Parameter variables

split_file = r.pdf

extract_folder = r\\Extracted

rename_folder = r\\

 

#Check if file exists

while(True):

                modificationTime = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(split_file)))

                runTime = time.strftime("%Y-%m-%d")

                print("looping...", "File Date:", modificationTime, "Current Date:", runTime)

                time.sleep(2)

                if modificationTime == runTime:

                break

 

#Call Functions

split_pdf(extract_folder, split_file)

rename_pdf(extract_folder, rename_folder)
