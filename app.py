import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="SA KenCho Bookmarks", page_icon="😁", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  

local_css("style/style.css")

# --- Load Assets ---
lottie_coding = load_lottieurl("https://lottie.host/e112f601-0e38-4d3f-a86d-8f2772fe122a/bTvKxU0CHo.json")
img_contact_form = Image.open("images/jordan.jpeg")

with st.container():
    st.subheader("This is my quick bookmarks collection for work, mainly focus on GenAI, Container and AWS :wave:")
    st.title("Quick Bookmarks for seasoned Solutions Architect from AWS")
    st.write("I am passionate about finding ways to learn Python coding, GenAI and AWS services")
    st.write("[Learn More >](https:/www.google.com)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("")
        st.write(
            """
            On my YouTube channel I am creating tutorials on Python, AWS and GenAI
            Feel free to subscribe and support me!
            """
        )
        st.write("[YouTube Channel >](https://youtube.com.hk)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate Lottie Animations Insider your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in your Streamlit application and animate your application
            """
        )
        st.markdown("[Watch Video...](XXXXXXXXXXXXXXXXXXXXXXXXXXXX)")


