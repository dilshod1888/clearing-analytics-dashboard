# Clearing Analytics Dashboard

A portfolio project demonstrating a banking and payment clearing analytics solution built around PostgreSQL, SQL, and Power BI.

## Business Goal

Clearing operations generate large volumes of transaction data from multiple payment channels. This project demonstrates how operational and financial data can be transformed into executive dashboards for monitoring transaction activity, clearing positions, commissions, and reconciliation KPIs.

> **Important:** All data in this repository is synthetic. No confidential banking, customer, or production data is included.

## Dashboard Areas

- Executive Summary
- Transaction Analytics
- Clearing & Settlement
- Commission Analytics
- Operational & Reconciliation Monitoring

## Key KPIs

| KPI | Description |
|---|---|
| Transaction Count | Total processed transactions |
| Transaction Amount | Total transaction value |
| Net Clearing Position | Incoming amount minus outgoing amount |
| Commission Revenue | Calculated processing/interchange revenue |
| Reconciliation Rate | Matched transactions as a percentage |
| Processing Success Rate | Successfully processed files/sessions |

## Architecture

```
Synthetic Transaction Data
          ↓
     PostgreSQL
          ↓
    SQL Analytics
          ↓
      Power BI
          ↓
Executive Dashboard
```

## Repository Structure

```
clearing-analytics-dashboard/
├── data/          # Synthetic sample data
├── sql/           # Schema and analytical queries
├── docs/          # Business and KPI documentation
├── powerbi/       # Power BI project documentation
├── images/        # Dashboard screenshots
└── README.md
```

## Technologies

**PostgreSQL · SQL · Power BI · Python (optional ETL/data generation)**

## Portfolio Value

This project is designed to demonstrate practical skills in financial data analytics, transaction processing, database analytics, KPI design, and executive dashboard development.
