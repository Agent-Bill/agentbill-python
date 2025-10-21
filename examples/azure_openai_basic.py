"""
Azure OpenAI Basic Example with AgentBill Tracking
"""
from openai import AzureOpenAI
from agentbill import AgentBill

# Initialize AgentBill
agentbill = AgentBill.init({
    "api_key": "your-agentbill-api-key",
    "customer_id": "customer-123",
    "debug": True
})

# Wrap Azure OpenAI client
client = agentbill.wrap_azure_openai(AzureOpenAI(
    api_key="your-azure-api-key",
    api_version="2024-02-01",
    azure_endpoint="https://your-resource.openai.azure.com"
))

# Make a request - automatically tracked!
response = client.chat.completions.create(
    model="gpt-4",  # Your deployment name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)

# Flush telemetry
agentbill.flush()
