from agno.models.mistral.mistral import MistralChat

# Provide compatibility for code that expects a ScrapeOptions symbol to be available
# Export ScrapeOptions from firecrawl when present, fall back to V1ScrapeOptions, or
# provide a helpful ImportError-raising placeholder to avoid import-time failures.
try:
    from firecrawl import ScrapeOptions  # type: ignore
except Exception:
    try:
        from firecrawl import V1ScrapeOptions as ScrapeOptions  # type: ignore
    except Exception:
        class ScrapeOptions:
            def __init__(self, *args, **kwargs):
                raise ImportError("firecrawl-py is not installed. Please install using `pip install firecrawl-py` to use ScrapeOptions.")

__all__ = [
    "MistralChat",
    "ScrapeOptions",
]
