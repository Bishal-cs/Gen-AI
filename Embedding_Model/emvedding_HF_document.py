from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Artificial Intelligence is transforming industries worldwide.",
    "Machine Learning is a subset of AI that learns from data.",
    "Climate change is causing rising sea levels and extreme weather.",
    "The history of the Internet started with ARPANET in the 1960s.",
    "Data Structures like arrays, stacks, and queues are fundamental in CS.",
    "Python is a versatile programming language popular for AI and web dev.",
    "Renewable energy sources like solar and wind are vital for sustainability.",
    "The human brain is an inspiration for artificial neural networks.",
    "Blockchain technology enables secure and decentralized transactions.",
    "Quantum computing could revolutionize problem-solving in the future.",
    "The Incremental Model is a software development approach where the system is designed, implemented, and tested in small parts (increments). Each increment adds functionality until the full system is complete."
]

query = input("What is the Incremental Model in Software Development? ")

document_embedding = embedding.embed_documents(documents)
query_embbed = embedding.embed_query(query)

score = cosine_similarity([query_embbed], document_embedding)[0]

index, scores = sorted(list(enumerate(score)), key = lambda x:x[1])[-1]

print(documents[index])
print("simmilarity between scores -> ",scores)