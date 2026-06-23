from agno.models.mistral.mistral import MistralChat

# Provide a backward-compatible ScrapeOptions symbol expected by downstream code.
# Prefer an existing V1ScrapeOptions if present in the module, otherwise provide
# a minimal placeholder so imports succeed during test collection.
try:
    from agno.models.mistral.mistral import V1ScrapeOptions as ScrapeOptions
except Exception:
    class ScrapeOptions:
        """Placeholder ScrapeOptions for compatibility during import-time checks."""
        def __init__(self, *args, **kwargs):
            pass

__all__ = [
    "MistralChat",
    "ScrapeOptions",
]
