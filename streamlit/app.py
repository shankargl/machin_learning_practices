from streamlit import file_uploader
from streamlit import sidebar
import numpy as np
import streamlit as st
import pandas as pd 

st.title("demo app")   #title
name = st.text_input("enter your name") #text input
if name:
    st.write(f"hello my dear {name}!") #display


#using slider

age=st.slider("enter your age",min_value=18,max_value=100,value=25)
if age:
    st.write(f"your age is {age}")


#using selectbox
options=["python","c++","java","c","java script"]
choice=st.selectbox("choose your favorite language",options)
if choice:
    st.write(f"you choose {choice}")



#using checkbox
if st.checkbox("show dataframe"):
    st.write(df)
else:
    st.write("dataframe is not shown")
    

#using radio button
sex=st.radio("choose your gender",["male","female"])
if sex=="male":
    st.write("you are male")
else:
    st.write("you are female")
#creating dataframe
df=pd.DataFrame({
    'first':[1,2,3,4,5,6],
    "second":[9,8,7,6,5,4],
    "third":[100,200,300,400,500,600]
})  

st.table(df) #display static table
st.write(df) #display dataframe

data=pd.DataFrame(
    np.random.randn(20,3),
    columns=["col1","col2","col3"]

)
st.write(data)
st.line_chart(data) #display line chart
st.area_chart(data) #display area chart
st.bar_chart(data) #display bar chart   


#with sidebar/
with st.sidebar:
    st.write("hello my dear shankar") 
    file_uploader=st.file_uploader("enter a pdf file",type=["pdf","txt"]   )

    if file_uploader is not None:
        st.write(file_uploader)    
