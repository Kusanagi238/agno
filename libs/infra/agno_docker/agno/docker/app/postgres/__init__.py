from agno.docker.app.postgres.pgvector import PgVectorDb
from agno.docker.app.postgres.postgres import PostgresDb

class MemorySearchResult:
    """Compatibility stub for zep_cloud.types.MemorySearchResult expected by external code.

    This minimal implementation exists only so that importers looking for the
    symbol `MemorySearchResult` do not fail. It can be expanded if callers
    require specific attributes or behavior.
    """
    def __init__(self, *args, **kwargs):
        # act as a simple container placeholder
        self.args = args
        self.kwargs = kwargs

__all__ = [
    "PgVectorDb",
    "PostgresDb",
    "MemorySearchResult",
]
