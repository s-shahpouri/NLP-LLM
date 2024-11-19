import streamlit as st
from llama_index.llms import Ollama

# Initialize the LLM
OLLAMA_MODEL = "llama3.2"
llm = Ollama(model=OLLAMA_MODEL)

st.title("Question & Answer with Ollama")

# Input question
question = st.text_input("Ask a question:")

if st.button("Submit"):
    if question:
        response = llm.complete(question)
        st.subheader("Answer:")
        st.write(response)
    else:
        st.warning("Please enter a question.")
