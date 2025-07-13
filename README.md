# Lang-graph-AgenticAI

A minimal project using LangGraph with MCP (Multi-Client Protocol) for agentic workflows.

## 🔧 Setup

```bash
uv pip install -r requirements.txt
````

Or with plain Python:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Run

```bash
uv run client.py
```

## 📁 Structure

* `client.py` — Runs LangGraph client with MCP tools
* `main.py` — Basic agent entry point
* `mcp_servers/` — Tool servers
* `notebooks/` — Experiments

