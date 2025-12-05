import streamlit as st
from utils.auth import register_user
import time

def show():
    """Professional registration page with corporate design"""
    
    # Custom CSS for professional, modern design
    st.markdown("""
    <style>
    /* Clean professional background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Professional title */
    .prof-title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        color: #ffffff;
        margin-bottom: 1rem;
        letter-spacing: 1px;
    }
    
    .prof-subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        margin-bottom: 3rem;
        font-weight: 400;
    }
    
    /* Professional card container */
    .prof-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 3rem 2.5rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        max-width: 500px;
        margin: 0 auto;
    }
    
    /* Form header */
    .form-header {
        text-align: center;
        margin-bottom: 2.5rem;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 1.5rem;
    }
    
    .form-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: inline-block;
        color: #667eea;
    }
    
    .form-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 0;
    }
    
    .form-description {
        color: #7f8c8d;
        font-size: 0.95rem;
        margin-top: 0.5rem;
    }
    
    /* Input fields styling */
    .stTextInput > div > div > input {
        background: #f8f9fa !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 8px !important;
        color: #2c3e50 !important;
        padding: 0.9rem 1rem !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        background: #ffffff !important;
        border: 2px solid #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #adb5bd !important;
    }
    
    .stTextInput > label {
        color: #2c3e50 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Submit button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.9rem 2rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
    }
    
    /* Success message */
    .success-msg {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        text-align: center;
        font-weight: 500;
        margin-top: 1.5rem;
        font-size: 0.95rem;
    }
    
    .success-icon {
        color: #28a745;
        font-size: 1.2rem;
        margin-right: 0.5rem;
    }
    
    /* Error message */
    .error-msg {
        background: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        text-align: center;
        font-weight: 500;
        margin-top: 1.5rem;
        font-size: 0.95rem;
    }
    
    .error-icon {
        color: #dc3545;
        font-size: 1.2rem;
        margin-right: 0.5rem;
    }
    
    /* Info section */
    .info-section {
        text-align: center;
        margin-top: 2rem;
        padding-top: 1.5rem;
        border-top: 2px solid #f0f0f0;
        color: #7f8c8d;
        font-size: 0.9rem;
    }
    
    .info-section a {
        color: #667eea;
        text-decoration: none;
        font-weight: 600;
    }
    
    .info-section a:hover {
        text-decoration: underline;
    }
    
    /* Features section */
    .features {
        display: flex;
        gap: 1.5rem;
        margin-top: 2rem;
        flex-wrap: wrap;
    }
    
    .feature-item {
        flex: 1;
        min-width: 140px;
        text-align: center;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
    }
    
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-text {
        font-size: 0.85rem;
        color: #495057;
        font-weight: 500;
    }
    
    /* Password requirements */
    .requirements {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
        font-size: 0.85rem;
        color: #6c757d;
    }
    
    .requirements ul {
        margin: 0.5rem 0 0 1.5rem;
        padding: 0;
    }
    
    .requirements li {
        margin: 0.3rem 0;
    }
    
    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
    
    # Title section
    st.markdown('<div class="prof-title">Welcome to Our Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="prof-subtitle">Create an account to get started</div>', unsafe_allow_html=True)
    
    # Create centered layout
    col1, col2, col3 = st.columns([1, 2.5, 1])
    
    with col2:
        st.markdown('<div class="prof-card">', unsafe_allow_html=True)
        
        # Form header
        st.markdown("""
        <div class="form-header">
            <div class="form-icon">👤</div>
            <h2 class="form-title">Create Account</h2>
            <p class="form-description">Fill in your details to register</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("register_form"):
            username = st.text_input("Username", placeholder="Enter username")
            email = st.text_input("Email Address", placeholder="your.email@example.com")
            password = st.text_input("Password", type="password", placeholder="Enter password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm password")
            
            # Password requirements
            st.markdown("""
            <div class="requirements">
                <strong>Password Requirements:</strong>
                <ul>
                    <li>At least 8 characters long</li>
                    <li>Contains uppercase and lowercase letters</li>
                    <li>Includes numbers and special characters</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            submit = st.form_submit_button("Create Account", use_container_width=True)
            
            if submit:
                if not username or not email or not password:
                    st.markdown('<div class="error-msg"><span class="error-icon">⚠️</span>Please fill in all required fields</div>', unsafe_allow_html=True)
                elif password != confirm_password:
                    st.markdown('<div class="error-msg"><span class="error-icon">⚠️</span>Passwords do not match. Please try again.</div>', unsafe_allow_html=True)
                elif len(password) < 8:
                    st.markdown('<div class="error-msg"><span class="error-icon">⚠️</span>Password must be at least 8 characters long</div>', unsafe_allow_html=True)
                else:
                    success, message = register_user(username, password, email)
                    if success:
                        st.markdown(f'<div class="success-msg"><span class="success-icon">✓</span>{message}</div>', unsafe_allow_html=True)
                        time.sleep(2)
                        st.session_state.page = "Login"
                        st.rerun()
                    else:
                        st.markdown(f'<div class="error-msg"><span class="error-icon">⚠️</span>{message}</div>', unsafe_allow_html=True)
        
        # Info section
        st.markdown("""
        <div class="info-section">
            Already have an account? <a href="#">Sign in here</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Features section below the card
        st.markdown("""
        <div class="features">
            <div class="feature-item">
                <div class="feature-icon">🔒</div>
                <div class="feature-text">Secure & Encrypted</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">⚡</div>
                <div class="feature-text">Fast Setup</div>
            </div>
            <div class="feature-item">
                <div class="feature-icon">✓</div>
                <div class="feature-text">Verified Accounts</div>
            </div>
        </div>
        """, unsafe_allow_html=True)