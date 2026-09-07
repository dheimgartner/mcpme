# mcpme

A personal MCP server that exposes your CV so any MCP-compatible agent can answer questions about you.

## Install

```bash
pip install -e .
# or with uv
uv tool install .
```

## Usage

By default the bundled `cv.md` is used. Point to your own CV with an env var:

```bash
MCPME_CV_PATH=/path/to/your-cv.md mcpme
```

## Connect to Claude Code

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "mcpme": {
      "command": "mcpme",
      "env": {
        "MCPME_CV_PATH": "/path/to/your-cv.md"
      }
    }
  }
}
```

## What it exposes

| Type | Name | Description |
|------|------|-------------|
| Tool | `read_cv` | Returns the full CV text |
| Resource | `cv://resume` | CV as an MCP resource |
| Prompt | `about_me` | Primed prompt for CV Q&A |
