#Basic Code for Bedrock App with langchain
#Runs with the default profile

import boto3
from langchain_aws import ChatBedrock

client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
model_id = "anthropic.claude-3-haiku-20240307-v1:0"
model_kwargs =  { 
    "max_tokens": 1024,
    "temperature": 0.9,
}

claude_v2_client = ChatBedrock(
    client=client,
    model_id=model_id,
    model_kwargs=model_kwargs,
)

response = claude_v2_client.invoke("what is large learning model?")
print(response.content)