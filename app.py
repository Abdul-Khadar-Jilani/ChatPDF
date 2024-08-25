import streamlit as st
from PyPDF2 import PdfReader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter

# Function to process the PDF
def process_pdf(pdf_file):
    pdfreader = PdfReader(pdf_file)
    raw_text = ''
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content
    return raw_text

# Streamlit app
def main():
    st.title("Chat with your PDF")
    
    # Prompt for OpenAI API key
    openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")
    
    if not openai_api_key:
        st.warning("Please enter your OpenAI API Key.")
        st.stop()

    # Upload PDF file
    pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])

    if pdf_file:
        raw_text = process_pdf(pdf_file)

        text_splitter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 800,
            chunk_overlap  = 200,
            length_function = len,
        )
        texts = text_splitter.split_text(raw_text)

        # Use the OpenAI API key
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

        document_search = FAISS.from_texts(texts, embeddings)

        # Question input
        query = st.text_input("Enter your question about the PDF:")

        if query:
            chain = load_qa_chain(OpenAI(openai_api_key=openai_api_key), chain_type="stuff")
            docs = document_search.similarity_search(query)
            answer = chain.run(input_documents=docs, question=query)
            
            st.write("**Answer:**", answer)

if __name__ == "__main__":
    main()
