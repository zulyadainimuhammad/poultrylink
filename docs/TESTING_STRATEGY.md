# Testing Strategy

## Test layers
1. Unit tests for services, validation and state transitions.
2. API tests for contracts, status codes and permissions.
3. Database integration tests for constraints, relationships and migrations.
4. Frontend tests for forms, navigation and accessibility.
5. End-to-end tests for registration, listing, search, requests and responses.
6. Security tests for ownership, role escalation, injection, rate limits and uploads.
7. Operational tests for health checks, backup restore and deployment smoke tests.

For each write workflow test valid input, invalid/missing fields, unauthenticated access, unauthorised access, conflicts, not-found behaviour and boundaries/unit/currency consistency.

## Local checks
Backend: `pytest` and `ruff check backend`. Frontend: `npm run build`.

Set coverage thresholds after measuring a meaningful baseline.
