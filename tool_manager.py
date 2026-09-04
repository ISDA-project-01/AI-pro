from web_search import web_search
from code_executor import code_executor
from terminal_manager import terminal_manager
from rag_manager import rag_manager

class ToolManager:
    def __init__(self):
        self.tools = {
            "web_search": web_search.search,
            "code_execution": code_executor.execute_python,
            "terminal": terminal_manager.run_command,
            "rag_query": rag_manager.query_context
        }

    def get_available_tools(self) -> list:
        return list(self.tools.keys())

    def execute_tool(self, tool_name: str, *args, **kwargs):
        if tool_name in self.tools:
            return self.tools[tool_name](*args, **kwargs)
        return f"Tool {tool_name} not found."

tool_manager = ToolManager()
