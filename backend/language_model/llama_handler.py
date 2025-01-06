from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import streamlit as st


# Initialize the language model
def llm_initializer():
    # Initialize memory
    if "memory" not in st.session_state:
        memory = ConversationBufferMemory()
        st.session_state.memory = memory
    model = OllamaLLM(model="llama3.2", memory=st.session_state.memory)
    return model


