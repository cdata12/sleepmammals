import streamlit as st
from streamlit_extras.switch_page_button import switch_page

col3, col4 = st.columns(2)
with col3:
    st.subheader("Machine Learning :video_camera:")
    st.text(" What Is Machine Learning?")
    with st.expander("⏯️ Introduction To Machine Learning", expanded=True):
        st.video("https://www.youtube.com/watch?v=ukzFI9rgwfU&ab_channel=Simplilearn")

    with st.expander("⏯️ How to select the best algorithm in Data Science?"):
        st.video("https://www.youtube.com/watch?v=MQB36sEX_og&ab_channel=DataScienceTechInstitute")

with col4:
    st.subheader("Mammals :video_camera:")
    st.text("It's time to learn more about mammals")
    with st.expander("⏯️ Importance of the science of classifying : Taxonomy", expanded=True):
        st.video("https://www.youtube.com/watch?v=F38BmgPcZ_I&ab_channel=CrashCourse")
    with st.expander("⏯️ How the Animal Kingdom Sleeps"):
        st.video("https://www.youtube.com/watch?v=A-JtybJbVbA&ab_channel=TheAtlantic")
    
st.divider()

st.subheader("Example of taxonomy : American black bear 🧸")
col1 = st.columns(1)
st.image('images/taxonomy_example.webp', caption='Classification  of the American black bear and outlines the levels from species to domain.')

col1,col2,col3 = st.columns([1,11,1])
if col1.button("⬅️"):
    st.markdown(switch_page("Machine Learning Models 🧠"))
if col3.button("➡️"):
    st.markdown(switch_page("About"))