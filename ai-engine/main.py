import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import sys
# Environment variables (API Key) load karein
load_dotenv()

# LLaMA 3 model initialize karein Groq ke zariye (Coding ke liye best hai)
llm = ChatGroq(
    model="qwen/qwen3.8-27b", 
    temperature=0.2, 
    max_tokens=800
)

# Agent 1: Senior Backend Developer (Coder)
coder_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert Senior Backend Engineer. Write highly optimized, clean, and secure code for the user's problem. Provide the code and a brief explanation of your approach."),
    ("user", "{problem_statement}")
])
coder_chain = coder_prompt | llm | StrOutputParser()

# Agent 2: Strict QA Engineer (Reviewer)
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict Quality Assurance (QA) Engineer. Review the provided code. Find edge cases, security flaws, and performance bottlenecks. Outline your critique clearly and point out what the developer missed."),
    ("user", "Here is the code written by the backend developer:\n\n{code}\n\nPlease critique it rigorously.")
])
qa_chain = qa_prompt | llm | StrOutputParser()

def run_debate(problem):
    print("===================")
    print(f"📝 TASK: {problem}")
    print("===================\n")

    print("🧑‍💻 Agent 1 (Senior Dev) is writing code...\n")
    initial_code = coder_chain.invoke({"problem_statement": problem})
    print(initial_code)

    print("\n" + "="*40 + "\n")

    print("🕵️ Agent 2 (QA Expert) is reviewing...\n")
    review = qa_chain.invoke({"code": initial_code})
    print(review)
    print("\n====================================")

if __name__ == "__main__":
    # Ab yeh user ki input command line se lega
    if len(sys.argv) > 1:
        user_problem = sys.argv[1]
    else:
        user_problem = "Write a Python function to process a 10GB CSV file."
        
    run_debate(user_problem)