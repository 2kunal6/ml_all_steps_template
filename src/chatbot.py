# Reference https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps#build-a-bot-that-mirrors-your-input
from inference import ChromaDB

import streamlit as st


st.title("Echo Bot")

chroma_db = ChromaDB()

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)


# Display assistant response in chat message container
with st.chat_message("assistant"):
    if(prompt is not None):
        st.markdown(chroma_db.get_inference(prompt))
