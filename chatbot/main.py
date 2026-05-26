from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph import add_messages
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
load_dotenv()

#To define state
class ChatState(TypedDict):
    #BaseMessage can include huma,AI,System,Tool messages
    #reducer:add_messages,useful to append base messages
    messages:Annotated[list[BaseMessage],add_messages]

graph=StateGraph(ChatState)

llm=ChatGroq(
    model="llama-3.3-70b-versatile"
)



def chat_node(state: ChatState):
#take user query from state 
 messages=state['messages'] #extract from state
#send to llm 
 response=llm.invoke(messages)
#store response from llm in state
 return {'messages':[response]}

# add nodes
graph.add_node('chat_node',chat_node )

#add edges
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

#checkpointer for storing previous messages in memory
checkpointer=MemorySaver()
chatbot=graph.compile(checkpointer=checkpointer)
#print(chatbot.get_graph().draw_ascii())

initial_state={
    'messages':[HumanMessage(content='What is  the date')]
}
#print(chatbot.invoke(initial_state)['messages'][-1])

#defining threads for identifying users
thread_id ='1'
while True:
 user_message=input('Type here: ')
 print('User:',user_message)
 if user_message.strip().lower() in ['exit','quit','bye']:
   break
# configuration for specifying thread(user)
 config={'configurable':{'thread_id':thread_id}}  
 #everytime invoke is called state is re written and hence it acnt remember
 response=chatbot.invoke({'messages':[HumanMessage(content=user_message)]},config=config)

 print('AI:',response['messages'][-1].content) 

