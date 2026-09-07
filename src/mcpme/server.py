import os
from pathlib import Path

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("mcpme")


def _load_cv() -> str:
    cv_path = os.environ.get("MCPME_CV_PATH")
    if cv_path:
        return Path(cv_path).read_text()
    return (Path(__file__).parent / "cv.md").read_text()


@mcp.resource("cv://resume", description="The owner's full CV / résumé in Markdown format.")
def get_cv() -> str:
    return _load_cv()


@mcp.tool(description="Return the owner's full CV / résumé. Use this to answer questions about the person's background, skills, and experience.")
def read_cv() -> str:
    return _load_cv()


@mcp.prompt(description="Loads the CV and primes the model to answer questions about the owner.")
def about_me() -> str:
    cv = _load_cv()
    return (
        "You are a helpful assistant answering questions about the following person "
        "based strictly on their CV. Be concise and factual.\n\n"
        f"<cv>\n{cv}\n</cv>"
    )
