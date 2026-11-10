# Product and Architecture Decisions

| Decision | Current position | Revisit when |
|---|---|---|
| Product boundary | PoultryLink separate from PoultryGuard AI | Integration use case is validated |
| Architecture | Modular monolith | Scale/team boundaries justify separation |
| Backend | FastAPI/Python | Requirements change |
| Database | PostgreSQL | Workload needs specialised storage |
| Frontend | Next.js/TypeScript | Product constraints change |
| Search | PostgreSQL first | Measured relevance/scale limits appear |
| Geography | Country/state/LGA/market hierarchy | Reference source is selected |
| AI | Out of MVP 1 | Validated use case and data exist |
| Payments | Out of MVP 1 | Legal/operational readiness exists |
| Licence | All-rights-reserved placeholder | Owner selects a conventional licence |

## ADR template
For consequential choices, create a numbered document in `docs/adr/` covering status, context, decision, alternatives, consequences and security/privacy implications.
