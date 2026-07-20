import streamlit as st
import bcrypt

st.title("Secure Authentication System 🔒")
st.write("A safe way to hash and verify user passwords.")

if 'users_db' not in st.session_state:
    st.session_state.users_db = {}

tab1, tab2 = st.tabs(["Sign Up", "Login"])

with tab1:
    st.subheader("Create a New Account")
    new_user = st.text_input("Choose a Username", key="reg_user")
    new_password = st.text_input("Choose a Password", type="password", key="reg_pass")
    
    if st.button("Register"):
        if new_user in st.session_state.users_db:
            st.warning("Username already exists! Try another.")
        elif len(new_password) < 4:
            st.error("Password is too short!")
        else:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), salt)
          
            st.session_state.users_db[new_user] = hashed_password
            st.success("Account created securely!")
with tab2:
    st.subheader("Login to your Account")
    login_user = st.text_input("Username", key="log_user")
    login_password = st.text_input("Password", type="password", key="log_pass")
    
    if st.button("Login"):
        if login_user in st.session_state.users_db:
            stored_hash = st.session_state.users_db[login_user]
          
            if bcrypt.checkpw(login_password.encode('utf-8'), stored_hash):
                st.success(f"Welcome back, {login_user}! Authentication successful. 🎉")
                st.balloons()
            else:
                st.error("Incorrect password. Access Denied.")
        else:
            st.error("User not found.")


st.divider()
st.subheader("Backend Database View (For Educational Purposes)")
st.write("Notice how the passwords are turned into unreadable hashes:")
st.write(st.session_state.users_db)
