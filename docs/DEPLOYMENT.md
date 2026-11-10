# Deployment Guide (Planning)

Environments: local developer setup; isolated test/staging; production with managed database, HTTPS, backups, monitoring and secret management.

Deploy immutable builds. Apply reviewed migrations as a controlled step. Keep credentials outside the repository. Use health checks and structured logs. Configure CORS explicitly. Test database restoration and document app/schema rollback steps.

Decisions still required: hosting provider/region, database and retention policy, object storage, domain/TLS, secret manager, monitoring/alerting and privacy/data-processing requirements.

No production hosting is configured by this scaffold.
