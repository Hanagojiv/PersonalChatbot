# 🤖 Knowledge Base Chatbot

Welcome to the Knowledge Base Chatbot 📚, a generative AI-driven application designed to facilitate efficient information retrieval from PDF documents via conversational interfaces. This application is deployed on Streamlit Cloud and can be accessed [here](https://personalchatbotgit-swtxqf6emsroewvi3ugdfx.streamlit.app).

## 🌟 Application Overview

The Knowledge Base Chatbot leverages advanced natural language processing techniques to understand and respond to user inquiries based on the content extracted from uploaded or linked PDF documents. This application primarily aims to assist users in obtaining quick answers without the need to manually search through extensive documents.

### ✨ Features

- **PDF Content Extraction**: Users can provide PDFs either via direct upload or through a link. The application then extracts the text from the PDF for processing. 📄
- **Conversational Interface**: Users can query the extracted text through a conversational interface, receiving responses that are contextually relevant to the input PDF content. 💬
- **Streamlit Deployment**: The application is hosted on Streamlit Cloud, offering a user-friendly and accessible interface. 🌐

### 🛠 Technical Details

- **PDF Processing**: Utilizes `pypdf` to read and extract text from PDF files.
- **Generative AI**: Leverages OpenAI's GPT-3.5 model to generate answers based on the extracted content. 🧠
- **Environment Management**: Uses environment variables for API keys and sensitive data, ensuring security and configurability. 🔐

## 🧠 Understanding of Generative AI Concepts

The Knowledge Base Chatbot leverages 🤖 Generative AI by integrating OpenAI's GPT-3.5 model, showcasing advanced language understanding and generation capabilities. This integration enables the chatbot to interpret user queries and generate contextually relevant answers based on the content extracted from PDF documents, demonstrating a comprehensive grasp of natural language processing (NLP) techniques.

## ✅ Quality and Clarity of the Application

### 🚀 Modifications and Improvements
The chatbot is designed with user interaction at its core, allowing for PDF submissions through both direct uploads and URL links 🌐. It includes robust error handling to provide clear feedback on PDF load or extraction issues, enhancing reliability and user experience.

### 📝 Clarity
The interface uses Streamlit’s interactive features to create a simple and intuitive user environment. Backend functions are modular, handling tasks like PDF content extraction, text processing, and AI-driven conversations, ensuring a clear and maintainable codebase.

## 🚀 Getting Started

To use the chatbot, follow these steps:
1. Navigate to the [application page](https://personalchatbotgit-swtxqf6emsroewvi3ugdfx.streamlit.app).
2. Provide a PDF by uploading a file or entering a link to a PDF. 📤
3. Once the PDF is processed, enter your questions in the chat interface. 🗨️

## Working Photos:

#### When I uploaded my resume from my local computer this is how i interacted with the chatbot:
![ResumeUpload](/Images/1.png)
![ResumeUpload](/Images/2.png)

#### When I attempt to ask questions that are 'out-of-bound,' the chatbot verifies whether the question is relevant. If it's not, it will display a message requesting relevant questions. This demonstrates that the prompt engineering was effectively executed to ensure responses stay within the scope of the uploaded content.

![ResumeUpload](/Images/3.png)

#### When I try to access a pdf file from an online link

![ResumeUpload](/Images/4.png)





### 🚨 Notice

- Please ensure that the PDF files provided are no longer than 5 pages to ensure optimal performance and responsiveness. 📋

## 💻 Development and Deployment

This application is developed using Python and deployed on Streamlit Cloud. Key libraries and frameworks used include `streamlit`, `pypdf`, `requests`, and `openai`.

## 🤝 Contribution

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. 🔄

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

For support or queries, reach out via the contact form on the application website.

## 🎉 Acknowledgements

- OpenAI for the GPT models
- Streamlit for the deployment platform
- Contributors and supporters of this project
