import streamlit as st

#dashboards , apis etc

st.title("Chai Taste Poll")

col1,col2=st.columns(2)
with col1:
    st.header("Masala Chai")
    vote1=st.button("vote masal chai")

with col2:
    st.header("Adrak Chai")
    vote2=st.button("vote adrak chai")

if vote1:
    st.success("Thanks for voting 1")
elif vote2:
    st.success("Thanks for voting 2")

name = st.sidebar.text_input("enter your name")   
choice=st.sidebar.selectbox("choices",["1","2","3"]
) 

with st.expander("show instructions"):
    st.write("""
    1.do this
    2.do that
    3.do this
    """)

#markdown

st.markdown('###Welcome')
st.markdown('> Blockquote')

#pandas
