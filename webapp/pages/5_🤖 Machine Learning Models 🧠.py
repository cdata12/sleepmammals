import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import joblib

#-------------------------------------------------------------------------------------------------------

conservation_dico = {
    'Domesticated' : 1
    ,'Least Concern' : 2 
    ,'Near Threatened' : 3  
    ,'Lower Risk: Conservation Dependent' : 4 
    ,'Vulnerable' : 5 
    ,'Endangered' : 6 
    ,'Critically Endangered' : 7
}
inverse_dict = {v: k for k, v in conservation_dico.items()}

#-------------------------------------------------------------------------------------------------------

model_totalsleep = joblib.load('models/rf_totalsleep.joblib')
model_dreaming = joblib.load('models/gbr_dreaming.joblib')

#-------------------------------------------------------------------------------------------------------

if 'history' not in st.session_state or not isinstance(st.session_state['history'], pd.DataFrame):
    st.session_state['history'] = pd.DataFrame(columns=['Type', 'Conservation', 'LifeSpan', 'Gestation', 'Predation', 
                                                        'Exposure', 'Danger', 'Prediction'])

def add_prediction_to_history(species_name, prediction_type, inputs, prediction, bool):
    if(bool):
        new_data = {'Type': prediction_type, 'Conservation': inverse_dict.get(inputs[0], None), 'LifeSpan':inputs[1], 'Gestation': inputs[2], 
                'Predation': inputs[3], 'Exposure': inputs[4], 'Danger': inputs[5], 'Prediction': round(prediction[0],2)}
    else:
        new_data = {'Type': prediction_type, 'Gestation': inputs[0], 
                'Predation': inputs[1], 'Exposure': inputs[2], 'Danger': inputs[3], 'Prediction': round(prediction[0],2)}
    
    if (species_name==""):
        data_df = pd.DataFrame([new_data]) 
    else:
        data_df = pd.DataFrame([new_data],  index=[species_name]) 
    st.session_state['history'] = pd.concat([st.session_state['history'], data_df])

#-------------------------------------------------------------------------------------------------------
st.markdown("""You can use the built model (GradientBoostingRegressor) to predict the sleeping attributes
            TotalSleep and Dreaming from the general, ecological and biological attributes.
            Don't forget to name the species ⚠️""")
                
col1, col2 = st.columns(2)
with col1:
    st.subheader("TotalSleep")
    species_name = st.text_input("Name the species ", "")
    conservation = st.select_slider('Conservation status',
        options=['Domesticated', 'Least Concern', 'Near Threatened', 'Lower Risk: Conservation Dependent', 'Vulnerable', 'Endangered', 'Critically Endangered']
        ,value='Lower Risk: Conservation Dependent')

    lifeSpan = st.slider('LifeSpan (years)', 1, 150, 65)    
    gestation = st.slider('Gestation (days)', 0, 700, 235)
    predation = st.slider('Predation', 1, 5, 3)
    exposure = st.slider('Exposure', 1, 5, 2)
    danger = st.slider('Danger', 1, 5, 4)
    if st.button("PREDICT", disabled=species_name == ""):
        inputs = [conservation_dico[conservation], lifeSpan, gestation, predation, exposure, danger]
        prediction = model_totalsleep.predict([inputs])
        st.write(f'Prediction: {round(prediction[0],2)} of sleep, enveloped in tranquility.')
        add_prediction_to_history(species_name, 'Total Sleep', inputs, prediction, True)

#-------------------------------------------------------------------------------------------------------

with col2:
    st.subheader("Dreaming")
    #totalsleep = st.slider('TotalSleep (hours)', 0, 24, 1)
    species_name = st.text_input("Name the species", "")
    gestation_d = st.slider('Gestation (days) ', 0, 700, 313)
    predation_d = st.slider('Predation ', 1, 5, 2)
    exposure_d = st.slider('Exposure ', 1, 5, 3)
    danger_d = st.slider('Danger ', 1, 5, 2)
    if st.button("PREDICT ", disabled=species_name == ""):
        inputs = [gestation_d, predation_d, exposure_d, danger_d]
        prediction = model_dreaming.predict([inputs])
        st.write(f'Prediction: {round(prediction[0],2)} hours of lovely dreaming')
        add_prediction_to_history(species_name, 'Dreaming', inputs, prediction, False)

#-------------------------------------------------------------------------------------------------------

st.subheader("Prediction history")
st.dataframe(st.session_state['history'])

csv = st.session_state['history'].to_csv(index=False)

st.download_button(
    label="Download prediction history as CSV",
    data=csv,
    file_name='prediction_history.csv',
    mime='text/csv',
)

#-------------------------------------------------------------------------------------------------------
col1,col2,col3 = st.columns([1,11,1])
if col1.button("⬅️"):
    st.markdown(switch_page("Exploratory Data Analysis 📈3️⃣"))
if col3.button("➡️"):
    st.markdown(switch_page("Discover ML & mammals world 🌎"))

#-------------------------------------------------------------------------------------------------------