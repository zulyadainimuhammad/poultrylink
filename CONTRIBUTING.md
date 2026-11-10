# Contributing

## Workflow
1. Identify or open an issue describing the work.
2. Create a focused branch from `main`.
3. Make a coherent change.
4. Add/update tests and documentation.
5. Run checks locally.
6. Open a pull request with rationale, test evidence and migration notes.

## Commit conventions
Examples: `docs: define MVP requirements`, `feat(auth): add registration endpoint`, `feat(marketplace): add listing search`, `test(requests): cover buyer request validation`.

## Engineering expectations
Keep handlers thin and business rules in services. Validate inputs at system boundaries. Add tests for normal, invalid and unauthorised cases. Include reviewed Alembic migrations for schema changes. Never commit credentials, private buyer/farmer data or production data.

## Product expectations
Do not silently introduce payments, escrow, delivery guarantees, ratings or advanced AI features into MVP 1.
