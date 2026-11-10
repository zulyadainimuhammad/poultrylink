# Product Requirements Document

**Product:** PoultryLink  
**Release:** MVP 1  
**Status:** Draft for validation  
**Market focus:** Nigeria-first

## Purpose and goals
MVP 1 helps value-chain participants represent supply and demand in structured ways and discover relevant opportunities. It should support accounts, profiles, a controlled product catalogue, listings, search, buyer requests, seller responses and basic messaging.

## Non-goals
In-app payments, escrow, wallets, delivery fleet management, guaranteed fulfilment, automated disputes, public seller ratings, AI forecasting, personalised AI recommendations and native mobile applications.

## Roles
| Role | Initial capability |
|---|---|
| FARMER | Manage profile/listings; respond to relevant requests |
| BUYER | Search listings; create requests; review responses |
| SUPPLIER | List inputs/products; respond to relevant requests |
| SERVICE_PROVIDER | Maintain service profile; respond to scoped enquiries |
| ADMIN | Moderate accounts/listings and support operations |

Decide whether accounts can hold multiple roles before enforcing role exclusivity.

## Functional requirements
### FR-01 Accounts
Registration, sign-in/out, duplicate prevention, secure password hashing and protected operations. Account recovery and contact verification are launch considerations.

### FR-02 Profiles
Role-aware profiles with display/business name, farm/business description and public contact preferences. Use country/state/LGA and optional market/community references. Keep private account data separate from public fields.

### FR-03 Catalogue
Controlled product categories, product names and units to reduce inconsistent data.

### FR-04 Listings
Authorised sellers create, edit, pause and close their own listings. Records include product, quantity/unit, decimal price/currency, location, availability, delivery/pick-up information and timestamps. Optional poultry attributes include bird age and average weight. Suggested statuses: DRAFT, ACTIVE, PAUSED, CLOSED, EXPIRED.

### FR-05 Search
Search by product/category and location, with filters for quantity, price and product attributes where data exists. Results communicate that offers are not guaranteed transactions.

### FR-06 Buyer requests
Capture product, quantity/unit, specifications, delivery/pick-up location, needed-by window and optional budget. Buyers manage and close their own requests.

### FR-07 Seller responses
Capture proposed quantity, price/currency, availability, delivery terms and message. A response is not an order or binding payment instruction.

### FR-08 Messaging
Contextual buyer–seller communication. Restrict access to participants; define reporting, blocking, retention and moderation before broad launch.

## Data quality requirements
Quantity has an explicit unit. Monetary amounts use decimal precision and currency. Advertised price, buyer budget, response price and transaction price remain distinct. Store timestamps in UTC. Use controlled geographic references. Timestamp listing availability and treat it as potentially stale. Treat user-entered text as untrusted.

## Non-functional requirements
Security, privacy, reliability, paginated APIs, indexed query paths, accessibility, responsive mobile UX, maintainable modular design, automated tests and privacy-conscious observability.

## MVP acceptance criteria
Authentication/authorisation tests pass; profiles, listings, search, requests and responses work; messaging is access-controlled; critical flows work on mobile; support/moderation/privacy processes are documented; and a supervised pilot has produced recorded findings.

## Open decisions
Supported identity methods; phone verification policy; multi-role accounts; required vs optional poultry attributes; location granularity; public contact policy; moderation rules; and consented signals for market intelligence.
