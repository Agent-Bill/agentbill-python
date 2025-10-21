"""
Basic example of using AgentBill SDK with OpenAI
"""
import os
from agentbill import AgentBill
from openai import OpenAI

# Initialize AgentBill with your API key
agentbill = AgentBill.init({
    "api_key": os.getenv("AGENTBILL_API_KEY", "your-api-key"),
    "base_url": os.getenv("AGENTBILL_BASE_URL"),
    "customer_id": "customer-123",
    "debug": True
})

# Wrap your OpenAI client
client = agentbill.wrap_openai(OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
))

# Use OpenAI normally - tracking is automatic!
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)

# All usage (tokens, cost, latency) is automatically tracked to your AgentBill dashboard
