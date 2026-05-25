# MODEL.md

## Overview

The system was designed as a multi-tenant ESG ingestion and analyst review platform capable of handling emissions-related data from multiple enterprise systems.

The primary design goal was normalization of heterogeneous source data into a consistent reviewable emissions model while preserving source traceability and auditability.

---

# Core Design Principles

1. Multi-source ingestion
2. Immutable audit trail
3. Source traceability
4. Analyst review workflow
5. Scope 1/2/3 categorization
6. Unit normalization
7. Suspicious data detection

---

# Data Model

## Company

Represents a tenant organization.

Fields:
- id
- name

Purpose:
Supports multi-tenancy by isolating uploaded records per organization.

---

## DataSource

Represents a logical ingestion event/source.

Fields:
- company
- source_type
- uploaded_at
- uploaded_by

Supported source types:
- SAP
- Utility
- Travel

Purpose:
Tracks provenance of uploaded emissions data.

---

## RawUpload

Stores original uploaded source files.

Fields:
- source
- file
- original_filename
- uploaded_at

Purpose:
Preserves source-of-truth raw evidence for auditability.

---

## EmissionRecord

Central normalized emissions table.

Fields:
- company
- source
- activity_type
- scope
- quantity
- unit
- normalized_quantity
- normalized_unit
- emission_factor
- emission_value
- record_date
- status
- suspicious_flag
- validation_message
- source_row_id
- locked
- created_at

Purpose:
Represents normalized emissions activity records across all ingestion systems.

This model intentionally centralizes normalized emissions data to simplify analyst review workflows.

---

# Scope Classification

Scope mapping strategy:

| Source | Scope |
|---|---|
| SAP Fuel | Scope 1 |
| Utility Electricity | Scope 2 |
| Corporate Travel | Scope 3 |

---

# Audit Model

## AuditLog

Tracks analyst modifications and workflow changes.

Fields:
- emission_record
- field_name
- old_value
- new_value
- edited_by
- edited_at

Purpose:
Provides immutable audit history required for ESG assurance and external audits.

---

# Normalization Strategy

Different source systems expose different schemas and units.

Normalization converts:
- fuel quantities
- electricity usage
- travel distances

into standardized emissions values:
- kgCO2e

The prototype uses simplified static emission factors.

---

# Validation Strategy

Validation engine detects:
- invalid units
- negative quantities
- suspiciously high activity values

Suspicious records are highlighted for analyst review.

---

# Locking Strategy

Approved records become locked to simulate audit-safe workflows.

Locked records:
- cannot be modified
- visually indicate audit finalization

---

# Tradeoffs

The model intentionally prioritizes:
- explainability
- auditability
- review workflow simplicity

over:
- complex real-time integrations
- highly granular emissions factor engines
- event-driven architectures

This was considered appropriate for a 4-day prototype scope.