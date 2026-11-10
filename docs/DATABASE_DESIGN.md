# Database Design (Logical Draft)

This is a proposed logical model, not deployed database tables. Validate during implementation.

## Core entities
- **users:** UUID, email/phone, password_hash, account_status, timestamps.
- **user_roles:** id, user_id FK, role_code (FARMER/BUYER/SUPPLIER/SERVICE_PROVIDER/ADMIN), created_at. A join table allows multi-role support if product policy permits.
- **profiles:** id, user_id FK, display_name, business_name, bio, public_contact_preferences, timestamps.
- **locations:** id, country_code, state code/name, LGA code/name, market/community name, optional coordinates and parent_location_id.
- **categories:** id, unique code, name, optional parent and active flag.
- **products:** id, category_id FK, name, description, default unit and active flag.
- **listings:** id, seller_user_id, product_id, title/description, quantity_available DECIMAL, quantity_unit, unit_price DECIMAL, currency_code, location_id, availability/listing status, optional availability dates, delivery flag, optional average_weight_kg and age value/unit, timestamps.
- **listing_media:** id, listing_id, object_key, media_type, sort_order, created_at.
- **buyer_requests:** id, buyer_user_id, product_id, title/description, quantity_required DECIMAL, unit, optional budget range/currency, destination_location_id, needed-by window, delivery flag, status and timestamps.
- **seller_responses:** id, request_id, seller_user_id, quantity_offered DECIMAL, unit, unit_price DECIMAL, currency, message, availability window, status and timestamps.
- **conversations / participants / messages:** contextual links, participants and timestamped messages; enforce participant access on every read/write.
- **audit_events:** actor, action, target type/id, timestamp and limited metadata.

## Design rules
Use UUIDs for externally exposed entities unless justified otherwise. Use DECIMAL/NUMERIC for money and quantities. Store ISO currency codes (e.g. NGN). Separate listing price, buyer budget, response price and confirmed transaction price. Use UTC timestamps, foreign keys and reviewed deletion policies.

## Market intelligence readiness
Potential events include listing created/updated/closed, availability changes, request created/closed, seller response created and confirmed transaction (only with a defined, evidenced confirmation flow and consent). Never infer completed trades from price or message activity.
