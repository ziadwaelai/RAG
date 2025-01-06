import streamlit as st
from backend.processing import cvParser
from backend.language_model import llama_handler
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def chat_tab_view():
    model = llama_handler.llm_initializer()
    conversation = ConversationChain(llm=model, memory=st.session_state.memory)
    st.title('Chat Tab')
    st.write('Welcome to the Chat Tab!')

    # Initialize message history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I help you?"}
        ]

    # Display the chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle user input
    if user_input := st.chat_input("What is up?"):
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()  # Placeholder for message
            response_parts = []
            try:
                for part in conversation.predict(input=user_input):  # Iterate over generator
                    response_parts.append(part)
                    message_placeholder.markdown("".join(response_parts))  # Update response progressively
                response = "".join(response_parts)  # Final response
            except Exception as e:
                response = "Oops! Something went wrong."
                message_placeholder.markdown(response)
                st.error(f"Error: {e}")

        # Add assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Option to reset chat
    if st.sidebar.button("Reset Chat"):
        # reload the page
        print("Reloading page")


