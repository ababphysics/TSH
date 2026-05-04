import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables (e.g., OPENAI_API_KEY)
load_dotenv()

def initialize_rag():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'tsh_paper.txt')
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Please run scripts/extract_text.py first.")
        return None

    print("Loading documents and building vector store...")
    # 1. Load document
    loader = TextLoader(data_path, encoding='utf-8')
    docs = loader.load()

    # 2. Split document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # 3. Create vector store
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()

    # 4. Define prompt and chain
    system_prompt = (
        "You are an expert AI assistant specializing in the Thickness Structure Hypothesis (TSH) by Hirokazu Abe.\n"
        "Use the following pieces of retrieved context to answer the user's question.\n"
        "If you don't know the answer or if the information is not in the context, just say that you don't know.\n"
        "Keep the answer concise and highly accurate according to TSH principles.\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain

def chat():
    print("Initializing TSH RAG Chatbot...")
    rag_chain = initialize_rag()
    if not rag_chain:
        return

    print("\nInitialization complete! You can now ask questions about TSH.")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        try:
            response = rag_chain.invoke({"input": user_input})
            print(f"\nAI: {response['answer']}\n")
        except Exception as e:
            print(f"\nError: {e}\n(Did you set your OPENAI_API_KEY?)")

if __name__ == "__main__":
    chat()
