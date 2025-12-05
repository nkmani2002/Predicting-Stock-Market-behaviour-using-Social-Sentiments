
import streamlit as st
from pages import home, about, login, register, predictor
from utils import styles, navbar

# Page configuration
st.set_page_config(
    page_title="Stock Sentiment Predictor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom styles
styles.apply_custom_styles()

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Main app logic
def main():
    # Display navbar
    navbar.create_navbar()
    
    # Route to appropriate page
    if st.session_state.page == "Home":
        home.show()
    elif st.session_state.page == "About":
        about.show()
    elif st.session_state.page == "Login":
        login.show()
    elif st.session_state.page == "Register":
        register.show()
    elif st.session_state.page == "Predictor":
        predictor.show()
        

if __name__ == "__main__":
    main()