import PyPDF2                           # importing the module                  


with open('lebo101.pdf','rb') as pdf_file_object:     # opening the file and representing it as a pdf_file_object and it is a file object 

    pdf_file_reader = PyPDF2.PdfReader(pdf_file_object)    # reading and opening the pdf file and it is a pdf file object


    no_of_pages=len( pdf_file_reader.pages)                 # to count the number of pages present in the pdf file
    
    print('no. of pages', no_of_pages)   


    first_page=pdf_file_reader.pages[3]                 # reading the first page of the pdf it will give the meta data
      
   # print(first_page.extract_text())                     # gives the exact data 

    print(first_page.images[0])                          # to get he data of the image 

    print(first_page.images[0].name)                      # using attribute to get the name of the image

    print(first_page.images[0].data)                       # by this we will get the meta data of the image  in bytes

    