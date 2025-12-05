
def apply_custom_styles():
    import streamlit as st
    st.markdown("""
    <style>
        /* Hide sidebar completely */
        [data-testid="stSidebar"] {
            display: none;
        }
        
        /* Remove default background */
        .stApp {
            background: #ffffff;
        }
        
        /* Main container */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 100%;
        }
        
        /* Enhanced Navbar styling */
        .navbar-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem 3rem;
            margin: -2rem -2rem 2rem -2rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            animation: slideDown 0.8s ease-out;
        }
        
        @keyframes slideDown {
            from { transform: translateY(-100px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        
        .navbar-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .logo {
            font-size: 2.5rem;
            font-weight: 900;
            color: white;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
            letter-spacing: 1px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .logo-icon {
            font-size: 3rem;
            animation: bounce 2s ease-in-out infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        /* Enhanced nav buttons */
        .nav-button-container {
            display: flex;
            gap: 1rem;
            align-items: center;
        }
        
        /* Card styling */
        .card {
            background: white;
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            animation: fadeInUp 1s ease-out;
            margin: 1.5rem 0;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid #f0f0f0;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 50px rgba(0, 0, 0, 0.15);
        }
        
        @keyframes fadeInUp {
            from { transform: translateY(50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        
        /* Button styling */
        .stButton>button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            font-size: 1rem;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        }
        
        /* Nav buttons specific styling */
        div[data-testid="column"] .stButton>button {
            width: 100%;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            color: white;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        div[data-testid="column"] .stButton>button:hover {
            background: rgba(255, 255, 255, 0.3);
            border-color: rgba(255, 255, 255, 0.5);
            transform: translateY(-2px);
        }
        
        /* Input fields */
        .stTextInput>div>div>input, .stSelectbox>div>div>select {
            border-radius: 12px;
            border: 2px solid #e0e0e0;
            padding: 0.75rem;
            transition: all 0.3s ease;
        }
        
        .stTextInput>div>div>input:focus, .stSelectbox>div>div>select:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        /* Animated title */
        .animated-title {
            font-size: 3rem;
            font-weight: 900;
            background: linear-gradient(45deg, #667eea, #764ba2, #667eea);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientText 3s ease infinite;
            text-align: center;
            margin: 2rem 0;
        }
        
        @keyframes gradientText {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Success/Error messages */
        .success-msg {
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
            padding: 1.2rem;
            border-radius: 12px;
            animation: slideIn 0.5s ease-out;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
            font-weight: 600;
        }
        
        .error-msg {
            background: linear-gradient(135deg, #ef4444, #dc2626);
            color: white;
            padding: 1.2rem;
            border-radius: 12px;
            animation: shake 0.5s ease-out;
            box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
            font-weight: 600;
        }
        
        @keyframes slideIn {
            from { transform: translateX(-100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            75% { transform: translateX(10px); }
        }
        
        /* Metric styling */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
            background-color: transparent;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 60px;
            background-color: white;
            border-radius: 12px;
            padding: 0 2rem;
            font-weight: 600;
            border: 2px solid #e0e0e0;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #f8f9fa;
            border-color: #667eea;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)