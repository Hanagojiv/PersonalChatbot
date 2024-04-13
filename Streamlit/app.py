import streamlit as st
from pypdf import PdfReader
import requests
import io
import os
from dotenv import load_dotenv
import openai


# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_pdf_content_from_link(link: str):
    response = requests.get(link)
    response.raise_for_status()  # Check for HTTP errors.
    return response.content

def extract_pdf_content_using_pypdf(content: bytes) -> (str, int):
    reader = PdfReader(io.BytesIO(content))
    extracted_text = ""
    num_words = 0
    for page in reader.pages:
        page_text = page.extract_text() or ""
        extracted_text += page_text
        num_words += len(page_text.split())
    return extracted_text, num_words

def get_answer_from_openai(pdf_content, user_input):
    try:
        messages = [
            {"role": "system", "content": "You are a knowledgeable assistant. Answer questions based on this document content."},
            {"role": "system", "content": pdf_content},
            {"role": "user", "content": user_input}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Streamlit chat UI
# URL of the GIF
gif_url = "https://static.helpjuice.com/helpjuice_production/uploads/upload/image/4752/direct/1548993346223-opt3.gif"

# Display the GIF
st.image(gif_url)

# Then display your title
st.title("   Knowledge Base Chatbot")



# Provide the PDF
# with st.expander("Provide the PDF"):
input_type_option = st.selectbox("Provide the PDF", ("Link", "Upload a PDF"))
file_content = None

if input_type_option == 'Link':
    file_link = st.text_input("Enter the PDF link")
    if st.button("Load PDF from Link"):
        try:
            file_content = get_pdf_content_from_link(file_link)
            pdf_text, num_words = extract_pdf_content_using_pypdf(file_content)
            st.session_state.pdf_content = pdf_text
            st.success(f"PDF loaded with {num_words} words extracted.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

elif input_type_option == 'Upload a PDF':
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file is not None:
        file_content = uploaded_file.read()
        pdf_text, num_words = extract_pdf_content_using_pypdf(file_content)
        st.session_state.pdf_content = pdf_text
        st.success(f"PDF loaded with {num_words} words extracted.")

# User input for chat
# if 'pdf_content' in st.session_state and (user_input := st.chat_input("Your question:")):
#     # Append user message to chat history and display it
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Get the response from the chatbot
#     bot_response = get_answer_from_openai(st.session_state.pdf_content, user_input)
    
#     # Display typing indicator
#     for _ in range(5):  # Simulate typing for 0.5 seconds
#         time.sleep(0.1)

#     # Append bot response to chat history and display it
#     st.session_state.messages.append({"role": "assistant", "content": bot_response})
#     with st.chat_message("assistant"):
#         st.markdown(bot_response)






st.header("Chat with the Bot")

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# # Display chat history using st.chat_message
# for message in st.session_state.messages:
#     role = message["role"]
#     content = message["content"]
#     with st.chat_message(role=role):
#         st.write(content)

# User input for chat
# ... [other parts of your code] ...


if 'pdf_content' in st.session_state and (user_input := st.chat_input("Your question:")):
    # Append user message to chat history and display it
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get the response from the chatbot based on the PDF content and the user query
    bot_response = get_answer_from_openai(st.session_state.pdf_content, user_input)

    # Append bot response to chat history and display it
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# # User input for chat
# user_input = st.text_input("Your question:", key="user_query")

# # Check for the input and whether the PDF content is loaded
# if 'pdf_content' in st.session_state and user_input:
#     if st.button("Send"):
#         # Append user message to chat history
#         st.session_state.messages.append({"role": "user", "content": user_input})

#         # Display user message
#         with st.chat_message("user"):
#             st.markdown(user_input)

#         # Clear the input box for next message
#         st.session_state.user_input = ""

#         # Display temporary "typing..." message
#         with st.chat_message("assistant"):
#             typing_placeholder = st.empty()
#             typing_placeholder.text("Bot is typing...")

#         # Here you could add code to wait for the bot response
#         # ...

#         # After getting the response, empty the placeholder
#         typing_placeholder.empty()

#         # Get the response from the chatbot
#         bot_response = get_answer_from_openai(st.session_state.pdf_content, user_input)

#         # Append bot response to chat history and display it
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         with st.chat_message("assistant"):
#             st.markdown(bot_response)

#         # Rerun the app to reflect the changes in the UI
#         st.experimental_rerun()

# # This is necessary to manage the chat history and new input effectively
# if 'user_input' in st.session_state and st.session_state.user_input == '':
#     del st.session_state.user_input

# User input for chat
# user_input = st.text_input("Your question:", key="user_query")
# if st.button("Send"):
#     if user_input:
#         # Append user message to chat history
#         st.session_state.messages.append({"role": "user", "content": user_input})
        
#         # Get the response from the chatbot based on the PDF content and the user query
#         bot_response = get_answer_from_openai(st.session_state.pdf_content, user_input)
        
#         # Append bot response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
#         # Rerun the script to update the chat history
#         st.experimental_rerun()
