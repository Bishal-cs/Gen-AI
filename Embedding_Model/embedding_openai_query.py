from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv 

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

print(str(embedding.embed_query("Hi this is the test of embedding of the query!")))
