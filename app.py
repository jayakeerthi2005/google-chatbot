import streamlit as st
import google.generativeai as genai

# Google API Key
API_KEY = "AQ.Ab8RN6KPmFaPlXv2KM1HkCLNYZQImXou6bDacsnNTc8HdYEvVQ"

genai.configure(api_key=API_KEY)

# Updated Gemini model
model = genai.GenerativeModel("gemini-3.8-flash")

# Streamlit page
st.set_page_config(
    page_title="Google Gemini Chatbot",
    page_icon="🤖"
)

st.title("🤖 Google Gemini Chatbot")
st.write("Ask anything to Gemini!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        # Send message to Gemini
        response = model.generate_content(user_input)

        bot_response = response.text

        # Show response
        with st.chat_message("assistant"):
            st.markdown(bot_response)

        # Save response
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_response
        })

    except Exception as e:
        st.error(f"Error: {e}")