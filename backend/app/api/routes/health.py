"""Health endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """Report liveness; database readiness is not checked yet."""
    return {"status": "healthy"}
