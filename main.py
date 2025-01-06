from backend.processing import cvParser
from Streamlit_App.tabs import chat_tab,upload_tab
import streamlit as st


PAGES = {
    "chat": chat_tab.chat_tab_view,
    "upload": upload_tab.upload_tab_view
}
def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    PAGES[selection]()

if __name__ == "__main__":
    main()
