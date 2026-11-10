# Security and Privacy Baseline

## Identity and access
Use a reviewed password hashing algorithm. Never log passwords, tokens or secrets. Define a secure session/token and recovery flow. Enforce role and resource ownership on the server. Audit privileged actions and rate-limit authentication, recovery and user-generated activity.

## Application security
Validate input, use parameterised database access, escape user content, configure CORS narrowly, require HTTPS outside local development, review dependencies, protect against spam/scraping and validate uploads by size/type/signature. Select appropriate CSRF protections for the chosen authentication mechanism.

## Privacy
Minimise collection; explain public profile/listing fields; separate private contact and credential data; define retention, access, correction and deletion processes; restrict conversation access. Review applicable Nigerian data-protection obligations with qualified counsel before launch.

## Operations
Use secret management, backups with restoration tests, incident response and access revocation. Avoid production personal data in development and tests.

## Launch blockers
Complete threat modelling, privacy review, dependency scan, access-control tests, backup/restore test and incident response runbook.
