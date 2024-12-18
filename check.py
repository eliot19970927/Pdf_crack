import PyPDF2
import multiprocessing

# Function to attempt unlocking the PDF
def try_password(password, pdf_path, output_path):
    print(f"Trying password: {password}")  # Print each password being tried
    try:
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            if pdf_reader.decrypt(password):
                # Save the unlocked PDF
                with open(output_path, "wb") as output_file:
                    pdf_writer = PyPDF2.PdfWriter()
                    for page_num in range(len(pdf_reader.pages)):
                        pdf_writer.add_page(pdf_reader.pages[page_num])
                    pdf_writer.write(output_file)
                return f"Success! The password is: {password}"
            return None
    except Exception:
        return None

# Function to unlock the PDF using multiprocessing
def unlock_pdf():
    pdf_path = "aaa.pdf"
    output_path = "unlocked.pdf"
    password_list_path = "passwords.txt"
    
    with open(password_list_path, "r") as file:
        passwords = file.read().splitlines()

    # Create a pool of worker processes
    pool = multiprocessing.Pool()
    results = pool.starmap(try_password, [(password, pdf_path, output_path) for password in passwords])
    
    for result in results:
        if result:
            print(result)
            break
    else:
        print("Failed to unlock the PDF.")

# Run the function
unlock_pdf()