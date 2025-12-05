import streamlit as st
from utils.auth import authenticate_user
import time

def show():
    """Professional login page with purple gradient theme"""
    
    # Custom CSS matching the purple gradient style
    st.markdown(r"""
    <style>
    /* Purple gradient background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Center content vertically */
    .block-container {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Professional white card */
    .login-card {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 24px;
        padding: 3rem 2.5rem;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(10px);
        margin: 0 auto;
    }
    
    /* Welcome section */
    .welcome-section {
        text-align: center;
        margin-bottom: 2.5rem;
        padding-bottom: 2rem;
        border-bottom: 2px solid #f0f0f0;
    }
    
    .welcome-icon {
        width: 70px;
        height: 70px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1.5rem;
        font-size: 2.2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    
    .welcome-title {
        font-size: 2rem;
        font-weight: 700;
        color: #2d3748;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.5px;
    }
    
    .welcome-subtitle {
        font-size: 1rem;
        color: #718096;
        font-weight: 500;
        margin: 0;
    }
    
    /* Form label */
    .form-label {
        display: block;
        font-size: 0.9rem;
        font-weight: 600;
        color: #4a5568;
        margin-bottom: 0.6rem;
        letter-spacing: 0.3px;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        background: #f7fafc !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 12px !important;
        color: #2d3748 !important;
        padding: 1rem 1.2rem !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05) !important;
    }
    
    .stTextInput > div > div > input:focus {
        background: #ffffff !important;
        border: 2px solid #667eea !important;
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1),
                    0 2px 4px rgba(0, 0, 0, 0.05) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #a0aec0 !important;
    }
    
    .stTextInput > label {
        display: none !important;
    }
    
    .stTextInput {
        margin-bottom: 1.5rem;
    }
    
    /* Submit button */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 1rem 2rem !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4) !important;
        margin-top: 1rem !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 30px rgba(102, 126, 234, 0.5) !important;
    }
    
    /* Success message */
    .success-message {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        padding: 1.1rem 1.3rem;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 0.95rem;
        margin-top: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.8rem;
        box-shadow: 0 6px 15px rgba(72, 187, 120, 0.4);
        animation: slideIn 0.4s ease;
    }
    
    .success-message::before {
        content: '✓';
        display: flex;
        align-items: center;
        justify-content: center;
        width: 26px;
        height: 26px;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        font-size: 0.9rem;
        font-weight: 700;
    }
    
    /* Error message */
    .error-message {
        background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%);
        color: white;
        padding: 1.1rem 1.3rem;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 0.95rem;
        margin-top: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.8rem;
        box-shadow: 0 6px 15px rgba(245, 101, 101, 0.4);
        animation: shake 0.4s ease;
    }
    
    .error-message::before {
        content: '✕';
        display: flex;
        align-items: center;
        justify-content: center;
        width: 26px;
        height: 26px;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        font-size: 1rem;
        font-weight: 700;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-10px); }
        75% { transform: translateX(10px); }
    }
    
    /* Security badge */
    .security-info {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.6rem;
        margin-top: 1.8rem;
        padding: 0.9rem;
        background: rgba(102, 126, 234, 0.08);
        border-radius: 10px;
        font-size: 0.85rem;
        color: #667eea;
        font-weight: 600;
        border: 1px solid rgba(102, 126, 234, 0.15);
    }
    
    .security-info::before {
        content: '🔒';
        font-size: 1.1rem;
    }
    
    /* Footer */
    .login-footer {
        text-align: center;
        margin-top: 2rem;
        padding-top: 1.8rem;
        border-top: 2px solid #f0f0f0;
    }
    
    .login-footer p {
        color: #718096;
        font-size: 0.9rem;
        margin: 0;
        font-weight: 500;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Form adjustments */
    .stForm {
        margin: 0 !important;
        padding: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create centered layout with proper columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Welcome section
        st.markdown("""
        <div class="welcome-section">
            <div class="welcome-icon">🔐</div>
            <h1 class="welcome-title">Welcome Back</h1>
            <p class="welcome-subtitle">Sign in to continue to your account</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Login form
        with st.form("login_form", clear_on_submit=False):
            # Username field
            st.markdown('<label class="form-label">Username</label>', unsafe_allow_html=True)
            username = st.text_input("Username", placeholder="Enter your username", label_visibility="collapsed", key="username_field")
            
            # Password field
            st.markdown('<label class="form-label">Password</label>', unsafe_allow_html=True)
            password = st.text_input("Password", type="password", placeholder="Enter your password", label_visibility="collapsed", key="password_field")
            
            # Submit button
            submit = st.form_submit_button("Sign In", use_container_width=True)

            # Handle form submission
            if submit:
                if not username or not password:
                    st.markdown('<div class="error-message">Please enter both username and password</div>', unsafe_allow_html=True)
                else:
                    success, message = authenticate_user(username, password)
                    if success:
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.markdown(f'<div class="success-message">{message} Redirecting to dashboard...</div>', unsafe_allow_html=True)
                        st.balloons()
                        time.sleep(2)
                        st.session_state.page = "Predictor"
                        st.rerun()
                    else:
                        st.markdown(f'<div class="error-message">{message}</div>', unsafe_allow_html=True)
        
        # Security badge
        st.markdown("""
        <div class="security-info">
            Secure & Encrypted Connection
        </div>
        """, unsafe_allow_html=True)
        
        # Footer
        st.markdown("""
        <div class="login-footer">
            <p>© 2024 StockAI. All rights reserved.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)