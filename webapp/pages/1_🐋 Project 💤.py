import sys
sys.path.append("pages")
sys.path.append("webapp")
import streamlit as st
from Mammals import add_bg_from_local
from streamlit_extras.switch_page_button import switch_page

# streamlit page setup
# sidebar : collapsed, auto or expanded
st.set_page_config(
    page_title="Welcome to Sleep Mammals",
    page_icon="🦍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#hidden or visible
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

optimized_image_path = "images/background_2_without.webp"
add_bg_from_local(optimized_image_path, optiiamgemized_image_path, False)
# Title and introduction
st.title('Sleep Mammals Project 💤')

st.write("""
## Unveiling the mysteries of mammalian slumber through machine learning

Welcome to the Sleep Mammals Project, an exploratory journey into the sleep patterns of mammals using the power of machine learning. Our project aims to predict total sleep time and dreaming phases across various species, integrating ecological and biological attributes into our models.

From understanding the relationship between body weight and sleep duration to exploring the impacts of predation risk on sleep patterns, our project delves deep into the factors that influence mammalian rest. With a dataset comprising 87 unique species, we embrace the challenge of uncovering the hidden patterns of sleep.

Through rigorous data analysis, innovative feature engineering, and the application of advanced machine learning algorithms, we strive to bring insights into the enigmatic world of sleep in the animal kingdom.

Join us as we navigate through the intricacies of machine learning to shine a light on the sleep habits of mammals, offering a glimpse into the natural world that is both enlightening and inspiring.
""")

#col1, col2, col3 = st.columns([3,4,3])
col1, col2, col3 = st.columns(3)

if col1.button("Let's go to the EDA"):
    st.markdown(switch_page("Exploratory Data Analysis 📈1️⃣"))
if col3.button("Meet the team 🧑🏽‍💻"):
    st.markdown(switch_page("About"))

st.write(" ▶️ You can collapse or expand the menu manually (minimized to the top left corner)")

