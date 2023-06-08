# DuckDB Notebook

## What Is DuckDB
- An open-source, columnar, in-process, and embeddeable RDBMS written in C++.
- Designed to be embedded directly into applications, allowing engineers to easily incorporate it into their software as a local database engine (think SQLite for OLAP). There are no client/ server setup requirements.
- Supports wide range of SQL operations including transacations, indexing, tables, and views.
- Provides transactional guarantees of Atomicity, Consistency, Isolation, and Durability (ACID) through Multi-Versioned Concurrency Control (MVCC).
- Has a bunch of client APIs: Java, Python, R, Node.

## Why DuckDB

- An embeddable DBMS that is designed to be embedded directly into applications, making it lightweight and efficient.
- Provides fast query performance on large datasets, making it suitable where performance is at the forefront.
- Provides ad-hoc analytics for CSV, PARQUET, CSV.GZ files without requiring additional libraries like pandas (join in pandas tend to be slow) or numpy.
- Supports standard SQL syntax with a familiar SQL interface, making it easy for developers familiar with SQL.
- Has a columnar-vectorized query execution engine, where queries are still interpreted, but a large batch of values ("a vector") are processed in one operation. This greatly reduces overhead present in traditional systems such as PostgreSQL, MySQL which processes each row sequentially. Vectorized query execution leads to far better performance in OLAP queries.
