# Backend

FastAPI service for PoultryLink.

From the repository root:

```bash
pip install -e ".[dev]"
uvicorn app.main:app --app-dir backend --reload
pytest
```

The current service contains only root and liveness endpoints. Authentication and marketplace workflows are not implemented yet.
