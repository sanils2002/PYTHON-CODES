import PyPDF2

pdf1File = open('File1.pdf', 'rb')
pdf2File = open('File2.pdf', 'rb')
pdf3File = open('File3.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdf3Reader = PyPDF2.PdfFileReader(pdf3File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf3Reader.numPages):
    pageObj = pdf3Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('Merge File.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
pdf3File.close()
