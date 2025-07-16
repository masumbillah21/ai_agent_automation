import streamlit as st
import asyncio
from workflows.customer_support_graph import create_customer_support_graph
from dotenv import load_dotenv

load_dotenv()
graph = create_customer_support_graph()

st.set_page_config(page_title="AI Agent Assistant", page_icon="🤖")

st.title("AI Agent Assistant")
st.write("Ask your question below:")

if "history" not in st.session_state:
    st.session_state.history = []

if "pending" not in st.session_state:
    st.session_state.pending = None


for entry in st.session_state.history:
    st.markdown(f"**You:** {entry['user']}")
    st.markdown(f"**AI:** {entry['ai']}")


if st.session_state.pending:
    st.markdown(f"**You:** {st.session_state.pending}")
    with st.spinner("Processing..."):
        result = asyncio.run(graph.ainvoke({"input_text": st.session_state.pending}))
        ai_response = result["response"]
    st.session_state.history.append({"user": st.session_state.pending, "ai": ai_response})
    st.session_state.pending = None
    st.rerun()

with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        query = st.text_input("💬", label_visibility="collapsed", placeholder="Type your message...")
    with col2:
        submit = st.form_submit_button("Submit")

    if submit and query.strip():
        st.session_state.pending = query
        st.rerun()
