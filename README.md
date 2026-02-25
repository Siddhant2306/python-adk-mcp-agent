# Agent (Google ADK + Remote MCP tools)

A minimal **Google ADK** agent configuration that connects to one or more **remote MCP (Model Context Protocol)** servers and exposes their tools to a Gemini model.

## What it does

- Loads environment variables from `.env`.
- Creates a `google.adk.agents.LlmAgent` using model `gemini-2.5-flash`.
- Attaches two MCP toolsets via `StreamableHTTPConnectionParams`:
  - `MCP_SERVER_URL`
  - `SEQUENTIAL_MCP_URL`

This repo is essentially the “agent wiring” layer — the functionality depends on which MCP servers you point it at.

## Files

- `agent.py` — defines `root_agent`.
- `requirements.txt` — Python deps.
- `.env` — your local config (not committed).

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```env
MCP_SERVER_URL=http://localhost:PORT/mcp
SEQUENTIAL_MCP_URL=http://localhost:PORT/mcp
# (and any auth headers/keys your MCP servers require)
```

## Run / usage

How you run this depends on your ADK runner / application wrapper.

At minimum, `agent.py` must be importable so your runner can pick up `root_agent`.

## Notes

- If either MCP URL is missing, the tool connection will fail.
- Keep `.env` out of git.

## TODO

- Add a small runner script (CLI) to interact with the agent locally.
- Document the expected MCP server endpoints and any auth requirements.
