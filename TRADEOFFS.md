# TRADEOFFS.md

# Overview

This prototype intentionally prioritized:
- ingestion architecture
- normalization
- analyst workflows
- auditability

over production-scale infrastructure and deep carbon-accounting complexity.

Given the 4-day timeline, several features were intentionally deferred.

---

# 1. No Direct SAP Integration

## Not Built

Did not implement:
- SAP OData APIs
- BAPI integrations
- IDoc ingestion
- SAP middleware connectivity

## Why

Real SAP integrations are:
- organization-specific
- security-heavy
- infrastructure-dependent

Implementing realistic enterprise SAP connectivity would have consumed the majority of the prototype timeline while contributing little to the analyst workflow evaluation goals.

CSV ingestion was selected as a realistic operational compromise.

---

# 2. No PDF OCR Utility Parsing

## Not Built

Did not implement:
- OCR pipelines
- PDF bill extraction
- scanned utility invoice parsing

## Why

Utility PDFs introduce:
- OCR reliability challenges
- vendor-specific formatting issues
- complex parsing edge cases

The prototype instead focused on structured CSV exports because:
- they are commonly available from utility portals
- they better demonstrate normalization workflows
- they reduce noise unrelated to core architecture

---

# 3. No Real Emissions Factor Engine

## Not Built

Did not implement:
- EPA factor datasets
- DEFRA mappings
- dynamic regional emissions factors
- year-specific factor versioning

## Why

The assignment primarily evaluates:
- ingestion
- normalization
- review workflows
- auditability

rather than scientific carbon accounting precision.

Static placeholder emission factors were sufficient to demonstrate normalization architecture without introducing unnecessary complexity.

---

# 4. No Authentication System

## Not Built

Did not implement:
- JWT authentication
- RBAC
- SSO
- organization-level permissions

## Why

The prototype focused on ESG operational workflows rather than identity infrastructure.

Adding enterprise-grade authentication would significantly increase implementation scope without improving the core ingestion and analyst review demonstration.

---

# 5. No Background Processing Pipeline

## Not Built

Did not implement:
- Celery workers
- asynchronous ingestion
- queue-based processing

## Why

The uploaded datasets in the prototype are small enough for synchronous processing.

Background infrastructure was considered unnecessary complexity for a prototype-scale workload.

---

# 6. No Versioned Record Editing

## Not Built

Did not implement:
- record version history
- rollback workflows
- soft-deletion recovery

## Why

The prototype instead used:
- audit logs
- approval locking

to demonstrate audit-safe workflows at lower implementation complexity.

---

# 7. No Advanced Data Quality Engine

## Not Built

Did not implement:
- statistical anomaly detection
- ML-based validation
- duplicate clustering
- predictive quality scoring

## Why

The prototype intentionally kept validation explainable and transparent for analysts.

Simple deterministic validation rules were easier to review and defend during evaluation.

---

# 8. No Granular ESG Taxonomy

## Not Built

Did not implement:
- subcategory-level Scope 3 mappings
- supplier emissions hierarchies
- lifecycle analysis modeling

## Why

The assignment focused on ingestion workflows rather than comprehensive ESG ontology design.

The simplified Scope 1/2/3 structure provided enough realism without excessive domain complexity.

---

# Final Reflection

The implementation intentionally optimized for:
- clarity
- realism
- explainability
- reviewability

rather than attempting to simulate every aspect of a production ESG platform.

The resulting prototype demonstrates:
- realistic enterprise ingestion patterns
- normalization workflows
- analyst review operations
- audit-safe approval processes

within the constraints of a short prototype timeline.