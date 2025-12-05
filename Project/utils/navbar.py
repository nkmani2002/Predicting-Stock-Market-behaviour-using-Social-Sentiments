
import streamlit as st

def create_navbar():
    """Create enhanced animated navbar"""
    st.markdown('<div class="navbar-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 4])
    
    with col1:
        st.markdown('<div class="logo"><span class="logo-icon">📈</span> StockAI</div>', unsafe_allow_html=True)
    
    with col2:
        if st.session_state.logged_in:
            cols = st.columns([1, 1, 1, 1, 2])
        else:
            cols = st.columns([1, 1, 1, 1, 2])
        
        with cols[0]:
            if st.button("🏠 Home", key="nav_home", use_container_width=True):
                st.session_state.page = "Home"
                st.rerun()
        
        with cols[1]:
            if st.button("ℹ️ About", key="nav_about", use_container_width=True):
                st.session_state.page = "About"
                st.rerun()
        
        if not st.session_state.logged_in:
            with cols[2]:
                if st.button("🔐 Login", key="nav_login", use_container_width=True):
                    st.session_state.page = "Login"
                    st.rerun()
            
            with cols[3]:
                if st.button("📝 Register", key="nav_register", use_container_width=True):
                    st.session_state.page = "Register"
                    st.rerun()
        else:
            with cols[2]:
                if st.button("🔮 Predictor", key="nav_predictor", use_container_width=True):
                    st.session_state.page = "Predictor"
                    st.rerun()
            
            with cols[3]:
                st.markdown(f'<div style="color: white; text-align: center; padding: 0.75rem; font-weight: 600;">👤 {st.session_state.username}</div>', unsafe_allow_html=True)
            
            with cols[4]:
                if st.button("🚪 Logout", key="nav_logout", use_container_width=True):
                    st.session_state.logged_in = False
                    st.session_state.username = ""
                    st.session_state.page = "Home"
                    st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
