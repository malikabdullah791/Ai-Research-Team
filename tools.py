import os

from crewai_tools import SerperDevTool
from crewai.tools import tool


# ============================================================
# WEB SEARCH TOOL
# ============================================================

if not os.getenv("SERPER_API_KEY"):
    raise ValueError(
        "SERPER_API_KEY is missing. Add it in Streamlit Secrets."
    )


web_search_tool = SerperDevTool()


# ============================================================
# CALCULATOR TOOL
# ============================================================

@tool("Research Calculator")
def calculator_tool(expression: str) -> str:
    """
    Perform a basic mathematical calculation.

    Example:
    25 * 4
    100 / 5
    (50 + 30) / 2
    """

    allowed_characters = set(
        "0123456789+-*/().% "
    )

    if not expression:
        return "No expression was provided."

    if not set(expression) <= allowed_characters:
        return "Invalid expression. Only basic mathematical operators are allowed."

    try:

        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return f"Calculation result: {result}"

    except Exception as error:

        return f"Calculation failed: {error}"
