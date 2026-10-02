from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq



load_dotenv()


LLM=ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3,
    

)
prompt = PromptTemplate(
    input_variables=["Age", "Height", "Weight", "Goals", "Gender"],
    template="""
    You are a Dietitian. 
    Your task is to provide the daily calorie requirement for a person based on their age: {Age}, gender: {Gender}, height: {Height}, weight: {Weight} and fitness goals: {Goals}.
    Explain nicely without using any bold formatting or double asterisks (**)
    Explain Shortly.
    """
)

formatted_prompt = prompt.invoke({
    "Age": "22",
    "Gender": "Male",
    "Height": "160 cm",
    "Weight": "58 kg",
    "Goals": "Weight Gain"
})

result = LLM.invoke(formatted_prompt)
print(result.content)

# Option 2 (Alternative LCEL pipe syntax):
# chain = prompt | LLM
# result = chain.invoke({
#     "Age": "25",
#     "Gender": "Male",
#     "Height": "175 cm",
#     "Weight": "70 kg",
#     "Goals": "Weight loss"
# }){}