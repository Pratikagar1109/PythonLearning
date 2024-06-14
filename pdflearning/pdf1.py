import PyPDF2                           # importing the module                  


with open('2206399_LAB1.pdf','rb') as pdf_file_object:     # opening the file and representing it as a pdf_file_object

    pdf_file_reader = PyPDF2.PdfReader(pdf_file_object)    # reading and opening the pdf file


    no_of_pages=len( pdf_file_reader.pages)                 # to count the number of pages present in the pdf file
    
    print('no. of pages', no_of_pages)   


    #  first_page=pdf_file_reader.pages[0]                      # reading the first page of the pdf
      
    for page in range(no_of_pages):                         # to read all the pages present in the pdf
     page=pdf_file_reader.pages[page]

     
     
     
   

    print(page.extract_text())                        # extracting the text data from the pdf file

   