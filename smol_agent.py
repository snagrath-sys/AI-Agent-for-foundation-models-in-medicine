from smolagents import CodeAgent
from smolagents.models import HfApiModel
from tools import math_tools

def initialize_agent(hf_token):
    """Initialize and return the smolAgent"""
    model = HfApiModel(
        model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        token=hf_token
    )
    
    agent = CodeAgent(
        model=model,
        tools=[math_tools.add_numbers],
        additional_authorized_imports=["duckdb"]
    )
    
    return agent

def process_message(agent, prompt, conversation_history=""):
    """Process a message using the agent"""
    try:
        response = agent.run(prompt)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

def format_conversation_history(messages):
    """Format conversation history for the agent"""
    conversation = ""
    for msg in messages:
        role = "Human" if msg["role"] == "user" else "Assistant"
        conversation += f"{role}: {msg['content']}\n"
    return conversation
