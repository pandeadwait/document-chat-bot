import streamlit as st

def main():
    st.set_page_config(page_title = "Chat With Multiple PDFs", page_icon = ":books:")

    st.header("Chat With Multiple PDFs :books:")
    st.text_input("Ask a question about you document:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your pdfs here:")
        st.button("Process")


if __name__ == "__main__":
    main()