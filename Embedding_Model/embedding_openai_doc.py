from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv 

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

doc = [
    "Hii i am bishal Das",
    "This is testing of the embedding model",
    "and the embedding model from openai",
    "i cant use it because this is paid"
]
print(str(embedding.embed_documents(doc)))
