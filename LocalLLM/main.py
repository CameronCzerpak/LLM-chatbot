from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# This file is based on Tech with Tim https://www.youtube.com/watch?v=d0o89z134CQ
# "Create a LOCAL Python AI Chatbot In Minutes Using Ollama" video
# 

# Notes: My python enivornemnt was already setup using Conda
# python3 -m venv chatbot was giving me issues on Windows
# Instead, I created main.py and created a virtual environemnt though
# vscode, rather than powershell.
# Future projects where I interact with the Openai API are less likely to encounter
# these issues since I'll run them on Mac/UNIX

# Create template for how LLM should respond
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

#LLM model
model = OllamaLLM(model="llama3")
# Prompt user inputs
prompt = ChatPromptTemplate.from_template(template)
# Chain model and prompt using langchain
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the local AI ChatBot! Type 'exit' to end session")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("LLM: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
# print(result)