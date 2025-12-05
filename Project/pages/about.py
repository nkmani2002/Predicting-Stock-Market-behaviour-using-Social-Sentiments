
# import streamlit as st

# def show():
#     """About page"""
#     st.markdown('<div class="animated-title">About Our Platform</div>', unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="card">
#         <h2 style="color: #667eea; margin-bottom: 1.5rem;">🎯 Our Mission</h2>
#         <p style="font-size: 1.15rem; line-height: 1.8; color: #333; margin-bottom: 2rem;">
#         We aim to democratize stock market prediction by combining social media sentiment analysis 
#         with advanced machine learning algorithms. Our platform helps traders and investors make 
#         informed decisions based on real-time data and predictive analytics.
#         </p>
        
#         <h2 style="color: #667eea; margin-top: 2.5rem; margin-bottom: 1.5rem;">🔬 Technology Stack</h2>
#         <ul style="font-size: 1.1rem; line-height: 2.2; color: #333;">
#             <li><strong style="color: #667eea;">Machine Learning:</strong> Random Forest, Logistic Regression, SVM</li>
#             <li><strong style="color: #667eea;">Sentiment Analysis:</strong> VADER Sentiment Analyzer</li>
#             <li><strong style="color: #667eea;">Data Processing:</strong> Pandas, NumPy</li>
#             <li><strong style="color: #667eea;">Visualization:</strong> Plotly, Seaborn</li>
#             <li><strong style="color: #667eea;">Framework:</strong> Streamlit</li>
#         </ul>
        
#         <h2 style="color: #667eea; margin-top: 2.5rem; margin-bottom: 1.5rem;">📧 Contact Us</h2>
#         <p style="font-size: 1.1rem; line-height: 1.8; color: #333;">
#         <strong>Email:</strong> support@stockai.com<br>
#         <strong>Twitter:</strong> @StockAI_Predict<br>
#         <strong>Support:</strong> Available 24/7
#         </p>
#     </div>
#     """, unsafe_allow_html=True)


import streamlit as st

