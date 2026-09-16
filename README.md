Retail Sales & Customer Analytics

A practical end-to-end portfolio project that moves synthetic retail data from raw CSV files through Python validation and transformation into SQL Server and a Power BI dashboard.

The fictional retailer sells through physical stores and an online channel. The data covers customers, products, stores, sales, sale items, promotions and returns.

Data Pipeline

Raw CSV files -> Python and pandas -> SQL Server staging tables -> relational reporting model and views -> Power BI

Planned Workflow

Extract - Read seven related CSV files and check their expected structure.

Transform - Standardize data types and dates, handle missing values and duplicates, and apply basic business rules.

Load - Use Python and pyodbc to load validated data into SQL Server staging tables.

Model - Use T-SQL to populate clean relational tables with primary and foreign keys and create reusable reporting views.

Analyze - Answer business questions about revenue, trends, channels, customers, products, promotions and returns.

Report - Build a Power BI dashboard with a small set of clear KPIs and DAX measures.

Technology Stack

Python 3

pandas

pyodbc and Microsoft ODBC Driver for SQL Server

Microsoft SQL Server / SQL Server Management Studio

T-SQL

Power BI Desktop / DAX

Git / GitHub

Planned Data Model

Customers

Products

Stores

Sales

SaleItems

Promotions

Returns
