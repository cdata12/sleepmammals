import base64
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

def add_bg_from_local(image_file, image_smartphone, bool):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    
    with open(image_smartphone, "rb") as image_smartphone:
        encoded_string_smartphone = base64.b64encode(image_smartphone.read())
    if bool:
        st.markdown(
            f"""
            <style>
            @media (min-width: 992px) {{
                .stApp {{
                    background-image: url(data:image/png;base64,{encoded_string.decode()});
                    background-size: cover;
                }}
            }}

            @media (max-width: 991px) {{
                .stApp {{
                    background-image: url(data:image/png;base64,{encoded_string_smartphone.decode()});
                    background-size: 100% 100%;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
                st.markdown(
            f"""
            <style>
            @media (min-width: 992px) {{
                .stApp {{
                    background-image: url(data:image/png;base64,{encoded_string.decode()});
                    background-size: cover;
                }}
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
#-----------------------------------------------------------

def webp_convert(original_image_path, optimized_image_path):
    # Chemin de l'image originale et de la nouvelle image
    
    # Ouvrir l'image originale
    image = Image.open(original_image_path)

    image.save(optimized_image_path, 'WEBP')

#-----------------------------------------------------------
def main():
    #hidden or visible
    st.markdown("""
        <style>
        #MainMenu {visibility: visible;}
        footer {visibility: visible;} 
        </style>
        """, unsafe_allow_html=True)

    #background
    original_image_path = "images/background_1_original.png"
    optimized_image_path = "images/background_1_try_2.webp"
    image_smartphone = "images/background_3_blank.webp"
    
    #webp_convert(original_image_path, optimized_image_path)
    
    add_bg_from_local(optimized_image_path, image_smartphone, True)
 
    col1, col2, col3 = st.columns([7,6,1])
    with col2:
        with st.container():
            for x in range(30):
                st.write("")

    result = col2.button("Enter")
    if (result==True):
        st.markdown(switch_page("project 💤"))
        
if __name__ == '__main__':
    st.set_page_config(
        page_title="Welcome to Sleep Mammals",
        page_icon="🦍",
        layout= "wide", #"wide", 
        initial_sidebar_state="collapsed"
    )
    main()