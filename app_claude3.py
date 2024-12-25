# A simple script to test claude 3 on aws bedrock to host in streamlit
import boto3
import json
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_aws import ChatBedrock
import os
import streamlit as st

os.environ["aws-profile"] = "aws-toolkit-local"
region = "us-east-1" # for example, "us-east-1" or "us-west-2"

AWS_ACCESS_KEY_ID = st.secrets["aws-toolkit-local"]["AWS_ACCESS_KEY_ID"] #get secrets from streamlit 
AWS_SECRET_ACCESS_KEY = st.secrets["aws-toolkit-local"]["AWS_SECRET_ACCESS_KEY"] #get secrets from streamlit

bedrock_runtime = boto3.client(
    aws_access_key_id=AWS_ACCESS_KEY_ID, #for streamlit live 
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY, #for streamlit live 
    service_name="bedrock-runtime",
    region_name=region,
)

model_id = "anthropic.claude-3-haiku-20240307-v1:0"

model_kwargs =  { 
    "max_tokens": 512,
    "temperature": 0.9,
}

claude_3_client = ChatBedrock(
    client=bedrock_runtime,
    model_id=model_id,
    model_kwargs=model_kwargs,
)

def my_chatbot(language, prompt_text):
  
    prompt = ChatPromptTemplate.from_template(
        """
        You are a chatbot. You are in {language} mode. 
        Please answer the following question. {prompt_text}
        """
    )
    chain = prompt | claude_3_client | StrOutputParser()
    response = chain.invoke({"language": language, "prompt_text": prompt_text})
    return response


# Streamlit app
st.title("ChatApp using Bedrock & Claude3")

language = st.sidebar.selectbox("Select a language", ["English", "Spanish", "French"])

if language:
    prompt_text = st.text_area(label="Enter your Prompt", max_chars=100)

if prompt_text:
    response = my_chatbot(language, prompt_text)
    st.write(response)