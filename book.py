import streamlit as st
import PyPDF2
from docx import Document

def pdf_to_text(pdf_file):
    # Initialize a PDF reader
    reader = PyPDF2.PdfReader(pdf_file)
    
    # Extract text from each page
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()

    return text

def save_to_word(text, output_filename):
    # Create a new Word Document
    doc = Document()
    
    # Add the extracted text
    doc.add_paragraph(text)
    
    # Save the document
    doc.save(output_filename)

# Streamlit App
st.title("PDF to Word Data Entry")

# File upload
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF
    text = pdf_to_text(uploaded_file)
    
    # Display extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text from PDF", text, height=300)

    # Download the extracted text as a Word document
    if st.button("Convert to Word"):
        output_filename = "output.docx"
        save_to_word(text, output_filename)
        with open(output_filename, "rb") as file:
            st.download_button(
                label="Download Word Document",
                data=file,
                file_name=output_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
