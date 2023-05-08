from textwrap import fill
import pickle
import requests
import json
import streamlit as st
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder

html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">Car Price Prediction </h2>
</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)




html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App </h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)


age=st.sidebar.selectbox("What is the age of your car:",(0,1,2,3))
hp=st.sidebar.slider("What is the hp_kw of your car?", 40, 300, step=5)
km=st.sidebar.slider("What is the km of your car", 0,350000, step=1000)
gearing_type=st.sidebar.radio('Select gear type',('Automatic','Manual','Semi-automatic'))
car_model=st.sidebar.selectbox("Select model of your car", ('Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))



richard_transformer = pickle.load(open('transformer', 'rb'))


my_dict = {
    "age": age,
    "hp_kW": hp,
    "km": km,
    'Gearing_Type':gearing_type,
    "make_model": car_model
    
}

df = pd.DataFrame.from_dict([my_dict])


st.header("The configuration of your car is below")
st.table(df)

df2 = richard_transformer.transform(df)
df2 = pd.DataFrame(df2)
df2.to_csv('df2.csv', index=False, header=False)
with open('df2.csv', 'r') as f:
    payload = f.read().strip('\n')

url = 'https://kgxgp7z7f8.execute-api.us-east-1.amazonaws.com/beta'

st.subheader("Press predict if configuration is okay")

 
# Single Observation
event = {
  "data": payload
  
}



response = requests.post(url, data=json.dumps(event))
result = response.json()

if st.button("Predict"):
    st.success("The estimated price of your car is €{} ".format(int(result)))
    