def show():
    """About page with modern design"""
    st.markdown('<div class="animated-title">About StockAI Platform</div>', unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
    <div class="card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-align: center; padding: 3rem;">
        <h1 style="font-size: 2.5rem; margin-bottom: 1rem; color: white;">🚀 Transforming Market Predictions</h1>
        <p style="font-size: 1.3rem; opacity: 0.95; color: white;">
        Empowering traders with AI-driven sentiment analysis and real-time market insights
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mission and Vision Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <div style="text-align: center; margin-bottom: 1.5rem;">
                <span style="font-size: 4rem;">🎯</span>
            </div>
            <h2 style="color: #667eea; text-align: center; margin-bottom: 1.5rem;">Our Mission</h2>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #555; text-align: center;">
            We democratize stock market prediction by combining social media sentiment analysis 
            with cutting-edge machine learning algorithms. Our platform empowers traders and 
            investors to make data-driven decisions with confidence.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <div style="text-align: center; margin-bottom: 1.5rem;">
                <span style="font-size: 4rem;">👁️</span>
            </div>
            <h2 style="color: #667eea; text-align: center; margin-bottom: 1.5rem;">Our Vision</h2>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #555; text-align: center;">
            To become the world's most trusted AI-powered financial analytics platform, 
            making advanced market prediction tools accessible to everyone worldwide.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Technology Stack
    st.markdown("""
    <div class="card">
        <h2 style="color: #667eea; text-align: center; margin-bottom: 2rem;">🔬 Our Technology Stack</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Using Streamlit columns for better compatibility
    col1, col2, col3 = st.columns(3)
    
    technologies = [
        ("🤖", "Machine Learning", "Random Forest, Logistic Regression, Support Vector Machines"),
        ("💭", "Sentiment Analysis", "VADER Sentiment Analyzer for real-time tweet processing"),
        ("📊", "Data Processing", "Pandas & NumPy for efficient data manipulation"),
        ("📈", "Visualization", "Plotly & Seaborn for interactive charts"),
        ("⚡", "Framework", "Streamlit for responsive web applications"),
        ("🔒", "Security", "Encrypted user authentication & data protection")
    ]
    
    for i, (icon, title, desc) in enumerate(technologies):
        col = [col1, col2, col3][i % 3]
        with col:
            st.markdown(f"""
            <div class="card" style="text-align: center; min-height: 200px;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">{icon}</div>
                <h3 style="color: #667eea; margin-bottom: 1rem; font-size: 1.3rem;">{title}</h3>
                <p style="color: #666; font-size: 0.95rem; line-height: 1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Statistics Section
    st.markdown("""
    <div class="card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 2rem;">
        <h2 style="text-align: center; margin-bottom: 2rem; color: white;">📊 Platform Statistics</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">🧑‍💼</div>
            <h2 style="font-size: 2.5rem; margin-bottom: 0.5rem; color: #667eea;">500+</h2>
            <p style="font-size: 1.1rem; color: #555;">Active Users</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔮</div>
            <h2 style="font-size: 2.5rem; margin-bottom: 0.5rem; color: #667eea;">10K+</h2>
            <p style="font-size: 1.1rem; color: #555;">Predictions Made</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎯</div>
            <h2 style="font-size: 2.5rem; margin-bottom: 0.5rem; color: #667eea;">85%</h2>
            <p style="font-size: 1.1rem; color: #555;">Accuracy Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">💬</div>
            <h2 style="font-size: 2.5rem; margin-bottom: 0.5rem; color: #667eea;">24/7</h2>
            <p style="font-size: 1.1rem; color: #555;">Support Available</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Features Section
    st.markdown("""
    <div class="card">
        <h2 style="color: #667eea; text-align: center; margin-bottom: 2rem;">✨ Key Features</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    features = [
        ("⚡", "Real-Time Analysis", "Get instant sentiment analysis from social media trends"),
        ("🎯", "High Accuracy", "85%+ prediction accuracy with ensemble ML models"),
        ("📱", "Easy to Use", "Upload CSV files and get results in seconds"),
        ("🔒", "Secure", "Your data is encrypted and stored securely"),
        ("📊", "Visual Reports", "Interactive charts and confusion matrices"),
        ("🌐", "Multi-Stock", "Support for multiple stock symbols simultaneously")
    ]
    
    for i, (icon, title, desc) in enumerate(features):
        col = [col1, col2, col3][i % 3]
        with col:
            st.markdown(f"""
            <div class="card" style="border-left: 4px solid #667eea; min-height: 150px;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{icon}</div>
                <h3 style="color: #667eea; margin-bottom: 0.5rem; font-size: 1.2rem;">{title}</h3>
                <p style="color: #666; font-size: 0.95rem; line-height: 1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contact Section
    st.markdown("""
    <div class="card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-align: center; padding: 3rem;">
        <h2 style="margin-bottom: 2rem; color: white;">📧 Get In Touch</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📧</div>
            <p style="font-size: 1.1rem; margin-bottom: 0.3rem; font-weight: 600; color: #667eea;">Email</p>
            <p style="color: #666;">support@stockai.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🐦</div>
            <p style="font-size: 1.1rem; margin-bottom: 0.3rem; font-weight: 600; color: #667eea;">Twitter</p>
            <p style="color: #666;">@StockAI_Predict</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">💬</div>
            <p style="font-size: 1.1rem; margin-bottom: 0.3rem; font-weight: 600; color: #667eea;">Support</p>
            <p style="color: #666;">24/7 Available</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🌐</div>
            <p style="font-size: 1.1rem; margin-bottom: 0.3rem; font-weight: 600; color: #667eea;">Website</p>
            <p style="color: #666;">www.stockai.com</p>
        </div>
        """, unsafe_allow_html=True)