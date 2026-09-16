# Project Plan

## Business Scenario

The project represents a fictional retail company that sells products through physical stores and an online channel.

The source data covers customers, products, stores, sales transactions, promotions and product returns. The goal is to build a small, traceable batch data pipeline and use the prepared data to answer practical business questions.

## Pipeline Scope

1. Generate reproducible raw CSV files with Python.
2. Validate and transform the raw files with pandas.
3. Save rejected records and a short pipeline run summary.
4. Load valid records into SQL Server staging tables with pyodbc.
5. Populate clean relational tables with T-SQL.
6. Create reusable reporting views and analysis queries.
7. Connect Power BI to the reporting layer and create DAX measures.
8. Add automated data-quality tests and a basic GitHub Actions workflow.

## Questions to Explore

- How much revenue does the company generate?
- Which products and categories perform best?
- Which stores generate the most sales?
- How do online and in-store sales compare?
- Which customers spend the most?
- How many customers return for additional purchases?
- Which products have the highest return rates?
- Do promotions appear to increase sales?
- How does revenue change over time?

## Core Tables

- Customers
- Products
- Stores
- Sales
- SaleItems
- Promotions
- Returns

## Planned Output

- Reproducible raw dataset
- Python batch pipeline
- Rejected-row reports and data-quality summary
- SQL Server staging and clean relational layers
- SQL analysis queries and reporting views
- Power BI dashboard
- Data dictionary and lineage notes
- Automated tests
- Short summary of business findings

## Scope Boundary

The first complete version runs locally with Python and SQL Server. A small Microsoft Fabric or Azure extension may be added only after the local pipeline is complete and documented.
