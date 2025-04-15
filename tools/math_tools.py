from typing import Dict, Any
from smolagents.tools import tool

@tool
def add_numbers(a: float, b: float) -> Dict[str, Any]:
    """
    Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        Dict[str, Any]: Dictionary containing the result and any additional information
    """
    result = a + b
    return {
        "result": result,
        "explanation": f"Added {a} and {b} to get {result}"
    }


