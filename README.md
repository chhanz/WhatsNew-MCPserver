# WhatsNew-MCPserver

An MCP (Model Context Protocol) server that fetches AWS What's New announcements by month.

> 🇺🇸 [English README](./README.md)  |  🇰🇷 [한국어 README](./README-kr.md)

## Overview

This server exposes a single MCP tool `get_whats_new` that queries the AWS What's New page via its internal JSON API and returns formatted results filtered by year/month.

## Requirements

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

```bash
git clone https://github.com/chhanz/WhatsNew-MCPserver.git
```

## MCP Tool

### `get_whats_new`

| Parameter | Format | Example |
|-----------|--------|---------|
| `year_month` | `YYYY/MM` | `2026/01` |

Returns a formatted list of AWS What's New entries for the specified month, including title, date, description, and link.

## Usage

### Kiro MCP Configuration

Add to your `.kiro/settings/mcp.json`:

```json
{
  "mcpServers": {
    "whats-new-mcp": {
      "command": "uvx",
      "args": [
        "--from", "/path/to/WhatsNew-MCPserver",
        "whats-new-mcp"
      ],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Project Structure

```
WhatsNew-MCPserver/
├── pyproject.toml
├── README.md
├── README-kr.md
└── src/
    └── whats_new_mcp/
        ├── __init__.py
        └── server.py
```

## Notes

- The API endpoint is an undocumented internal API used by the AWS website frontend. It may change without notice.
- Monthly filtering is done client-side since the API only supports year-level tag filtering.

## License

This project is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Commercial use is not permitted.
