import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS

def getPdfText(pdfDocs):
    text = ""

    for pdf in pdfDocs:
        reader = PdfReader(pdf)

        for page in reader.pages:
            text += page.extract_text()

    return text

def getTextChunks(rawText):
    textSplitter = CharacterTextSplitter(separator = '\n', chunk_size = 1000, chunk_overlap = 200, length_function = len)

    chunks = textSplitter.split_text(rawText)

    return chunks

def getVectorstore(textChunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name = "hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts = textChunks, embedding = embeddings)

    return vectorstore

def main():
    load_dotenv()

    st.set_page_config(page_title = "Chat With Multiple PDFs", page_icon = ":books:")

    st.header("Chat With Multiple PDFs :books:")
    st.text_input("Ask a question about you document:")

    with st.sidebar:
        st.subheader("Your documents")
        pdfDocs = st.file_uploader("Upload your pdfs here:", accept_multiple_files = True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                rawText = getPdfText(pdfDocs)
                
                textChunks = getTextChunks(rawText)

                vectorstore = getVectorstore(textChunks)

if __name__ == "__main__":
    main()