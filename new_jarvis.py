import requests
from streamlit_lottie import st_lottie
import streamlit as st
import io
import pandas as pd
import cv2
import numpy as np
import streamlit as st
#from streamlit import SessionState
#from session_state import SessionState
import datetime
#from datetime import datetime, timedelta
import hashlib
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import io
import base64
from flask import Flask, jsonify, request, session
#from flask_session import Session
import traceback
import deta
import dask.dataframe as dd
import json
import time
from deta import Deta
import requests
from streamlit_lottie import st_lottie
import streamlit as st
import smtplib
from urllib.parse import quote_plus
import string
import traceback
import deta
import database as db
import dask.dataframe as dd
from deta import Deta
# Define the user database
#@st.cache

#user authentication
def get_auth_db():
    project_key = "d08nkg8ruxp_ZYSZ2Xgyhx3TP9gRQ3mz7N1haKmh1ndJ"
    db = deta.Deta(project_key).Base("auth_one")
    return db
users = db.fetch_all_users()

'''usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
hashed_passwords = [user["password"] for user in users]
usernames = {user["key"]: user["key"] for user in users}
names = {user["key"]: user["name"] for user in users}
hashed_passwords = {user["key"]: user["password"] for user in users}

# Hash the passwords
for key, value in hashed_passwords.items():
    hashed_passwords[key] = hashlib.sha256(value.encode()).hexdigest()

# Initialize the authenticator
authenticator = stauth.Authenticate(
    name="sales_dashboard",
    usernames=usernames,
    hashed_passwords=hashed_passwords,
    secret_key="abcdef",
    cookie_expiry_days=1
)

# Get user credentials and authenticate
name, authentication_status, username = authenticator.login("Login", "main")
#name, authentication_status, username = authenticator.login("Login", "main")'''
users = {
    "user1": {
        "name": "John Smith",
        "password": "password1"
    },
    "user2": {
        "name": "Jane Doe",
        "password": "password2"
    }
}

# Define a function to hash the passwords


# Check authentication status
'''if authentication_status == False:
    st.error("Username/password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status:
    st.success(f"Welcome, {name}!")'''
def get_db():
    project_key = "d08nkg8ruxp_ZYSZ2Xgyhx3TP9gRQ3mz7N1haKmh1ndJ"
    db = deta.Deta(project_key).Base("employees")
    return db
def load_data():
    try:
        '''project_key = "d08nkg8ruxp_ZYSZ2Xgyhx3TP9gRQ3mz7N1haKmh1ndJ"
            db = deta.Deta(project_key).Base("employees")'''
        db = get_db()
        records = db.fetch()
        df = pd.DataFrame(records)
        df['image_bytes'] = df['ima'].apply(lambda x: None if x is None else bytes(x))
        ddf = dd.from_pandas(df, npartitions=4)
        st.dataframe(df)  # display the data as a dataframe\
        #    return ddf
    except:
        traceback.print_exc()
