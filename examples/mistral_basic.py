"""
Mistral AI Basic Example with AgentBill Tracking
"""
from mistralai import Mistral
from agentbill import AgentBill

# Initialize AgentBill
agentbill = AgentBill.init({
    "api_key": "your-agentbill-api-key",
    "customer_id": "customer-123",
    "debug": True
})

# Wrap Mistral client
client = agentbill.wrap_mistral(Mistral(
    api_key="your-mistral-api-key"
))

# Make a request - automatically tracked!
response = client.chat.complete(
    model="mistral-large-latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)

# Flush telemetry
agentbill.flush()
