import re


def slugify(text: str) -> str:
    """Lowercase, collapse non-alphanumeric runs to a single dash, trim edges."""
    if not text:
        return ""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return slug.strip("-")


def truncate(text: str, max_len: int, suffix: str = "…") -> str:
    """Shorten text to max_len, breaking at the last whole word when possible."""
    if len(text) <= max_len:
        return text

    body_len = max_len - len(suffix)
    if body_len <= 0:
        return suffix[:max_len]

    chunk = text[:body_len]
    if body_len < len(text) and text[body_len] != " ":
        last_space = chunk.rfind(" ")
        if last_space > 0:
            chunk = chunk[:last_space]
    else:
        chunk = chunk.rstrip()

    return chunk + suffix
