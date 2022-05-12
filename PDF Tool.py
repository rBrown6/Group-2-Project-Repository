import PyPDF2
impot os
Path = 'C:/Users/jlaw/Desktop/Testing/'
folders = os.listdir(Path)
pdfMerger = PyPDF2.PdfFileMerger()
de pdf_merge(filelist): #Changed to just one argument
    pdfMerger = PyPDF2.PdfFileMerger()
    for file n os.listdir(filelist): #added os.listdir()
         if file.endswith('.pdf'):
                pdfMerger.append(filelist+'/'+file) #replaced Path+foldername with filelist
    pdfOutput = open(Path+folder+'/Tab C.pdf', 'wb' #Moved back one tab to prevent infinite loop
    pdfMerger.write(pdfOutput) 
    pdfOutput.close() 
for folder in folders:
    pdf_merge(Path+folder)` #Removed redundant + "/"
