import streamlit as st

def show():
    # Hero Section with Gradient Background
    st.markdown("""
        <style>
        /* Animated gradient background */
        .hero-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 80px 20px;
            border-radius: 20px;
            margin-bottom: 40px;
            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
            animation: pulse 3s ease-in-out infinite;
            position: relative;
            overflow: hidden;
        }
        
        @keyframes pulse {
            0%, 100% { box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3); }
            50% { box-shadow: 0 20px 80px rgba(102, 126, 234, 0.5); }
        }
        
        /* Glowing particles effect */
        .hero-section::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: particles 20s linear infinite;
        }
        
        @keyframes particles {
            0% { transform: translate(0, 0); }
            100% { transform: translate(50px, 50px); }
        }
        
        .hero-title {
            font-size: 3.5em;
            font-weight: 800;
            color: white;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 0 30px rgba(255,255,255,0.5);
            animation: glow 2s ease-in-out infinite;
            position: relative;
            z-index: 1;
        }
        
        @keyframes glow {
            0%, 100% { text-shadow: 0 0 30px rgba(255,255,255,0.5), 0 0 60px rgba(255,255,255,0.3); }
            50% { text-shadow: 0 0 40px rgba(255,255,255,0.8), 0 0 80px rgba(255,255,255,0.5); }
        }
        
        .hero-subtitle {
            font-size: 1.3em;
            color: rgba(255,255,255,0.9);
            text-align: center;
            margin-bottom: 30px;
            position: relative;
            z-index: 1;
        }
        
        .hero-button {
            display: inline-block;
            padding: 15px 40px;
            background: white;
            color: #667eea;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 700;
            font-size: 1.1em;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            position: relative;
            z-index: 1;
        }
        
        .hero-button:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        }
        
        /* Feature cards with glow effect */
        .feature-card {
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            padding: 30px;
            border-radius: 15px;
            border: 2px solid transparent;
            background-clip: padding-box;
            position: relative;
            transition: all 0.3s ease;
            margin: 15px 0;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 15px;
            padding: 2px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 50px rgba(102, 126, 234, 0.4);
        }
        
        .feature-card:hover::before {
            opacity: 1;
        }
        
        .feature-icon {
            font-size: 3em;
            margin-bottom: 15px;
            filter: drop-shadow(0 0 10px rgba(102, 126, 234, 0.5));
        }
        
        .feature-title {
            font-size: 1.5em;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .feature-text {
            color: #666;
            line-height: 1.6;
        }
        
        /* Stats section */
        .stats-container {
            display: flex;
            justify-content: space-around;
            margin: 50px 0;
            flex-wrap: wrap;
        }
        
        .stat-box {
            text-align: center;
            padding: 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            color: white;
            min-width: 200px;
            margin: 10px;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        .stat-number {
            font-size: 2.5em;
            font-weight: 800;
            text-shadow: 0 0 20px rgba(255,255,255,0.5);
        }
        
        .stat-label {
            font-size: 1em;
            opacity: 0.9;
            margin-top: 10px;
        }
        
        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 60px 20px;
            border-radius: 20px;
            text-align: center;
            margin: 50px 0;
            box-shadow: 0 20px 60px rgba(245, 87, 108, 0.3);
        }
        
        .cta-title {
            font-size: 2.5em;
            font-weight: 800;
            color: white;
            margin-bottom: 20px;
            text-shadow: 0 0 20px rgba(255,255,255,0.3);
        }
        
        .cta-text {
            font-size: 1.2em;
            color: rgba(255,255,255,0.9);
            margin-bottom: 30px;
        }
        
        /* Footer Styles */
        .footer-container {
            background: linear-gradient(135deg, #2d3561 0%, #1f2544 100%);
            padding: 60px 40px 20px 40px;
            margin-top: 60px;
            color: white;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 40px;
            max-width: 1200px;
            margin: 0 auto 40px auto;
        }
        
        .footer-section h3 {
            font-size: 1.5em;
            margin-bottom: 20px;
            color: #667eea;
            font-weight: 700;
        }
        
        .footer-logo {
            font-size: 2em;
            font-weight: 800;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .footer-about {
            color: rgba(255,255,255,0.8);
            line-height: 1.8;
            font-size: 0.95em;
        }
        
        .quick-links {
            list-style: none;
            padding: 0;
        }
        
        .quick-links li {
            margin-bottom: 12px;
        }
        
        .quick-links a {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            transition: all 0.3s ease;
            display: inline-block;
            font-size: 0.95em;
        }
        
        .quick-links a:hover {
            color: #667eea;
            transform: translateX(5px);
        }
        
        .quick-links a:before {
            content: '→ ';
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .quick-links a:hover:before {
            opacity: 1;
        }
        
        .map-container {
            width: 100%;
            height: 200px;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            margin-bottom: 15px;
        }
        
        .map-container iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
        
        .address-text {
            color: rgba(255,255,255,0.8);
            font-size: 0.9em;
            line-height: 1.6;
        }
        
        .footer-bottom {
            border-top: 1px solid rgba(255,255,255,0.1);
            padding: 20px 0;
            text-align: center;
            color: rgba(255,255,255,0.6);
            font-size: 0.9em;
        }
        
        @media (max-width: 768px) {
            .footer-content {
                grid-template-columns: 1fr;
                gap: 30px;
            }
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">📈 Stock Sentiment Predictor</h1>
            <p class="hero-subtitle">Predict market sentiment with AI-powered analysis</p>
            <div style="text-align: center;">
                <a href="#get-started" class="hero-button">Get Started</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Stats Section
    st.markdown("""
        <div class="stats-container">
            <div class="stat-box">
                <div class="stat-number">95%</div>
                <div class="stat-label">Accuracy Rate</div>
            </div>
            <div class="stat-box" style="animation-delay: 0.5s;">
                <div class="stat-number">10K+</div>
                <div class="stat-label">Users Trust Us</div>
            </div>
            <div class="stat-box" style="animation-delay: 1s;">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Real-time Analysis</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <div class="feature-title">AI-Powered Analysis</div>
                <div class="feature-text">
                    Advanced machine learning algorithms analyze market sentiment from multiple sources
                    to give you accurate predictions.
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">Real-Time Updates</div>
                <div class="feature-text">
                    Get instant sentiment analysis with live data streaming from news,
                    social media, and financial reports.
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <div class="feature-title">High Accuracy</div>
                <div class="feature-text">
                    Our models are trained on millions of data points to deliver
                    reliable predictions you can trust.
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Second row of features
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">Detailed Insights</div>
                <div class="feature-text">
                    Comprehensive charts and visualizations help you understand
                    market trends at a glance.
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <div class="feature-title">Secure & Private</div>
                <div class="feature-text">
                    Your data is encrypted and protected with industry-standard
                    security measures.
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">💼</div>
                <div class="feature-title">Portfolio Tracking</div>
                <div class="feature-text">
                    Monitor multiple stocks and get personalized alerts
                    for your investment portfolio.
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # CTA Section
    st.markdown("""
        <div class="cta-section">
            <h2 class="cta-title">Ready to Make Smarter Investment Decisions?</h2>
            <p class="cta-text">Join thousands of investors who trust our AI-powered predictions</p>
            <a href="#start" class="hero-button">Start Predicting Now</a>
        </div>
    """, unsafe_allow_html=True)
    
    