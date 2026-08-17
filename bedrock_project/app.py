import os
import boto3
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get AWS region
region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

# Create Bedrock client
client = boto3.client(
    "bedrock-runtime",
    region_name=region
)

# Send prompt to Bedrock
response = client.converse(
    modelId="amazon.nova-micro-v1:0",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": "Explain Amazon Bedrock in simple words."
                }
            ]
        }
    ]
)

# Extract AI response
answer = response["output"]["message"]["content"][0]["text"]

print("\nAI Response:")
print(answer)