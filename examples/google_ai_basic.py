"""
Google AI (Gemini) Basic Example with AgentBill Tracking
"""
import google.generativeai as genai
from agentbill import AgentBill

# Initialize AgentBill
agentbill = AgentBill.init({
    "api_key": "your-agentbill-api-key",
    "customer_id": "customer-123",
    "debug": True
})

# Configure Google AI
genai.configure(api_key="your-google-api-key")

# Create and wrap Gemini model
model = genai.GenerativeModel('gemini-pro')
wrapped_model = agentbill.wrap_google_ai(model)

# Make a request - automatically tracked!
response = wrapped_model.generate_content("What is the capital of France?")

print(response.text)

# Flush telemetry
agentbill.flush()
