# API Specification (Draft)

Base path: `/api/v1`. Only the health endpoint exists in the initial scaffold; other paths are proposed.

## System
| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Liveness |

## Authentication (planned)
POST `/auth/register`, POST `/auth/login`, POST `/auth/logout`, POST `/auth/refresh`, POST `/auth/password/forgot`, POST `/auth/password/reset`.

## Profiles and catalogue (planned)
GET/PATCH `/profiles/me`; GET `/profiles/{user_id}`; GET `/categories`; GET `/products`.

## Listings (planned)
POST `/listings`; GET `/listings`; GET/PATCH `/listings/{listing_id}`; POST `/listings/{listing_id}/close`.

Possible filters: q, category/product, state, LGA, minimum quantity, maximum price, currency, status, page and page_size.

## Buyer requests and responses (planned)
POST/GET `/buyer-requests`; GET/PATCH `/buyer-requests/{request_id}`; POST `/buyer-requests/{request_id}/responses`; GET `/buyer-requests/{request_id}/responses`.

## Messaging (planned)
POST/GET `/conversations`; GET/POST `/conversations/{id}/messages`.

## Contract conventions
JSON bodies, stable error shapes, correct status codes, server-side permission checks, capped pagination, request IDs, documented monetary precision and currency, and no exposure of credentials or private fields. Treat as draft until routes and schemas are implemented and tested.
