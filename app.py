
import streamlit as st
from PyPDF2 import PdfReader
import os

def main():

    st.set_page_config(page_title="Chat with your files", page_icon="🧠")
    st.header("Chat with your files")

    # upload file
    pdf = st.file_uploader("Upload your file.", type=None, accept_multiple_files=True, key="uploader")


    #extract the text from the pdf
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        st.write(text)


if __name__=='__main__':
    main()