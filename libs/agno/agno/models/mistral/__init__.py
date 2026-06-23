try:
    # Try the modern name first
    from agno.models.mistral.mistral import MistralChat, ScrapeOptions
except Exception:
    try:
        # Fall back to the older/alternate name if available
        from agno.models.mistral.mistral import MistralChat, V1ScrapeOptions as ScrapeOptions
    except Exception:
        # Ensure the name exists to avoid ImportError on import-time; keep None as a safe fallback
        from agno.models.mistral.mistral import MistralChat
        ScrapeOptions = None

__all__ = [
    "MistralChat",
    "ScrapeOptions",
]
