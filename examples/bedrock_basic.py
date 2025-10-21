"""
AWS Bedrock Basic Example with AgentBill Tracking
"""
import json
import boto3
from agentbill import AgentBill

# Initialize AgentBill
agentbill = AgentBill.init({
    "api_key": "your-agentbill-api-key",
    "customer_id": "customer-123",
    "debug": True
})

# Wrap Bedrock client
bedrock = agentbill.wrap_bedrock(
    boto3.client('bedrock-runtime', region_name='us-east-1')
)

# Make a request - automatically tracked!
response = bedrock.invoke_model(
    modelId='anthropic.claude-v2',
    body=json.dumps({
        "prompt": "\n\nHuman: What is the capital of France?\n\nAssistant:",
        "max_tokens_to_sample": 300,
        "temperature": 0.7
    })
)

# Parse response
result = json.loads(response['body'].read())
print(result['completion'])

# Flush telemetry
agentbill.flush()
