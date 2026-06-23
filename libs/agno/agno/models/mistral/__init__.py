from agno.models.mistral.mistral import MistralChat

try:
    from firecrawl import ScrapeOptions, FirecrawlApp
except Exception:
    class ScrapeOptions:  # fallback to provide clearer error when used
        def __init__(self, *args, **kwargs):
            raise ImportError("`firecrawl-py` not installed. Please install using `pip install firecrawl-py`")
    class FirecrawlApp:
        def __init__(self, *args, **kwargs):
            raise ImportError("`firecrawl-py` not installed. Please install using `pip install firecrawl-py`")

__all__ = [
    "MistralChat",
    "ScrapeOptions",
    "FirecrawlApp",
]
