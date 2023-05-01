import streamlit as st

# Text/Title
st.title('Streamlit tutorial. Btw, do not forget to start the py file import streamlit as st')

# Header/Subheader

st.header("This is just a header to see. use st.header() for a header")
st.subheader("and this is a subheader. use st.subheader() for a subheader")
# after cmmnd+s it displays it automatically

# text
st.text("I have to confess that streamlit is really amazing and impressive. \nI am looking forward to see using it for my future projects. \nBtw, use st.text() for a text")

# markdown
st.markdown("### markdowns start with 3# and have bigger font")

# Error/colorful text
st.success("Succesful")
st.info("this is information")
st.warning("this is just a warning")
st.error("Error! Check your entry!")

st.exception("Name Error ('name three not defined')")

# st.help() info about any python function
st.help(len)

# text writing : st.write
st.write("This is written with st.write()")
st.text("This is written with st.text()")
st.write(range(0,20,3))
st.text(range(0,20,30))

# images
st.image("image.jpeg")
st.image("image.jpeg", width = 600, caption = "An Ottoman worker")

# Videos
# vid_file = # open("vid_in_same_directory.mp4", "rb").read()
# vid_bytes = vid_file.read()
# st.video(vid_file)

# Audio
# audio_file = # open("audio_in_same_directory.mp3", "rb").read()
# st.audio(audio_file)

# Widget
# st.checkbox()
if st.checkbox("Show/Hide"):
    st.text("If you click, this will be displayed")

# radio buttons: st.radio()
status = st.radio("What is your status", ("Active", "Inactive"))

if status == "Active":
    st.success("You are Active")
else:
    st.warning("You are inactive, activate!")

# st.selectbox()
edu = st.selectbox("this is st.selectbox(): What is your education level:", ["Bachelor", "Master", "Ph.D."])
st.write("Your education level is", edu)

#st.multiselect()
cities = st.multiselect("this is st.multiselect(): Which cities you have been in:", ("Barcelona", "Istanbul", "Paris", "London", "Amsterdam"))
st.write("You have visited", len(cities), "cities")

# st.slider()

st.slider("What is your level", 1,10) # text and range

# st.button()

st.button("any button here")

# activate a button
if st.button("Source"):
    st.text("Axel Springer, The Last Century, Berlin: 2012")
    
# st.text_input()

name = st.text_input("Your first name", "Type here..")

if st.button("Submit"):
    result = "Great job", name.title()
    st.success(result)
    
# st.text_area

message = st.text_area("Enter your message", "Type Here..")

if st.button("message"):
    result = message.title()
    st.success(result)
    
# st.date_input()
import datetime
today = st.date_input("Today is", datetime.datetime.now())

# st.time_input()

the_time = st.time_input("The time is", datetime.time())

# st.jason() : displayin json
st.text("Displaying JSON")
st.json({"name": "McCluskey", "education":"PhD", "department": "IT"})

# st.code(): displaying raw code
st.text("Displayingg raw code")
st.code("import pandas as pd")

# displaying raw code with comments and others: 
with st.echo():
    # This is your comment
    import numpy as np
    def add_function(x,y):
        return np.sqrt(x+y)
    
# Progress bar: st.progress()
import time
my_bar = st.progress(5)
for p in range(10):
    my_bar.progress(p+1)

# st.balloons()
# st.balloons()

# st.sidebar(): SIDEBARS
st.sidebar.header("About")
st.sidebar.write("This is my first sidebar explanation")

