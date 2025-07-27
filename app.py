import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from templates import css, bot_template, user_template
import nest_asyncio

nest_asyncio.apply()

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
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(texts = textChunks, embedding = embeddings)

    return vectorstore

def getConversationChain(vectorstore):
    llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature = 0.3)
    memory = ConversationBufferMemory(memory_key = "chat_history", return_messages = True, input_key = "question")
    conversationChain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorstore.as_retriever(),
        memory = memory
    )

    return conversationChain

def handleQuestion(question):
    response = st.session_state.conversation({
        'question' : question,
        'chat_history': st.session_state.chatHistory
    })

    st.session_state.chatHistory = response['chat_history']

def main():
    load_dotenv()

    st.set_page_config(page_title = "Chat With Multiple PDFs", page_icon = ":books:")
    st.write(css, unsafe_allow_html = True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = []
    
    st.header("Chat With Multiple PDFs :books:")
    question = st.text_input("Ask a question about you document:")
    
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html = True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html = True)

    if question:
        handleQuestion(question)

    with st.sidebar:
        st.subheader("Your documents")
        pdfDocs = st.file_uploader("Upload your pdfs here:", accept_multiple_files = True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                rawText = getPdfText(pdfDocs)
                
                textChunks = getTextChunks(rawText)

                vectorstore = getVectorstore(textChunks)

                st.session_state.conversation = getConversationChain(vectorstore) 

if __name__ == "__main__":
    main()