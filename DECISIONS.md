# DECISIONS.md

# Overview

This document captures major implementation decisions, assumptions, and tradeoffs made during development of the ESG ingestion prototype.

The assignment intentionally left several architectural and domain ambiguities open-ended. The goal of this document is to explain how those ambiguities were resolved.

---

# 1. SAP Integration Strategy

## Decision

Used CSV export ingestion rather than direct SAP API integration.

## Why

Real-world SAP integrations are highly organization-specific and often involve:
- IDocs
- BAPIs
- OData services
- middleware layers

For a 4-day prototype, CSV ingestion was selected because:
- it reflects a common operational workflow
- sustainability teams frequently export SAP data manually
- it keeps focus on normalization and analyst review

## Realistic Considerations Included

The prototype intentionally included:
- German column headers
- plant codes
- vendor names
- cost center references
- inconsistent units

to simulate common SAP export challenges.

---

# 2. Utility Data Strategy

## Decision

Used CSV exports from utility portals instead of PDF parsing or direct APIs.

## Why

Many facilities teams still rely on:
- downloadable portal exports
- emailed billing spreadsheets

rather than structured APIs.

CSV ingestion provided:
- realistic operational workflow
- lower implementation complexity
- easier analyst validation

## Explicitly Ignored

The prototype does not handle:
- PDF OCR
- scanned bills
- utility-specific APIs
- tariff complexity calculations

These were considered out of scope for the prototype timeline.

---

# 3. Corporate Travel Strategy

## Decision

Used simplified CSV exports modeled after Concur/Navan reporting formats.

## Why

Corporate travel platforms typically expose:
- employee travel records
- airport codes
- travel categories
- trip dates

CSV ingestion allowed simulation of:
- flights
- taxi travel
- hotel-related activity

without implementing OAuth or third-party API integrations.

---

# 4. Normalization Design

## Decision

Normalized all ingestion sources into a single EmissionRecord model.

## Why

The primary analyst workflow is review and approval of emissions activity rather than source-specific processing.

A centralized normalized table simplified:
- filtering
- analyst review
- suspicious detection
- audit logging
- scope categorization

while still preserving source provenance through DataSource and RawUpload models.

---

# 5. Emission Factor Strategy

## Decision

Used simplified static emission factors.

## Why

The assignment focuses primarily on ingestion, normalization, and analyst review workflows rather than scientific carbon accounting accuracy.

A simplified factor approach reduced unnecessary complexity while still demonstrating normalization architecture.

---

# 6. Validation Strategy

## Decision

Implemented lightweight validation rules:
- invalid units
- negative quantities
- suspiciously large values

## Why

The prototype prioritizes surfacing analyst-reviewable anomalies rather than fully automated validation pipelines.

The goal was to demonstrate:
- operational review workflows
- suspicious record highlighting
- audit-safe approvals

---

# 7. Analyst Approval Workflow

## Decision

Approved records become locked for audit.

## Why

The assignment explicitly referenced:
- analyst signoff
- audit readiness

Locking records after approval simulates real ESG assurance workflows where finalized records should not be editable without traceability.

---

# 8. Frontend Design Strategy

## Decision

Built a lightweight analyst dashboard rather than a highly stylized UI.

## Why

The assignment prioritizes:
- operational usability
- workflow clarity
- data review efficiency

over visual complexity.

The interface was intentionally optimized for:
- reviewing large datasets
- identifying suspicious records
- approving/rejecting records quickly

---

# 9. Multi-Tenancy Design

## Decision

Added Company-level isolation.

## Why

Enterprise ESG systems typically support multiple client organizations.

Even though the prototype only demonstrates one company, the schema was designed to support future tenant isolation.

---

# 10. Questions I Would Ask The PM

If additional product clarification were available, I would ask:

1. Should emissions factors be organization-configurable?
2. Are uploads expected to be analyst-driven or automated?
3. Should approved records be versioned after edits?
4. What level of emissions calculation accuracy is required?
5. Are utility PDFs considered mandatory ingestion sources?
6. Should data quality scoring be added?
7. Are auditors expected to access the platform directly?