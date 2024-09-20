import streamlit as st
from py_dotenv import read_dotenv
import os

import ai
import pdf

import nest_asyncio
nest_asyncio.apply()

import asyncio

read_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

st.set_page_config(page_title="School.ai")
st.title("Easier way to study i guess")

st.session_state["llm_model"] = "mixtral-8x7b-32768"    
st.session_state.messages = []
st.session_state["document_data"] = None

document = st.file_uploader("Upload a part of a textbook...")

if document is not None:
    bytes = document.getvalue()
    parsed = asyncio.run(pdf.parse_file(bytes, document.name))
    st.session_state["document_data"] = parsed[0].text
    
if st.session_state["document_data"] != None:
    if st.button("Generate practice questions", type="primary"):
        st.session_state.messages.append({"role": "user", "content": f"Generate practice questions: {st.session_state['document_data']}"})
        with st.chat_message("user"):
            st.markdown("Generate practice questions")
        with st.chat_message("ai"):
            call = ai.prompt("Generate practice questions for me.", st.session_state["llm_model"], st.session_state["document_data"])
            st.write(call.choices[0].message.content)
        st.session_state.messages.append({"role": "ai", "content": call.choices[0].message.content})

# if prompt := st.chat_input("Ask anything..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     with st.chat_message("ai"):
#         response = ai.prompt(prompt, st.session_state["llm_model"])
#         written = st.write(response.choices[0].message.content)
#     st.session_state.messages.append({"role": "ai", "content": written})