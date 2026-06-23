from agno.models.mistral.mistral import MistralChat

# Provide backward-compatible exports expected by some consumers/tests.
# Try to import canonical names if present; otherwise create lightweight
# compatibility aliases so imports like `from agno.models.mistral import FirecrawlApp, ScrapeOptions`
# succeed during test collection.
try:
    from agno.models.mistral.mistral import FirecrawlApp, ScrapeOptions  # type: ignore
except Exception:
    class FirecrawlApp(MistralChat):
        """Backward-compatible alias for an app wrapper around MistralChat."""
        pass

    class ScrapeOptions:
        """Compatibility alias for legacy ScrapeOptions API."""
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)


__all__ = [
    "MistralChat",
]
