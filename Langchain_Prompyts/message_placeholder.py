from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

chat_template = ChatPromptTemplate([
    "system", "You are a multi talented ai agent that help to talk to human and handle the coustomer query.",
    MessagesPlaceholder(variable_name="chat_history"),
    "HumanMessage", "{user_input}"
])

chat_history = []

with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())


print(chat_history)

chat_template.invoke({"chat_history": chat_history, "user_input": "Hello"})