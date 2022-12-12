import PyPDF2

reader1 = PyPDF2.PdfFileReader(open('../pdf/merged.pdf', 'rb'))
wtr_reader = PyPDF2.PdfFileReader(open('../pdf/wtr.pdf', 'rb'))

writer = PyPDF2.PdfFileWriter()
for i in range(0, reader1.numPages):

    page = reader1.getPage(i)
    page.mergePage(wtr_reader.getPage(0))
    writer.addPage(page)
    with open('wtr_marked.pdf', 'wb') as file:
        writer.write(file)
