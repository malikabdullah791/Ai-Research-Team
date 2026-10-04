from crewai_tools import SerperDevTool
from crewai.tools import tool


# -----------------------------
# Web Search Tool
# -----------------------------
web_search_tool = SerperDevTool(
    search_url="https://google.serper.dev/search",
    n_results=5,
)


# -----------------------------
# Calculator Tool
# -----------------------------
@tool("Research Calculator")
def calculator(expression: str) -> str:
    """
    Calculate a basic mathematical expression.

    Use this tool when numerical calculations are required.
    Example:
    125 * 0.85
    """

    allowed = set("0123456789+-*/().% ")

    if not expression or not set(expression) <= allowed:
        return "Invalid mathematical expression."

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"Calculation result: {result}"
    except Exception:
        return "Could not calculate the expression."
