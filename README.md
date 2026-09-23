# Type hints added for clarity
# web-scraper

A lightweight web scraper with configurable extraction rules.

## Features

- CSS selector based extraction
- Export to JSON / CSV
- Rate limiting and retry
- robots.txt respect

## Quick Start

```bash
pip install requests beautifulsoup4
python scraper.py --url https://example.com --selector "h1"
```

## Configuration

Define scraping rules in `rules.yaml`:

```yaml
rules:
  - name: titles
    selector: "h2.title"
    type: text
  - name: links
    selector: "a[href]"
    type: attr
    attr: href
```

## License

MIT
