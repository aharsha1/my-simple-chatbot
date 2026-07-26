import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq


# Load API key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# Website title
st.title("🤖 My Simple AI Chatbot")


# Memory storage
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]


# Show previous chats
for message in st.session_state.messages:

    if message["role"] != "system":

        st.chat_message(
            message["role"]
        ).write(
            message["content"]
        )


# Chat input box
user_question = st.chat_input(
    "Ask something..."
)


if user_question:


    # Display user message

    st.chat_message("user").write(
        user_question
    )


    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )


    # Send request to Groq

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=st.session_state.messages

    )


    answer = response.choices[0].message.content


    # Display AI answer

    st.chat_message("assistant").write(
        answer
    )


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
