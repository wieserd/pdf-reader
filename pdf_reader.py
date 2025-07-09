import PyPDF2
import sys

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    """
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
            return text
    except FileNotFoundError:
        return f"Error: File not found at {pdf_path}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_reader.py <path_to_pdf_file>")
    else:
        pdf_file_path = sys.argv[1]
        extracted_text = extract_text_from_pdf(pdf_file_path)
        print(extracted_text)
