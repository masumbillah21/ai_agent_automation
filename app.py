import streamlit as st
import asyncio
from workflows.customer_support_graph import create_customer_support_graph
from dotenv import load_dotenv

load_dotenv()
graph = create_customer_support_graph()

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="AI Agent Assistant", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center;'>AI Agent Assistant 🤖</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "processing" not in st.session_state:
    st.session_state.processing = False


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_question = st.chat_input("Type your question and press Enter")
if user_question and not st.session_state.processing:
    st.session_state.processing = True
    st.session_state.messages.append({"role": "user", "content": user_question})
    st.rerun()

if st.session_state.processing and st.session_state.messages:
    latest_message = st.session_state.messages[-1]
    if latest_message["role"] == "user":
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            assistant_response = asyncio.run(
                graph.ainvoke({"input_text": latest_message["content"]})
            )

            full_response = ""
            for char in assistant_response["response"]:
                full_response += char
                response_placeholder.markdown(full_response)
                asyncio.sleep(0.01)

            st.session_state.messages.append({"role": "assistant", "content": full_response})

        st.session_state.processing = False
        st.rerun()
