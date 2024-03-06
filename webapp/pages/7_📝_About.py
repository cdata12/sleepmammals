import streamlit as st

st.subheader("Source code")
col1, col2, col3 = st.columns([4,1,1])
with col1:
        st.info("👨‍💻 The application is open source and available on GitHub.")
with col2:
    i.badge(type="github", name="cdouadi/sleepmammals")
counter ="""visiteurs site: <a><img src="https://www.cutercounter.com/hits.php?id=hvuxnofxa&nd=6&style=1" border="0" alt="counter"></a>"""
col3.markdown(counter, unsafe_allow_html=True)

st.subheader("Roadmap 🛣️")
st.warning(" 18/11/2024 - Choice of Sleep Mammals project 👶🔥")
st.success(" du 19 au 20/01/2024 - Architecture design")
st.success(" du 21/01 au 03/03/2024 - Development and deployment")
st.error(" 03/03/2024 - Submission of the project 🚧") 

st.subheader("Team 🚀")
st.info("Made with 💖 by : Longyin, Mattéo, Limam & - ")
st.info("🪐 Special thanks to DSTI Team 👨‍🏫 : BECAVIN, HANNA")

# buy me a coffee link
col3, col4 = st.columns([6,1])
with col4:
    i.button(username="dchakib", floating=False, width=221)
