# import PyPDF2

# def createfile(filename):

#     pdf_writer=PyPDF2.PdfWriter()

#     pdf_writer.add_blank_page(width=611,height=789)


# createfile("abcd.pdf")



import PyPDF2

def createfile(filename):
    pdf_writer = PyPDF2.PdfWriter()
    
    # Add a blank page
    pdf_writer.add_blank_page(width=611, height=789)
    
    # Write the PDF to a file
    with open(filename, 'wb') as f:
        pdf_writer.write(f)   

# Create the PDF file
createfile("abcd.pdf")
