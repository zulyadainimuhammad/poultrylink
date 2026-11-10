# PoultryLink

**A digital poultry marketplace and market-intelligence platform for Nigeria.**

PoultryLink is being developed to connect poultry farmers, buyers, input suppliers and agricultural service providers through structured product listings, buyer requests and seller responses. Its longer-term direction is a trusted digital poultry value-chain platform with commerce, market intelligence and AI-assisted decision support.

> **Product boundary:** PoultryLink is a separate product from PoultryGuard AI. Future integrations may be considered, but the initial product and MVP are independently scoped.

## MVP 1 scope
1. Account registration and authentication.
2. User profiles and roles.
3. Product catalogue.
4. Seller marketplace listings.
5. Listing search and filtering.
6. Structured buyer requests.
7. Seller responses to buyer requests.
8. Basic buyer–seller messaging.

Payments, delivery orchestration, disputes, ratings, advanced verification, market-price dashboards and AI recommendations are later phases, not MVP functionality.

## Initial user roles
`FARMER`, `BUYER`, `SUPPLIER`, `SERVICE_PROVIDER`, `ADMIN`.

## Initial product categories
Live birds, eggs, day-old chicks and growers, feed, poultry inputs/health products, and equipment.

## Technology direction
- Backend: Python + FastAPI
- Database: PostgreSQL
- ORM/migrations: SQLAlchemy + Alembic
- Validation: Pydantic
- Frontend: Next.js + TypeScript
- Tests: Pytest
- CI: GitHub Actions
- Initial search: PostgreSQL
- Future analytics/ML: Python and SQL, introduced when data supports it

## Repository structure
```text
.github/workflows/  CI
backend/            FastAPI service and tests
data/               Data documentation and local-only data directories
docs/               Product, architecture and delivery documentation
frontend/           Next.js application scaffold
infra/              Infrastructure notes
ml/                 Future analytics and ML work
scripts/            Developer and maintenance scripts
```

## Local setup
Requirements: Python 3.11+, Node.js LTS, Docker and Git.

```bash
git clone https://github.com/zulyadainimuhammad/poultrylink.git
cd poultrylink
cp .env.example .env
docker compose up -d db
python -m venv .venv
```

Windows PowerShell: ` .\.venv\Scripts\Activate.ps1 `  
macOS/Linux: `source .venv/bin/activate`

```bash
pip install -e ".[dev]"
uvicorn app.main:app --app-dir backend --reload
pytest
```

API docs: `http://127.0.0.1:8000/docs`.

Frontend:
```bash
cd frontend
npm install
npm run dev
```

## Engineering principles
- Keep business rules in services, not route handlers.
- Validate external input and enforce authorisation on the server.
- Store money as decimals with explicit currency; never use floats for money.
- Store quantities with explicit units.
- Model geography hierarchically (country, state, LGA, market); do not hard-code Kano.
- Separate listing price, transaction price and buyer budget.
- Store timestamps in UTC.
- Never commit secrets or private/production data.
- Do not claim verification, secure payments or transaction guarantees until implemented.

## Documentation
Start with [Product Vision](docs/PRODUCT_VISION.md), [PRD](docs/PRD.md), [MVP Scope](docs/MVP_SCOPE.md), [Architecture](docs/ARCHITECTURE.md), [Database Design](docs/DATABASE_DESIGN.md), [Data Strategy](docs/DATA_STRATEGY.md) and [Roadmap](docs/ROADMAP.md).

## Current status
**Foundation scaffold.** The initial repository documents and scaffolds the product. Marketplace workflows are not yet implemented or production-ready.

## Licence
A restrictive placeholder notice is in [LICENSE](LICENSE). No open-source reuse rights are granted until the owner selects a conventional licence.
