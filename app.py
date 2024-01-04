from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os


# Function to load OpenAI model and get response
def get_openAI_respnse(question):
    llm = OpenAI(model_name="text-davinci-003", temperature=0.5)
    response = llm(question)
    return response


## Intitialize Streamlit app
st.set_page_config(page_title = "Q&A Demo")
st.header("LangChain App")

input = st.text_input("Enter your question here", key="input")
response = get_openAI_respnse(input)

submit = st.button("Generate")


#If submit button is clicked
if submit:
    st.subheader("The response is")
    st.write(response)
