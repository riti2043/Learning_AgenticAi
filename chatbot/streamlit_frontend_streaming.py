import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage


#st.session_state->dict->(its a dictionary )

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[] #key is message history and value is empty list


#loading the conversation
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:
    #first add msg to msg history
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
      st.text(user_input)


    #ai_message=reponse['messages'][-1].content
   
    with st.chat_message('assistant'):
      ai_message=st.write_stream(
        message_chunk.content for message_chunk,metadata in chatbot.stream(
   
        {'messages':[HumanMessage(content=user_input)]},
        config={'configurable':{'thread_id':'thread-1'}}, 
        stream_mode='messages')
        
       )  

st.session_state['message_history'].append({'role':'assistant','content':user_input})          

