import requests
import json
import streamlit as st
import pandas as pd

# title of the sidebar
html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">Diabetes Prediction </h2>
</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

# title of the body
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App</h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)

# defining variables for user input
Pregnancies = st.sidebar.slider("What is the number of Pregnancies?", 0, 17, step=1)
Glucose = st.sidebar.slider("What is the glucose level?", 44, 199, step=1)
BloodPressure = st.sidebar.slider("What is the blood pressure?", 38, 122, step=1)
SkinThickness = st.sidebar.slider("What is the skin thickness?", 0, 63, step=1)
Insulin = st.sidebar.slider("What is the insulin level?", 0, 846, step=1)
BMI = st.sidebar.slider("What is the BMI?", 18, 68, step=1)
DiabetesPedigreeFunction = st.sidebar.slider("What is the DiabetesPedigreeFunction?", 0.05, 2.5, step=0.05)
Age = st.sidebar.slider("What is the Age?", 21, 81, step=1)


# converting user inputs into dictionary format
my_dict = {
    "Pregnancies": Pregnancies,
    "Glucose": Glucose,
    "BloodPressure": BloodPressure,
    'SkinThickness': SkinThickness,
    "Insulin": Insulin,
    "BMI": BMI,
    "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
    "Age": Age   
}

# converting user inputs from dictionary into dataframe
df = pd.DataFrame.from_dict([my_dict])

# displaying user inputs before prediction
st.header("The values you selected is below")
st.table(df)

# saving user inputs as csv file
df.to_csv('df.csv', index=False, header=False)

# reading and preparing the user inputs as payload for prediction
with open('df.csv', 'r') as f:
    payload = f.read().strip('\n')
 
# convert payload into event for lambda function
event = {
  "data": payload
}


# when API Gateway was activated, copy url address from API Gateway and paste here
url = 'https://cj79kg7mtl.execute-api.us-east-1.amazonaws.com/BETA'  

# prediction using API Gateway and Lambda function
response = requests.post(url, data=json.dumps(event))  # requests.post() method sends the data to lambda function via API Gateway.
result = response.json()  # Lambda function invokes endpoint and gets prediction result using data. Finally the response (prediction result) is sent app page via API Gateway.
result = round(result, 2)

# Display prediction result
st.subheader("Press predict if patient's inputs are okay")
if st.button("Predict"):
   st.success(f"The patient is diabetes with %{result} probabilities")

    


