import PyPDF2
import threading

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
    pdf_writer.encrypt(user_password=password, owner_password=None, use_128bit=True)

    with open(filename, 'wb') as f:
        pdf_writer.write(f)

# Global variable to indicate if the password is found
password_found = False
found_password = None

# Lock for thread-safe operations on shared resources
lock = threading.Lock()

# Function to attempt to decrypt the PDF with a given password
def attempt_decrypt(filename, password):
    global password_found, found_password
    try:
        with open(filename, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)

            # Try to decrypt with the password
            if pdf_reader.decrypt(password):
                with lock:
                    password_found = True
                    found_password = password
                    print("Password found:", password)
                    return True
    except Exception as e:
        print(f"Failed attempt with password {password}: {e}")
    return False

# Worker function for each thread
def password_cracker_worker(filename, passwords):
    for password in passwords:
        if password_found:
            break
        attempt_decrypt(filename, password)

# Function to crack the password based on the provided pattern
def crack_password(filename):
    # Define the pattern to generate passwords
    def password_generator():
        for day in range(1, 32):
            for month in range(1, 13):
                for year in range(1900, 2100):
                    yield f"{day:02d}{month:02d}{year}"

    # Create a list of all possible passwords
    all_passwords = list(password_generator())

    # Split the passwords into chunks for each thread
    num_threads = 8
    chunk_size = len(all_passwords) // num_threads
    threads = []

    for i in range(num_threads):
       start = i * chunk_size
       end = (i + 1) * chunk_size
    if i != num_threads - 1:
        end = (i + 1) * chunk_size
    else:
        end = None
 
        thread = threading.Thread(target=password_cracker_worker, args=(filename, all_passwords[start:end]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if not password_found:
        print("Password not found")
    else:
        print(f"Password cracking completed. Found: {found_password}")

# Create a password-protected PDF
create_password_protected_pdf("example.pdf", "29121983")

# Crack the password
crack_password("example.pdf")
