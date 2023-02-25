import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Use local CSS
#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#local_css('C:/Users/MDP/Pictures/Python Projects/web_pro_2222/styl/styl.css.txt')

# ---- LOAD ASSETS ----



# ---- HEADER SECTION ----
with st.container():
    im=Image.open('2222.jpg')
    st.image(im, caption='Sunrise by the mountains')
    st.title("deadline")

# ---- WHAT I Do----
with st.container():
    st.write("---")
    left_column,cnt_column,right_column= st.columns(3)
    with cnt_column:
        #st.header("deadline")
        st.write("##")
        st.header(
            """
           Our website is under construction
           Something big update is coming by our
           team.wait! we are launching soon with amazing updates!
            """
        )
        with cnt_column:
            with st.container():
                    st.write("---")
                    st.header("contact us")
                    st.write("##")
            if st.button("gmail"):
                with st.container():
                    st.write("---")
                    st.header("Get In Touch With Me!")
                    st.write("##")
                    contact_form = """
                    <form action="https://formsubmit.co/rosekrose12345@gmail.com" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="text" name="name" placeholder="Your name" required>
                        <input type="email" name="email" "Your email" placeholder="Your mail" required>
                        <textarea name="message" placeholder="Your message here" required></textarea>
                        <button type="submit">Send</button>
                    </form>
                    """
                    left_column,cnt_column,right_column = st.columns(3)
                    with cnt_column:
                        st.markdown(contact_form, unsafe_allow_html=True)
                    with right_column:
                        st.empty()
            else:
               st.write('')
            if st.button("github 🐱"):
                st.write("i don't have a github account")
            else:
               st.write('')
