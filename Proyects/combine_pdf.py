import PyPDF2
import sys
import os

path = './pdfs'
pathOut = '/combinedpdf'
merger = PyPDF2.PdfFileMerger()
for file in os.listdir(path):
    if file.endswith('.pdf'):
        merger.append(file)
merger.write("namefile.pdf")   