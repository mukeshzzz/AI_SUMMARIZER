import streamlit as st
import requests

st.title("📄 AI Summarize")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
question = st.text_input("Ask a question about the PDF:")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    response = requests.post("http://127.0.0.1:8000/upload/", files={"file": open("temp.pdf", "rb")})
    extracted_text = response.json()["extracted_text"]

    if st.button("Summarize"):
        summary_response = requests.post("http://127.0.0.1:8000/summarize/", files={"file": open("temp.pdf", "rb")})
        st.write("📜 **Summary:**")
        st.write(summary_response.json()["summary"])

    if st.button("Ask"):
        qa_response = requests.post("http://127.0.0.1:8000/ask/", files={"file": open("temp.pdf", "rb")}, params={"question": question})
        st.write("💡 **Answer:**")
        st.write(qa_response.json()["answer"])
