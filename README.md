Simple PDF Chatbot
This is a simple Streamlit web application that lets you chat with your PDF documents using Google's Gemini AI model.

🚀 How it Works
Upload PDFs: You upload one or more PDF files.

Process: The app extracts text, splits it into smaller parts, and creates a searchable database (vector store) from it using Google's embedding model.

Chat: You can then ask questions about your documents, and the Gemini AI will use the information from your PDFs and the conversation history to give you answers.

🛠️ Setup
Follow these steps to get the app running:

1. Get a Google AI API Key
Go to Google AI Studio and get your API key.

2. Prepare Your Project
Save the Python code: Save the provided Python code as app.py.

Create templates.py: Create a file named templates.py in the same folder as app.py and paste the CSS and HTML templates for chat messages into it (you provided these earlier).

3. Create a .env file
In the same folder as app.py, create a file named .env.

Add your Google AI API key inside this file like this:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Remember to replace YOUR_API_KEY_HERE with your actual key. Keep this file private!

4. Install Python Libraries
Open your terminal or command prompt.

(Optional but recommended) Create a virtual environment:

python -m venv venv
# On Windows: .\venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate

Install the required libraries:

pip install streamlit python-dotenv PyPDF2 langchain-community langchain-google-genai langchain nest_asyncio

▶️ How to Run
Make sure your virtual environment is active (if you created one).

In your terminal, navigate to the folder where you saved app.py.

Run the app:

streamlit run app.py

Your web browser should open automatically to the app (usually at http://localhost:8501).

💬 Using the App
Upload: Use the "Upload your pdfs here:" section in the sidebar to select your PDF files.

Process: Click the "Process" button. Wait for the "Processing" spinner to finish.

Ask: Type your questions in the text box at the top and press Enter. The AI will respond based on your documents and previous conversation.

Enjoy chatting with your PDFs!