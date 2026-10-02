from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Using active fast & lightweight model on Groq
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3,
    max_tokens=500,
)

response = llm.invoke("Summarize quantum computing in 2 sentences.")
# print(response)
print(response.content)
