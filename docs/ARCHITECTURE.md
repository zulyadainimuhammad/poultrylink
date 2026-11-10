# Architecture

## Initial approach
Start with a modular monolith: one API deployment and relational database with clear module boundaries. Avoid premature microservices.

```text
Browser / Mobile Web
       |
 Next.js frontend
       |
 FastAPI application
  |       |        |
Identity Marketplace Messaging
  |       |        |
      PostgreSQL
          |
  Future object storage
          |
   Future analytics / ML
```

## Backend modules
Identity, profiles, catalogue, marketplace, demand, responses, messaging and administration. Keep HTTP routes thin; validate contracts in schemas; put business rules in services.

## Data infrastructure
PostgreSQL is the source of truth. Use Alembic for schema evolution. Store media in object storage and persist keys/metadata in PostgreSQL. Begin search with PostgreSQL and add a search engine only when measured needs justify it.

## Geography
Use a hierarchy such as Country → State/Region → LGA/District → Market/Community. Avoid assumptions tied to one city.

## Security
Authentication identifies the user; authorisation decides access. Enforce ownership on listings and requests, participant checks for conversations, upload validation, rate limiting, secret management and minimal security logging.

## Future evolution
Payments, logistics integrations, analytics warehouse and ML services may be added behind stable contracts after product, operational and regulatory needs are validated. Record consequential decisions as ADRs.
