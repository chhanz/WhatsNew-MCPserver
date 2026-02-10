---
name: "whats-new-mcp"
displayName: "AWS What's New"
description: "Fetch and browse AWS What's New announcements by month using the whats-new-mcp server."
keywords: ["aws", "whats-new", "announcements", "aws-updates", "whats-new-mcp"]
author: "cheolhee"
---

# AWS What's New

## Overview

This power connects to the `whats-new-mcp` MCP server to fetch AWS What's New announcements filtered by year and month. It queries the AWS What's New internal JSON API and returns formatted results including title, date, description, and link for each entry.

Use this power when you need to check what AWS services or features were announced in a specific month.

## Available MCP Servers

- **whats-new-mcp**: Provides the `get_whats_new` tool

## Tool Usage

### `get_whats_new`

Fetches AWS What's New entries for a specific month.

| Parameter | Format | Required | Example |
|-----------|--------|----------|---------|
| `year_month` | `YYYY/MM` | Yes | `2026/01` |

**Example prompts:**
- "What AWS announcements were made in January 2026?"
- "Show me AWS What's New for 2025/12"
- "Get the latest AWS updates from last month"

**Example response format:**
```
# AWS What's New - 142 entries

## [1] Amazon S3 now supports ...
Date: 2026-01-15

Description text...

Link: https://aws.amazon.com/about-aws/whats-new/...
---
```

## Best Practices

- Use `YYYY/MM` format strictly (e.g., `2026/01`, not `2026/1`)
- The API fetches all entries for the given year, then filters by month client-side
- Results are sorted by date in descending order
- Each request may take a few seconds depending on the volume of entries for that year

## Troubleshooting

### No results returned
- Verify the year/month format is correct (`YYYY/MM`)
- Check that the month has published entries (future months won't have data)
- The API endpoint is undocumented and may change without notice

### Timeout errors
- The server uses a 30-second timeout per API call
- If the year has many entries, pagination may require multiple calls
- Try again if the request times out

### MCP server not responding
- Verify the server is running: check Kiro MCP server status
- Ensure the `whats-new-mcp` server is properly configured in mcp.json

## Configuration

No additional configuration required. The MCP server works out of the box after installation.

**Installation:**
```bash
git clone https://github.com/chhanz/WhatsNew-MCPserver.git
```

**Kiro MCP config (`mcp.json`):**
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

## MCP Config Placeholders

- **`/path/to/WhatsNew-MCPserver`**: Local path to the cloned `WhatsNew-MCPserver` repository.
  - **How to set it:** Replace with the actual path where you cloned the repository (e.g., `/Users/yourname/projects/WhatsNew-MCPserver`)

---

**Package:** `whats-new-mcp`
**MCP Server:** whats-new-mcp
