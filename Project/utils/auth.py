
import pandas as pd
import os
from datetime import datetime

USERS_FILE = "users.csv"

def initialize_users_file():
    """Initialize users file if it doesn't exist"""
    if not os.path.exists(USERS_FILE):
        pd.DataFrame(columns=['username', 'password', 'email', 'registration_date']).to_csv(USERS_FILE, index=False)

def register_user(username, password, email):
    """Register a new user"""
    initialize_users_file()
    users_df = pd.read_csv(USERS_FILE)
    
    if username in users_df['username'].values:
        return False, "Username already exists!"
    
    new_user = pd.DataFrame({
        'username': [username],
        'password': [password],
        'email': [email],
        'registration_date': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    })
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    users_df.to_csv(USERS_FILE, index=False)
    
    return True, "Registration successful!"

def authenticate_user(username, password):
    """Authenticate user credentials"""
    initialize_users_file()
    users_df = pd.read_csv(USERS_FILE)
    
    user = users_df[(users_df['username'] == username) & (users_df['password'] == password)]
    
    if not user.empty:
        return True, "Login successful!"
    else:
        return False, "Invalid username or password!"