def customers():
    st.title('Customer Management System')
    # Load the customer data
    db = get_db()
    customer_data = db.get('devi')  # load_data()
    st.subheader('Customer data')
    customer_df = pd.DataFrame.from_records(customer_data, index=['customer_id'])
    st.subheader('Add new customer')
    customer_acc_no = st.text_input('Customer Ac.No')
    customer_name = st.text_input('Customer name')
    cust_dob = st.text_input('Customer dob')
    cust_mob_one = st.text_input('Customer Mob One')
    cust_mob_two = st.text_input('Customer Mob Two')
    cust_mail = st.text_input('Customer mail')
    customer_id = st.text_input('Customer ID')
    customer_gender = st.selectbox('Customer Gender', ['Male', 'Female', 'Other'])
    customer_department = st.text_input('Customer address')
    cust_pan_no = st.text_input('Customer PAN.no')
    # Add an image uploader
    st.subheader('Upload customer image')
    uploaded_files = st.file_uploader('Choose images', type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)
    if st.button('Add customer'):
        try:
            for uploaded_file in uploaded_files:
                if uploaded_file is not None:
                    # Read the uploaded image with OpenCV
                    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
                    # Convert the image data into binary format
                    img_data = cv2.imencode('.jpg', img)[1].tostring()
                    img_data = io.BytesIO()
                    np.save(img_data, img)
                    img_data.seek(0)
                    st.write("good")
                else:
                    img_data = None
                db = get_db()
                data = {"name": customer_name, "id": customer_id, "gender": customer_gender,
                        "department": customer_department, 'image': base64.b64encode(img_data.read()).decode(),
                        "acc_num": customer_acc_no, "dob": cust_dob, "mob_one": cust_mob_one,
                        "mob_two": cust_mob_two,
                        "pan_num": cust_pan_no, "mail": cust_mail}
                key = data.pop('name')
                db.put(data, key=key)
                st.success('New customer added successfully')
        except Exception as e:
            st.error(f"Error occurred: {e}")
    # Allow the user to search for customer
    customer_dataaa = db.get('devi')
    customer_dattt = pd.DataFrame.from_records(customer_dataaa, index=['customer_id'])
    st.subheader('Search customer')
    search_term = st.text_input('Enter search term')
    search_by = st.selectbox('Search by', ['Customer name', 'Customer ID', 'Customer Ac.No'])
    search_results = None
    if st.button('Search'):
        if search_by == 'Customer name':
            search_results = customer_dattt[customer_df['key'].str.contains(search_term, case=False)]
        elif search_by == 'Customer ID':
            search_results = customer_dattt[customer_df['id'].str.contains(search_term, case=False)]
        elif search_by == 'Customer Ac.No':
            search_results = customer_dattt[customer_df['acc_num'].str.contains(search_term, case=False)]
    if search_results is not None:
        st.write(f"Search results for {search_by}:")
        st.dataframe(search_results)

    cust_del = st.text_input('Customer name', key='cust')
    if st.button('delete customer'):
        try:
            db = get_db()
            # Use Deta's API to delete an item
            deleted_item = db.delete(cust_del)
            # return deleted_item
        except Exception as e:
            st.error(f"Error occurred: {e}")
    # customer_names = [customer['name'] for customer in customer_data]
    st.subheader('Edit customer')
    db = get_db()
    customer_data = db.fetch().items
    customer_list = [item for item in customer_data]
    df = pd.DataFrame(customer_list)
    cust_list = df['key'].tolist()
    selected_customer = st.selectbox('Select a customer to edit', cust_list)
    customer_row = df[df['key'] == selected_customer].iloc[0]
    customer_acc_no = st.text_input('Customer Ac.No', value=customer_row['acc_num'])
    customer_name = st.text_input('Customer name', value=customer_row['key'])
    cust_dob = st.text_input('Customer dob', value=customer_row['dob'])
    cust_mob_one = st.text_input('Customer Mob One', value=customer_row['mob_one'])
    cust_mob_two = st.text_input('Customer Mob Two', value=customer_row['mob_two'])
    cust_mail = st.text_input('Customer mail', value=customer_row['mail'])
    customer_id = st.text_input('Customer ID', value=customer_row['id'])
    customer_gender = st.selectbox('Customer Gender', ['Male', 'Female', 'Other'], index=0, key='gender')
    customer_department = st.text_input('Customer address', value=customer_row['department'])
    cust_pan_num = st.text_input('Customer PAN.no', key='pan_input', value=customer_row['pan_num'])
    st.subheader('Upload customer image')
    # key = str(time.time())
    key = 'oit'
    uploaded_files = st.file_uploader('Choose images', key=key, type=['jpg', 'jpeg', 'png'],
                                      accept_multiple_files=True)
    if st.button('Edit customer'):
        try:
            for uploaded_file in uploaded_files:
                if uploaded_file is not None:
                    # Read the uploaded image with OpenCV
                    img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
                    # Convert the image data into binary format
                    img_data = cv2.imencode('.jpg', img)[1].tostring()
                    img_data = io.BytesIO()
                    np.save(img_data, img)
                    img_data.seek(0)
                    st.write("good")
                else:
                    img_data = None
                db = get_db()
                data = {"name": customer_name, "id": customer_id, "gender": customer_gender,
                        "department": customer_department, 'image': base64.b64encode(img_data.read()).decode(),
                        "acc_num": customer_acc_no, "dob": cust_dob, "mob_one": cust_mob_one,
                        "mob_two": cust_mob_two,
                        "pan_num": cust_pan_no, "mail": cust_mail}
                key = data.pop('name')
                db.update(data, key=key)
                st.success('New customer added successfully')
        except Exception as e:
            st.error(f"Error occurred: {e}")
