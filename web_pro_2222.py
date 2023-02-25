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
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css('C:/Users/MDP/Pictures/Python Projects/web_pro_2222/styl/styl.css.txt')

animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)


# ---- LOAD ASSETS ----



# ---- HEADER SECTION ----
with st.container():
    left_column,cnt_column,right_column= st.columns(3)
    with cnt_column:
        im=Image.open('2222.jpg')
        st.image(im, caption='Sunrise by the mountains')
        st.markdown("""
        <style>
        .big-font {
            font-size:40px;
        }
        </style>""",unsafe_allow_html=True)
        st.markdown('<p class="big-font">Deadline</p>', unsafe_allow_html=True)
        #st.write("Deadline")

# ---- WHAT I Do----
with st.container():
    st.write("---")
    left_column,cnt_column,right_column= st.columns(3)
    with cnt_column:
        #st.header("deadline")
        st.write("##")
        #st.set_page_config(layout="wide")
        st.write("Our website is under construction.Something big update is coming by our team. Wait we are launching with amazing updates!")
        with cnt_column:
            with st.container():
                st.write("---")
                st.markdown("""
                <style>
                .big-font {
                    font-size:28px;
                }
                </style>""",unsafe_allow_html=True)
                st.markdown('<p class="big-font">Contact us</p>', unsafe_allow_html=True)
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
                lft_column,cnt_column,cntt_column,right_column = st.columns(4)
                with cnt_column:
                    st.markdown(contact_form, unsafe_allow_html=True)
                with lft_column:
                    st.empty()
