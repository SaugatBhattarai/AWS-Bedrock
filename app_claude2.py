# A Simple application to test claude2 on aws bedrock
import boto3
import json
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_aws import BedrockLLM

region = "us-east-1" # for example, "us-east-1" or "us-west-2"

session = boto3.Session()
bedrock = session.client(
    service_name='bedrock', #creates a Bedrock client
    region_name=region
)

model_id = "anthropic.claude-v2"

model_kwargs = { 
    "max_tokens_to_sample": 512,
    "temperature": 1.0,
}

claude_2_client = BedrockLLM(
    region_name = region,
    model_id=model_id,
    model_kwargs=model_kwargs,
)

# Invoke Example
messages = [
    ("human","{question}"),
]

prompt = ChatPromptTemplate.from_messages(messages)


chain = prompt | claude_2_client | StrOutputParser()

# Chain Invoke
response = chain.invoke({"question": "who is buddha?"})
print(response)