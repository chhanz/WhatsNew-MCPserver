# WhatsNew-MCPserver

AWS What's New 발표 내용을 월별로 조회하는 MCP (Model Context Protocol) 서버입니다.

> 🇺🇸 [English README](./README.md)  |  🇰🇷 [한국어 README](./README-kr.md)

## 개요

`get_whats_new` MCP 도구를 제공하며, AWS What's New 페이지의 내부 JSON API를 통해 연/월 기준으로 필터링된 결과를 반환합니다.

## 요구사항

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## 설치

```bash
git clone https://github.com/chhanz/WhatsNew-MCPserver.git
```

## MCP 도구

### `get_whats_new`

| 파라미터 | 형식 | 예시 |
|---------|------|------|
| `year_month` | `YYYY/MM` | `2026/01` |

지정한 월의 AWS What's New 항목을 제목, 날짜, 설명, 링크 포함 형식으로 반환합니다.

## 사용법

### Kiro MCP 설정

`.kiro/settings/mcp.json`에 추가:

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

## 프로젝트 구조

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

## 참고사항

- 사용하는 API 엔드포인트는 AWS 웹사이트 프론트엔드가 내부적으로 사용하는 비공식 API입니다. 사전 공지 없이 변경될 수 있습니다.
- API가 연도 단위 태그 필터만 지원하므로, 월별 필터링은 클라이언트 측에서 처리합니다.

## 라이선스

이 프로젝트는 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 라이선스를 따릅니다. 상업적 사용은 허용되지 않습니다.
