"""Forum scraper skeleton (Task 2)."""

from bs4 import BeautifulSoup


def parse_forum_html(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    return [p.get_text(strip=True) for p in soup.select("p.review")]
