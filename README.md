
# Chat with Your PDF

**Chat with Your PDF** is a Streamlit application that allows users to interact with PDF documents by asking questions about the content. The application uses OpenAI's language models to provide answers based on the text extracted from the PDF.

## Features

- **PDF Upload**: Easily upload your PDF documents to the application.
- **API Key Integration**: Securely enter your OpenAI API key to enable the functionality.
- **Question Answering**: Ask questions about the content of the PDF and get accurate answers.
- **Text Chunking**: Efficiently process large PDFs by splitting text into manageable chunks.

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.7 or higher
- An OpenAI API key (sign up at [OpenAI](https://openai.com) if you don’t have one)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/chat-with-pdf.git
   cd chat-with-pdf
2. **Create a Virtual Environment:**
   ```bash
    python -m venv venv
   ```
3. **Activate the Virtual Environment:**
   ```bash
   venv\\Scripts\\activate```
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
5. **Run the Application:**
   ```bash
   streamlit run app.py
This will start the Streamlit server and open the application in your default web browser.

## Usage

- Enter Your OpenAI API Key: When prompted, enter your OpenAI API key to authenticate the application.
- Upload a PDF: Click on the upload button to select and upload your PDF document.
- Ask Questions: Enter your questions in the provided input field.
- The application will process the PDF and provide answers based on its content.
