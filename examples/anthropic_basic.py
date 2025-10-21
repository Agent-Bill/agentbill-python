"""
Basic example of using AgentBill SDK with Anthropic
"""
import os
from agentbill import AgentBill
from anthropic import Anthropic

# Initialize AgentBill
agentbill = AgentBill.init({
    "api_key": os.getenv("AGENTBILL_API_KEY", "your-api-key"),
    "base_url": os.getenv("AGENTBILL_BASE_URL"),
    "customer_id": "customer-123",
    "debug": True
})

# Wrap your Anthropic client
client = agentbill.wrap_anthropic(Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
))

# Use Anthropic normally - tracking is automatic!
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.content[0].text)

# All usage is automatically tracked to your dashboard
