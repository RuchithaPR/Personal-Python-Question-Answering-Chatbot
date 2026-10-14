import streamlit as st
from chatbot import get_answer

st.title("🐍 Python Question-Answering Chatbot")

st.write("Welcome! Ask me a question about Python, AI, or Machine Learning.")

question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question.strip():
        answer, score = get_answer(question)

        st.subheader("Answer")
        st.write(answer)

        st.caption(f"Similarity score: {score:.2f}")
    else:
        st.warning("Please enter a question first.")