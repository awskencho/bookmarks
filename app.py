import streamlit as st


# Fine more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="SA KenCho Bookmarks", page_icon="😁", layout="wide")



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  

local_css("style/style.css")

# --- Load Assets ---
#img_contact_form = Image.open("images/jordan.jpeg")

with st.container():
    st.subheader("This is my quick bookmarks collection for work, mainly focus on GenAI, Container and AWS :wave:")
    st.title("Quick Bookmarks for seasoned Solutions Architect in AWS")
    st.write("I am passionate about finding ways to learn Python coding, GenAI and AWS services")
    st.write("[Learn More >](https:/www.google.com)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials on Python, AWS and GenAI
            Feel free to subscribe and support me!
            """
        )
        st.write("[YouTube Channel >](https://youtube.com.hk)")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    text1_column, text2_column, text3_column = st.columns((1, 2, 3))

    with text1_column:
        st.subheader("Bedrock bookmakers")
        st.write("[Claude Prompt Engineering Overview >](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)")
        st.write("[Bedrock Claude Chat Repo >](https://github.com/aws-samples/bedrock-claude-chat?tab=readme-ov-file)")

    with text2_column:
        st.subheader("Bedrock bookmakers")
        st.write("[Claude Prompt Engineering Overview >](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)")
        st.write("[Bedrock Claude Chat Repo >](https://github.com/aws-samples/bedrock-claude-chat?tab=readme-ov-file)")

    with text3_column:
        st.subheader("Bedrock bookmakers")
        st.write("[Claude Prompt Engineering Overview >](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)")
        st.write("[Bedrock Claude Chat Repo >](https://github.com/aws-samples/bedrock-claude-chat?tab=readme-ov-file)")



