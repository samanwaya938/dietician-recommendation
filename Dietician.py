# from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Get the API token from the environment variable
# GROQ_API_TOKEN = os.getenv("GROQ_API_KEY")
OpenAI_API_TOKEN = os.getenv("AI_ML_API")

# Set the environment variable for the API token
# os.environ["GROQ_API_TOKEN"] = GROQ_API_TOKEN
os.environ["OPENAI_API_TOKEN"] = OpenAI_API_TOKEN

# Define the prompt template
template = """
You are a dietician and please answer based on the user question.

user question: Please give a {topic} for {gender} .

"""
# Corrected input variable to input_variables
prompt = PromptTemplate(template=template, input_variables=["topic", "gender"])

# Initialize the language model
llm = ChatOpenAI(base_url="https://api.aimlapi.com/v1", model="gpt-4o", api_key=OpenAI_API_TOKEN)

# Chain the prompt and the language model
chain = prompt | llm



# Define the Streamlit app
st.title("Dietician Chatbot")
topic = st.text_input("Enter the topic")
gender = st.selectbox("Select Gender",["Male", "Female"])
if st.button("Get Response"):
    response = chain.invoke({"topic": topic, "gender": gender})
    st.write(response.content)


