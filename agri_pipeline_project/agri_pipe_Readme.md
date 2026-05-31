# Agricultural Market Data Pipeline

## Project Overview

This project is a production-style Data Engineering pipeline built using Python, Pandas, SQLite, Apache Airflow and Parquet. The objective is to ingest agricultural market data, perform data quality validation, track data lineage, reconcile processing results, store data efficiently, and generate analytical reports.

The project follows industry-standard ETL (Extract, Transform, Load) practices and serves as a foundation for future integrations with Snowflake, dbt, Databricks, PySpark, and cloud platforms.

---

## Project Objectives

* Build a reusable and scalable ETL pipeline.
* Validate incoming market data.
* Detect and report data quality issues.
* Track data lineage using audit columns.
* Reconcile source and processed records.
* Store processed data in Parquet format.
* Load curated data into SQLite.
* Perform analytical queries using advanced SQL.
* Generate reports and logs for monitoring.

---

## Technology Stack

| Component            | Technology |
| -------------------- | ---------- |
| Programming Language | Python     |
| Data Processing      | Pandas     |
| Database             | SQLite     |
| File Storage         | Parquet    |
| Configuration        | YAML       |
| Logging              | Loguru     |
| SQL Analytics        | SQLite SQL |
| Documentation        | Markdown   |
| Orchestration        | Airflow    |
---

## Project Structure

```text
project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── parquet/
│
├── reports/
│   ├── validation_report.csv
│   ├── reconciliation_report.csv
│   └── analytics_report.csv
│
├── logs/
│   └── pipeline.log
│
├── docs/
│   └── data_dictionary.md
│
├── config/
│   └── config.yaml
│
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── validate_data.py
│   ├── reconcile_data.py
│   ├── analytics.py
│   └── database.py
│
├── sql/
│   └── analytics_queries.sql
│
├── database/
│   └── market_data.db
│
├── main.py
│
└── README.md
```

---

## Pipeline Architecture

```text
Raw Data
     │
     ▼
Data Cleaning
     │
     ▼
Validation Layer
     │
     ▼
Audit Columns
     │
     ▼
Reconciliation Layer
     │
     ▼
Parquet Storage
     │
     ▼
SQLite Database
     │
     ▼
Analytics Layer
     │
     ▼
Reports Generation
     │
     ▼
Logging & Monitoring
```

---

## Validation Layer

The validation process checks data quality before loading.

### Validation Rules

* Null value checks
* Duplicate record detection
* Negative price validation
* Empty commodity names
* Invalid date validation

### Output

```text
reports/validation_report.csv
```

### Report Columns

| Column         | Description                  |
| -------------- | ---------------------------- |
| total_records  | Total records received       |
| passed_records | Records passing validation   |
| failed_records | Records failing validation   |
| failure_reason | Validation error description |

---

## Audit Layer

The pipeline automatically tracks lineage information.

### Audit Columns

| Column              | Description                  |
| ------------------- | ---------------------------- |
| ingestion_timestamp | Data ingestion time          |
| source_file         | Source file name             |
| pipeline_run_id     | Unique pipeline execution ID |

---

## Reconciliation Layer

Ensures all records are accounted for throughout processing.

### Metrics Tracked

| Metric          | Description                    |
| --------------- | ------------------------------ |
| Source Count    | Original records               |
| Processed Count | Successfully processed records |
| Rejected Count  | Failed records                 |
| Duplicate Count | Duplicate records removed      |

### Output

```text
reports/reconciliation_report.csv
```

---

## Parquet Storage

Processed datasets are stored in Parquet format for efficient analytics and future cloud integrations.

### Example Output

```text
data/parquet/market_data.parquet
```

Benefits:

* Faster reads
* Smaller storage footprint
* Columnar format
* Compatible with Snowflake, Spark, and Databricks

---

## Database Layer

Curated data is loaded into SQLite for analysis.

### Database

```text
database/market_data.db
```

---

## SQL Analytics

Advanced SQL techniques are used for business analysis.

### Concepts Covered

* Common Table Expressions (CTEs)
* ROW_NUMBER()
* DENSE_RANK()
* LAG()
* LEAD()

### Example Analyses

* Top commodity per district
* Highest price commodity
* Market ranking analysis
* Historical price changes
* Trend analysis

---

## Data Warehouse Design

### Fact Table

```text
fact_market_prices
```

### Dimension Tables

```text
dim_commodity
dim_market
dim_date
dim_state
```

This schema provides a foundation for future migration to Snowflake or other cloud data warehouses.

---

## Reporting Layer

The pipeline generates operational and analytical reports.

### Reports

```text
reports/
```

Files:

```text
validation_report.csv
reconciliation_report.csv
analytics_report.csv
```

---

## Logging

Pipeline execution details are captured using Loguru.

### Log File

```text
logs/pipeline.log
```

### Information Captured

* Pipeline start time
* Pipeline end time
* Records processed
* Validation failures
* Reconciliation status
* Errors and exceptions

---

## Configuration Management

Configuration settings are managed using YAML.

### Configuration File

```text
config/config.yaml
```

Example:

```yaml
raw_path: data/raw
processed_path: data/processed
parquet_path: data/parquet
database_path: database/market_data.db
report_path: reports
log_path: logs
```

---

## Future Enhancements

### Data Engineering Roadmap

#### Phase 2

* DuckDB
* Polars
* Advanced Parquet Optimization

#### Phase 3

* Snowflake
* Snowpipe
* Stages
* Tasks

#### Phase 4

* dbt
* Data Testing
* Data Lineage
* Snapshots

#### Phase 5

* Databricks
* Delta Lake
* PySpark

#### Phase 6

* AWS Deployment
* Automated Scheduling
* CI/CD Integration

---

## Learning Outcomes

By completing this project, the following skills are demonstrated:

* Data Validation
* Data Quality Management
* ETL Development
* Data Lineage Tracking
* Reconciliation Frameworks
* Parquet Storage
* SQL Analytics
* Star Schema Design
* Logging and Monitoring
* Production Pipeline Design

---

## Author

Sunil Nakka

Associate Developer | Database Engineering | Cloud Technologies | Data Engineering

Project Goal:

Build a production-style data engineering pipeline and establish a strong foundation for Snowflake, dbt, Databricks, and PySpark.