def home():
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
        lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_9w3rjspv.json")
        with st.container():
            st.write("---")
            left_column, centrtt_column, right_column = st.columns(3)
            with left_column:
                st.write("##")
            with centrtt_column:
                st_lottie(lottie_coding, height=300, key="coding")
                st.title("This is Ravindhar's insurance management system made by MD Solutions")
                st.header("MD Solutions")
                st.subheader("Welcome to our App!")
                # image = cv2.imread("C:/Users/MDP/Pictures/Python Projects/sql app/md ima.JPG")
                # st.image(image, caption='image caption')
def life_insurance():
    st.title('Customer Management System')
    # Load the customer data
    db = get_db()
    customer_data = db.get('devi')  # load_data()
    # return customer_data.items
    # st.dataframe(customer_data)
    # Display the customer data
    st.subheader('Customer data')
    customer_df = pd.DataFrame.from_records(customer_data, index=['customer_id'])
    # customer_df = pd.DataFrame.from_records(customer_data)
    st.dataframe(customer_df)
    '''if customer_data is not None:
        for index, row in customer_data.iterrows():
            st.write(f"**Name:** {row['name']}, **ID:** {row['id']}, **Gender:** {row['gender']}, **Department:** {row['department']}")
            # Check if the image data is not None
            if row['image_bytes'] is not None:
                st.image(row['image_bytes'])'''
    st.subheader('Add new customer')

    customer_acc_no = st.text_input('Customer Ac.No')
    customer_name = st.text_input('Customer name')
    cust_dob = st.text_input('Customer dob')
    cust_mob_one = st.text_input('Customer Mob One')
    cust_mob_two = st.text_input('Customer Mob Two')
    cust_mail = st.text_input('Customer mail')
    customer_id = st.text_input('Customer ID')
    customer_gender = st.selectbox('Customer Gender', ['Male', 'Female', 'Other'], index=0, key='gender')
    customer_department = st.text_input('Customer address')
    cust_pan_no = st.text_input('Customer PAN.no', key='pan_input')
    customer_gender = st.selectbox('Add policy', ['life insurance', 'health insuance', 'vehicle insurance'],
                                   index=0,
                                   key='policy')
    customer_policy_type = st.selectbox('Add policy type', ['quarterly', 'half yearly', 'annually'], index=0,
                                        key='policy type')
    # add data
    policy_name = st.selectbox('Add company name',
                               ['hdfc', 'icici', 'bajaj', 'tata', 'aditya birla', 'max', 'others'],
                               index=0, key='policy name')
    if policy_name == 'others':
        policy_others = st.text_input('Enter company name')
    else:
        policy_others = None
        policy_start_date = st.text_input('policy start date')
        policy_end__date = st.text_input('policy end date')
        policy_premium_date = st.text_input('premium pay term')
        policy_defermation_passed = st.text_input('defermation passed')
        policy_premium_mode = st.selectbox('premium mode', ['quarterly', 'halfly', 'monthly', 'yearly'], index=0,
                                           key='policy_term')
        # add data
        # Add an image uploader
        st.subheader('Upload customer image')
        # key = str(time.time())
        uploaded_files = st.file_uploader('Choose images', type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)
        if st.button('Add customer'):
            try:
                for uploaded_file in uploaded_files:
                    if uploaded_file is not None:
                        # Read the uploaded image with OpenCV
                        img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
                        # Convert the image data into binary format
                        img_data = cv2.imencode('.jpg', img)[1].tostring()
                        img_data = io.BytesIO()
                        np.save(img_data, img)
                        img_data.seek(0)
                        st.write("good")
                    else:
                        img_data = None
                    db = get_db()
                    data = {"name": customer_name, "id": customer_id, "gender": customer_gender,
                            "department": customer_department, 'image': base64.b64encode(img_data.read()).decode(),
                            "acc_num": customer_acc_no, "dob": cust_dob, "mob_one": cust_mob_one,
                            "mob_two": cust_mob_two, "pan_num": cust_pan_no, "mail": cust_mail,
                            'policy_name': policy_name, 'policy_start_date': policy_start_date,
                            'policy_end__date': policy_end__date, 'policy_premium_date': policy_premium_date,
                            ' policy_defermation_passed': policy_defermation_passed,
                            'policy_premium_mode': policy_premium_mode}
                    key = data.pop('name')
                    db.put(data, key=key)
                    st.success('New customer added successfully')
            except Exception as e:
                st.error(f"Error occurred: {e}")


