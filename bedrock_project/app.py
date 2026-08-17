import boto3

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

response = client.converse(
    modelId="YOUR_MODEL_ID",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": "Explain AWS Bedrock in simple words"
                }
            ]
        }
    ]
)

print(response["output"]["message"]["content"][0]["text"])