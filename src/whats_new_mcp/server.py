import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("whats-new-mcp")

API_BASE = "https://aws.amazon.com/api/dirs/items/search"
DIRECTORY_ID = "whats-new-v2"
PAGE_SIZE = 100


def fetch_items(year: int, month: int) -> list[dict]:
    """Fetch items from AWS What's New API for a specific year/month. Includes pagination."""
    year_tag = f"whats-new-v2#year#{year}"
    results = []
    page = 0

    while True:
        params = {
            "item.directoryId": DIRECTORY_ID,
            "sort_by": "item.additionalFields.postDateTime",
            "sort_order": "desc",
            "size": PAGE_SIZE,
            "page": page,
            "item.locale": "en_US",
            "tags.id": year_tag,
        }
        resp = httpx.get(API_BASE, params=params, timeout=30, follow_redirects=True)
        resp.raise_for_status()
        data = resp.json()

        for item in data.get("items", []):
            fields = item.get("item", {}).get("additionalFields", {})
            date_str = fields.get("postDateTime", "")[:10]
            if date_str.startswith(f"{year}-{month:02d}"):
                results.append({
                    "title": fields.get("headline", ""),
                    "description": fields.get("postBody", ""),
                    "link": fields.get("headlineUrl", ""),
                    "published": date_str,
                })

        total = data.get("metadata", {}).get("totalHits", 0)
        fetched = (page + 1) * PAGE_SIZE
        if fetched >= total or not data.get("items"):
            break
        page += 1

    return results


def format_entries(entries: list[dict]) -> str:
    """Format entries into a readable string."""
    if not entries:
        return "No What's New entries found for the specified month."

    lines = [f"# AWS What's New - {len(entries)} entries\n"]
    for i, e in enumerate(entries, 1):
        lines.append(f"## [{i}] {e['title']}")
        lines.append(f"Date: {e['published']}")
        lines.append(f"\n{e['description']}\n")
        lines.append(f"Link: {e['link']}")
        lines.append("---\n")
    return "\n".join(lines)


@mcp.tool()
def get_whats_new(year_month: str) -> str:
    """Fetch news from AWS What's New API for a specific month.

    Args:
        year_month: Year/month to query (format: YYYY/MM, e.g. 2026/01)
    """
    try:
        parts = year_month.strip().split("/")
        year = int(parts[0])
        month = int(parts[1])
        if month < 1 or month > 12:
            return "Month must be between 01 and 12."
    except (ValueError, IndexError):
        return "Invalid format. Please use YYYY/MM format. (e.g. 2026/01)"

    entries = fetch_items(year, month)
    return format_entries(entries)


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
