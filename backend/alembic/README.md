# Database migrations

Alembic is configured at the repository root. Create migrations after adding SQLAlchemy domain models:

```bash
alembic revision --autogenerate -m "create initial domain tables"
alembic upgrade head
```

Review generated migrations manually before applying them. No application schema is created by this foundation.
