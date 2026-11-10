"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import get_settings

settings = get_settings()
app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="PoultryLink API foundation.",
    debug=settings.debug,
)
app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get("/", tags=["health"])
def root() -> dict[str, str]:
    """Return a basic service identity response."""
    return {"service": "PoultryLink API", "status": "ok"}
