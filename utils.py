import re


def slugify(text: str) -> str:
    """Lowercase, collapse non-alphanumeric runs to a single dash, trim edges."""
    if not text:
        return ""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return slug.strip("-")
