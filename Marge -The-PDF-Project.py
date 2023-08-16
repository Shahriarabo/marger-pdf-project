from PyPDF2 import PdfMerger

AllPdf = ["PDF1.pdf","PDF2.pdf","car1.pdf","car2.pdf","car3.pdf","car4.pdf"]

Thispdf =  PdfMerger()

for newpdf in AllPdf:
    Thispdf.append(newpdf)
Thispdf.write("Raselpdf.pdf")
Thispdf.close()