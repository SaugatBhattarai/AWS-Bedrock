# A simple script to test the connection to the Bedrock service
import boto3
import json
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

region = "us-east-1" # for example, "us-east-1" or "us-west-2"

session = boto3.Session()
bedrock = session.client(
    service_name='bedrock', #creates a Bedrock client
    region_name=region
)
output_text = bedrock.list_foundation_models()
print(json.dumps(output_text, indent=4)) 