from langchain.tools import Tool

@Tool
def calculator(expression: str) -> float:
    """
    Calculate a mathematical expression
    """
    try:
        return eval(expression)
    except Exception as e:
        return str(e)
    
math_tool = calculator