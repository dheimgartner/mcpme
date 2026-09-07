# mcpme

A personal MCP server that exposes your CV so any MCP-compatible agent can answer questions about you.

## Install

```bash
# Create a local virtual environment and install dependencies
uv venv
uv sync .

# Or install globally as a tool
uv tool install .
```

## Usage

By default the bundled `cv.md` is used. Point to your own CV with an env var:

```bash
MCPME_CV_PATH=/path/to/your-cv.md mcpme
```

## Connect to Claude Code

To connect the server to a specific project, create a local settings file:

```bash
mkdir -p .claude
cat > .claude/settings.local.json << 'EOF'
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
EOF
```

Or add it to your global `~/.claude/settings.json` to make it available everywhere.

## What it exposes

| Type | Name | Description |
|------|------|-------------|
| Tool | `read_cv` | Returns the full CV text |
| Resource | `cv://resume` | CV as an MCP resource |
| Prompt | `about_me` | Primed prompt for CV Q&A |
