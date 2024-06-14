import PyPDF2

# Function to create a password-protected PDF
def create_password_protected_pdf(filename, password):
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Add a page to the PDF
    pdf_writer.add_blank_page(width=612, height=792)
    

    # Write the PDF to a file
    with open(filename, 'wb') as f:
        pdf_writer.write(f)

    # Encrypt the PDF with the provided password
    pdf_reader = PyPDF2.PdfReader(filename)
    pdf_writer = PyPDF2.PdfWriter()

   
    # Use the correct argument 'user_password' instead of 'user_pwd'
    pdf_writer.encrypt(user_password=password, owner_password=None, use_128bit=True)

    with open(filename, 'wb') as f:
        pdf_writer.write(f)

# Function to crack the password based on the provided pattern
def crack_password(filename):
    # Define the pattern to generate passwords
    for day in range(1, 32):
        for month in range(1, 13):
            for year in range(1900, 2100):
                # Format the password as ddmmyyyy
                password = f"{day:02d}{month:02d}{year}"
                try:
                    # Attempt to open the PDF with the generated password
                    with open(filename, 'rb') as f:
                        pdf_reader = PyPDF2.PdfReader(f)
                        # Try to decrypt with the password
                        if pdf_reader.decrypt(password):
                            # If successful, print the password and return
                            print("Password found:", password)
                            return
                except Exception as e:
                    # Print error information for debugging
                    print(f"Failed attempt with password {password}: {e}")
                    continue

    print("Password not found")

# Create a password-protected PDF
create_password_protected_pdf("example.pdf", "29121983")

# Crack the password
crack_password("example.pdf")
 