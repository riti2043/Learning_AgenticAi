import streamlit as st

st.title("Hello")
st.subheader("By streamlit")
st.text("Welcome")
st.write("Choose")
lang=st.selectbox("Your fav.:",["C++","Java","Python"])
st.success("Selected")


#Widgets
if st.button("make"):
    st.success("Selected")
    pass

done=st.checkbox("done")    



if done:
    st.write("Done done")

type=st.radio("pick:",["stdio","sckit","console"])
num=st.selectbox("Your fav.:",["1","2","3"])

slider_box=st.slider("choices",0,5,3)

#for uncontrolled input
st.number_input("how much",min_value=1,max_value=10,step=1)
name=st.text_input("Name?")

if name:
    st.write(f"hello there! {name}")


dob=st.date_input("Select dob")
st.write(f"your dob {dob}")

#for dashboards