from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content= "You are a very helpfull ai assistent like jarvis full loded with emotion. and talk in small words."),
]

while True:
    user_ip = input("User: ")
    chat_history.append(HumanMessage(content=user_ip))
    if user_ip == "exit":
        break
    model_responce = model.invoke(chat_history)
    chat_history.append(AIMessage(content=model_responce.content))
    print("AI: ", model_responce.content)

print(chat_history)