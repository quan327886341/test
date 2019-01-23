import PyPDF2


# pdfFileObj = open('meetingminutes.pdf', 'rb')
# pdfFileObj = open('encrypted.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.isEncrypted)
# pdfReader.decrypt('rosebud')
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())


# pdf1File = open('meetingminutes.pdf', 'rb')
# pdf2File = open('meetingminutes2.pdf', 'rb')
# pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
# pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
# pdfWriter = PyPDF2.PdfFileWriter()
#
# for pageNum in range(pdf1Reader.numPages):
#     pageObj = pdf1Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
#
# for pageNum in range(pdf2Reader.numPages):
#     pageObj = pdf2Reader.getPage(pageNum)
#     if pageNum < 3:
#         pageObj.rotateClockwise(90)
#     pdfWriter.addPage(pageObj)
#
# pdfOutputFile = open('combinedminutes.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close()
# pdf1File.close()
# pdf2File.close()


minutesFile = open('meetingminutes.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdf1Reader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfWriter.encrypt('quan1984')
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
minutesFile.close()






























