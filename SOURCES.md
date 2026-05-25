# SOURCES.md

# Overview

This prototype was designed after researching realistic enterprise ESG data ingestion workflows commonly used by sustainability and operations teams.

The assignment emphasized handling realistic source formats rather than toy examples. The ingestion strategies and sample datasets below were selected to reflect common operational workflows observed in enterprise environments.

---

# 1. SAP Fuel & Procurement Data

## Research Summary

Research focused on common SAP export mechanisms including:
- SAP GUI CSV exports
- IDoc-based integrations
- SAP OData services
- BAPI workflows

In practice, many sustainability teams still receive manually exported CSV or Excel files from finance and operations teams rather than direct SAP integrations.

---

# Chosen Format

CSV export modeled after SAP operational reports.

Example characteristics included:
- plant codes
- cost centers
- vendor names
- mixed units
- German column headers

Example columns:
- Plant_Code
- Brennstofftyp
- Menge
- Einheit
- Buchungsdatum
- Vendor_Name
- Cost_Center

---

# Why These Fields Were Chosen

The dataset intentionally simulates:
- multilingual ERP environments
- operational fuel procurement records
- enterprise accounting structures

German field names were included because multinational SAP deployments frequently contain localized terminology.

---

# Real-World Challenges Simulated

The prototype partially simulates:
- inconsistent naming conventions
- unit inconsistency
- operational metadata coupling
- export formatting variability

---

# What Would Break In Production

A production system would additionally require:
- master data mapping
- unit conversion catalogs
- vendor normalization
- duplicate detection
- incremental ingestion handling
- ERP authentication/security controls

---

# 2. Utility Electricity Data

## Research Summary

Research focused on how facilities teams typically obtain electricity consumption data.

Common workflows observed:
- utility portal CSV exports
- emailed billing spreadsheets
- PDF invoices
- limited API availability depending on utility provider

---

# Chosen Format

CSV utility export.

Example columns:
- Meter_ID
- Service_Address
- kWh_Consumed
- Tariff_Code
- Billing_Start
- Billing_End

---

# Why These Fields Were Chosen

The schema intentionally models:
- non-calendar billing periods
- utility meter identifiers
- tariff references
- location-linked consumption tracking

These patterns commonly appear in enterprise energy reporting.

---

# Real-World Challenges Simulated

The prototype partially simulates:
- billing period misalignment
- large consumption anomalies
- multiple facilities
- varying tariff structures

---

# What Would Break In Production

A production deployment would additionally require:
- PDF parsing/OCR
- interval meter handling
- utility-specific adapters
- timezone normalization
- estimated meter read handling
- renewable energy certificate attribution

---

# 3. Corporate Travel Data

## Research Summary

Research focused on corporate travel platforms such as:
- Concur
- Navan
- TravelPerk

These systems commonly expose:
- employee itineraries
- airport codes
- trip categories
- travel dates
- booking metadata

---

# Chosen Format

CSV travel export.

Example columns:
- Employee_ID
- Traveler_Name
- Travel_Category
- Origin_Airport
- Destination_Airport
- Distance_KM
- Travel_Date

---

# Why These Fields Were Chosen

The schema intentionally models:
- airport-code-based routing
- multiple travel categories
- employee-linked activity records
- long-haul flight anomalies

Airport codes were selected because many travel systems expose route metadata rather than explicit emissions calculations.

---

# Real-World Challenges Simulated

The prototype partially simulates:
- missing emissions values
- inconsistent travel categorization
- long-haul outlier detection
- mixed transportation modes

---

# What Would Break In Production

A production deployment would additionally require:
- flight distance calculation engines
- cabin-class emissions adjustments
- hotel-night conversion factors
- currency normalization
- cancelled trip reconciliation
- OAuth-secured API ingestion

---

# Final Reflection

The ingestion architecture intentionally prioritizes:
- realism
- explainability
- operational workflows
- analyst reviewability

rather than attempting to fully replicate production-scale ESG infrastructure.

The chosen formats were selected because they realistically reflect how sustainability data is frequently exchanged operationally inside enterprises today.