def app():
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    # Hash the passwords in the user database
    hashed_users = {}
    for user, data in users.items():
        hashed_users[user] = {
            "name": data["name"],
            "password": hash_password(data["password"])
            }
    def nav():
        # if not login_form():
        #   return
        st.sidebar.title('Navigation')
        pages = {
            'Home': home,
            'Customers': customers,
            'life insurance': life_insurance,
        }
        selection = st.sidebar.radio("Go to", list(pages.keys()))
        # Display the selected page with the corresponding function
        pages[selection]()
    '''def login():
        current_time = int(time.time())
        # Create the Streamlit authenticator
        authenticator = stauth.Authenticator(
            hashed_users,
            "Login",
            "My App",
            cookie_duration_sec=86400,
            cookie_csrf_enabled=True
        )
        # Try to authenticate the user
        with st.spinner("Please wait..."):
            name, status, _ = authenticator.authenticate()
        # Display the appropriate content based on authentication statu
        if status == stauth.AuthenticationStatus.OK:
            st.success(f"Welcome, {name}!")
        elif status == stauth.AuthenticationStatus.NOT_AUTHENTICATED:
            st.warning("Please log in to access this app.")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
        # Handle login submission
        if st.button("Log in"):
            hashed_password = hash_password(password)
            status = authenticator.login(username, hashed_password)
            if status == stauth.AuthenticationStatus.OK:
                st.success(f"Welcome, {username}!")
            elif status == stauth.AuthenticationStatus.ERROR:
                st.error("Invalid username/password combination.")
            else:
                st.error("Unknown authentication status.")'''
    '''authenticator = StAuthenticator(
        key="my_app",
        title="My App",
        login_button_text="Log In",
        username_label="Username",
        password_label="Password",
        on_login=on_login,
        cookie_max_age=8640,
        )
    def on_login(username, password):
        if username == "my_username" and password == "my_password":
            authenticator.login_success(username)
        else:
            authenticator.login_failure("Invalid username or password")
    def login():
        if not authenticator.logged_in:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Log In"):
                on_login(username, password)
        else:
            st.success("You are logged in.")
    cookie_expiration_time = timedelta(days=1)
    class CustomAuthenticator(stauth.Authenticator):
        def authenticate(self, username, password):
            if username == "admin" and password == "1234":
                # Set the cookie with the username and expiration time
                expiration_time = datetime.now() + cookie_expiration_time
                st.session_state.username = username
                st.session_state.expiration_time = expiration_time
                return True
            return False
        def logout(self):
            # Clear the session state variables
            st.session_state.username = None
            st.session_state.expiration_time = None
        def is_authenticated(self):
            # Check if the username is present in the session state
            if "username" in st.session_state:
                username = st.session_state.username
                expiration_time = st.session_state.expiration_time
                # Check if the cookie is expired
                if datetime.now() < expiration_time:
                    return True
                else:
                    # Clear the session state variables if the cookie is expired
                    self.logout()
            return False
    authenticator = CustomAuthenticator()
    st.set_authenticator(authenticator)
    if not st.is_authenticated():
        st.write("Please log in to access this page.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Log in"):
            if authenticator.authenticate(username, password):
                st.success("Logged in.")
            else:
                st.error("Invalid username or password.")
    else:
        st.write("You are logged in as:", st.session_state.username)
        if st.button("Log out"):
            authenticator.logout()
            st.success("Logged out.")'''
    '''def login():
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if username=="pparker" and password=="abc123":
            st.success(f"hello {username}")
        else:
            st.error("Invalid username/password combination.")'''
    def login():
        state = st.session_state
        expire_date = datetime.datetime.now() + datetime.timedelta(days=1)
        if not hasattr(state, "logged_in"):
            state.logged_in = False
        if state.logged_in:
            st.success("You are already logged in!")
        else:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if username == "pparker" and password == "abc123":
                st.success(f"Hello {username}")
                state.logged_in = True
                st.set_cookie("login_status", "true", expires=expire_date)
            else:
                st.error("Invalid username/password combination.")
    login()
if __name__ == '__main__':
    app()
