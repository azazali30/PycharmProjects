import PyPDF2
import sys

file_list = sys.argv[1:]


def combiner(input_files):
    pdf_merger = PyPDF2.PdfFileMerger()
    for file in input_files:
        pdf_merger.append(file)
        print(file)
    pdf_merger.write("merged.pdf")


combiner(file_list)
