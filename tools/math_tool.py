from langchain.tools import Tool

def calculate_math(expression: str) -> str:
    """Evaluates a mathematical expression."""
    try:
        result = eval(expression)  # ⚠️ Be cautious with `eval`, use `sympy` for safer evaluation.
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# ✅ Define tool correctly
math_tool = Tool(
    name="Calculator",
    func=calculate_math,
    description="Use this tool to solve mathematical expressions. Example: '2+2' or 'sqrt(16)'."
)
