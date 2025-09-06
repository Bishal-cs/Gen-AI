# GenAI Learning Project: LangChain & Hugging Face

This project is a hands-on exploration of Generative AI using LangChain and Hugging Face models. It demonstrates how to build chatbots, work with embeddings, and create prompt-driven applications in Python.

## Features
- Chatbot interfaces using multiple providers (OpenAI, Anthropic, Google, Hugging Face API & Local)
- Embedding models for document and query processing
- Prompt engineering and template management
- Streamlit UI for interactive prompt testing

## Directory Structure
```
Langchain_Models/
│
├── Chat_Models/           # Chatbot model integrations
│   ├── chatmodel_openai.py
│   ├── chatmodel_anthropic.py
│   ├── chatmodel_google.py
│   ├── chatmodel_HF_API.py
│   └── chatmodel_HF_Local.py
│
├── Embedding_Model/       # Embedding model scripts
│   ├── embedding_openai_doc.py
│   ├── embedding_openai_query.py
│   ├── emvedding_HF_document.py
│   └── emvedding_HF_query.py
│
├── Langchain_Prompyts/    # Prompt engineering & UI
│   ├── Chatbot.py
│   ├── message.py
│   ├── prompt_generator.py
│   ├── prompts_ui.py      # Streamlit app for prompt testing
│   └── template.json      # Prompt template
│
├── LLMs_Demo/             # Demo scripts
│   └── 1_llms_demo.py
│
├── requirements.txt       # Python dependencies
└── test.py                # Test script
```

## Getting Started
1. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
2. **Set up environment variables**
   - Create a `.env` file with your API keys (OpenAI, Hugging Face, etc.)
3. **Run the Streamlit UI**
   ```powershell
   streamlit run Langchain_Prompyts/prompts_ui.py
   ```
4. **Explore and modify the code**
   - Try different models and prompts
   - Experiment with embeddings and chatbots

## Learning Goals
- Understand how to use LangChain for chaining LLMs and prompts
- Integrate Hugging Face models for both chat and embeddings
- Practice prompt engineering and template management
- Build interactive GenAI apps with Streamlit

## References
- [LangChain Documentation](https://python.langchain.com/docs/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Streamlit Documentation](https://docs.streamlit.io/)

---
Happy learning GenAI!
