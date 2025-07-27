# Simple PDF Chatbot

This is a simple Streamlit web application that lets you chat with your PDF documents using Google's Gemini AI model.

## 🚀 How it Works

1. **Upload PDFs:** You upload one or more PDF files.

2. **Process:** The app extracts text, splits it into smaller parts, and creates a searchable database (vector store) from it using Google's embedding model.

3. **Chat:** You can then ask questions about your documents, and the Gemini AI will use the information from your PDFs and the conversation history to give you answers.

## 🛠️ Setup

Follow these steps to get the app running:

### 1. Get a Google AI API Key

* Go to [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key) and get your API key.

### 2. Prepare Your Project

* **Save the Python code:** Save the provided Python code as `app.py`.

* **Create `templates.py`:** Create a file named `templates.py` in the same folder as `app.py` and paste the CSS and HTML templates for chat messages into it (you provided these earlier).

### 3. Create a `.env` file

* In the same folder as `app.py`, create a file named `.env`.

* Add your Google AI API key inside this file like this: