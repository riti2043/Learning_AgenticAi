import streamlit as st
from langgraph_database_backend import chatbot,retrieve_all_threads
from langchain_core.messages import HumanMessage
import uuid
#to generate thread id (utitlity function 1)

def generate_thread_id():
 thread_id=uuid.uuid4()
 return thread_id

def reset_chat(): 
  thread_id=generate_thread_id()
  st.session_state['thread_id']=thread_id
  add_thread(st.session_state['thread_id'])
  st.session_state['message_history']=[]

def add_thread(thread_id):
  if thread_id not in st.session_state['chat_threads']:
    st.session_state['chat_threads'].append(thread_id)  

def load_conversation(thread_id):
  return chatbot.get_state(config={'configurable':{'thread_id':'thread_id'}})
   # Check if messages key exists in state values, return empty list if not
  return state.values.get('messages', [])
  

#SESSION SETUP
#st.session_state->dict->(its a dictionary )

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[] #key is message history and value is empty list
  
if 'thread_id' not in st.session_state:
  st.session_state['thread_id']=generate_thread_id()

if 'chat_threads'  not in st.session_state:
  st.session_state['chat_threads']=retrieve_all_threads()

add_thread(st.session_state['thread_id'])  

#sidebar UI
st.sidebar.title('Rune Chatbot')

if st.sidebar.button('New Chat'):
  reset_chat()

st.sidebar.header('My conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
  if st.sidebar.button(str(thread_id)):
    st.session_state['thread_id']=thread_id
    messages=load_conversation(thread_id)

    temp_messages=[]

    for message in messages:
      if isinstance(message,HumanMessage):
       role='user'
      else:
        role='assistant'
      temp_messages.append({'role':role,'content':message.content})  
    
    st.session_state['message_history']=temp_messages

# Main UI
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

    config={'configurable':{'thread_id':st.session_state['thread_id']}}
    
    #ai_message=reponse['messages'][-1].content
    with st.chat_message('assistant'):
      
      ai_message=st.write_stream(
        message_chunk.content for message_chunk,metadata in chatbot.stream(
   
        {'messages':[HumanMessage(content=user_input)]},
        config=config, 
        stream_mode='messages')
        
       )  

st.session_state['message_history'].append({'role':'assistant','content':user_input})          
