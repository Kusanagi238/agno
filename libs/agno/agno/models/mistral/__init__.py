from agno.models.mistral.mistral import MistralChat

# Re-export a ScrapeOptions symbol for compatibility with environments
# that expect `from firecrawl import ScrapeOptions`. The upstream
# package may expose this under an alternate name (V1ScrapeOptions),
# so try both without raising on import failure to avoid breaking
# test collection.
try:
    from firecrawl import ScrapeOptions
except Exception:
    try:
        from firecrawl import V1ScrapeOptions as ScrapeOptions
    except Exception:
        ScrapeOptions = None  # type: ignore

__all__ = [
    "MistralChat",
    "ScrapeOptions",
]
