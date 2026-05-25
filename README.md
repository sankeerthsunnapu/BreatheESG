# Breathe ESG – ESG Data Ingestion & Review Platform

## Overview

Breathe ESG is a prototype ESG ingestion and analyst review platform built using Django REST Framework and React.

The platform ingests emissions-related operational data from multiple enterprise systems, normalizes heterogeneous formats into a unified emissions model, surfaces suspicious records for analyst review, and maintains audit-safe approval workflows.

This project was developed as part of the Breathe ESG technical assignment.

---

# Live Deployment

## Frontend

Add your Vercel URL here:

```txt
https://breathe-esg-one.vercel.app
```

---

## Backend API

```txt
https://breathe-esg-backend-8b2s.onrender.com
```

---

# Features

## Multi-Source ESG Ingestion

Supports ingestion from:
- SAP fuel/procurement exports
- utility electricity exports
- corporate travel exports

---

## Data Normalization

Converts heterogeneous operational data into:
- standardized emissions records
- normalized units
- kgCO2e emissions values

---

## Validation Engine

Detects:
- invalid units
- negative quantities
- suspiciously large activity values

Suspicious records are highlighted for analyst review.

---

## Analyst Review Workflow

Analysts can:
- review uploaded records
- approve/reject entries
- filter/search records
- identify suspicious data

Approved records become locked for audit safety.

---

## Audit Trail

Tracks:
- approval/rejection actions
- field changes
- timestamps

through immutable audit logs.

---

# Technology Stack

## Backend

- Django
- Django REST Framework
- PostgreSQL
- Pandas

---

## Frontend

- React
- Vite
- Tailwind CSS
- Axios

---

# Project Structure

```txt
BreatheESG/
│
├── backend/
│   ├── config/
│   ├── emissions/
│   ├── requirements.txt
│   └── manage.py
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── MODEL.md
├── DECISIONS.md
├── TRADEOFFS.md
├── SOURCES.md
└── README.md
```

---

# Supported Source Types

| Source | Example Format | Scope |
|---|---|---|
| SAP Fuel Data | CSV Export | Scope 1 |
| Utility Electricity | Portal CSV Export | Scope 2 |
| Corporate Travel | Concur-style CSV | Scope 3 |

---

# Example Workflows

## Upload ESG Data

Users can upload:
- SAP CSVs
- utility CSVs
- travel CSVs

through the web dashboard.

---

## Analyst Review

Uploaded records appear in a centralized dashboard where analysts can:
- filter records
- review suspicious activity
- approve/reject records
- review audit history

---

# Deployment Notes

## Backend Deployment

Backend deployed using:
- Render
- PostgreSQL

---

## Frontend Deployment

Frontend deployed using:
- Vercel

---

# Important Prototype Notes

This implementation intentionally prioritizes:
- ingestion workflows
- normalization
- analyst review
- auditability

over:
- real SAP integrations
- OCR pipelines
- production-grade emissions factor engines

Additional details are documented in:
- MODEL.md
- DECISIONS.md
- TRADEOFFS.md
- SOURCES.md

---

# Local Development

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Future Improvements

Potential future enhancements:
- real SAP/OData integrations
- PDF utility bill OCR
- asynchronous ingestion pipelines
- configurable emissions factors
- role-based access control
- advanced anomaly detection

---

# Author

Sankeerth Sunnapu