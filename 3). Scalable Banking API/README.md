# Scalable Banking API - Transaction Processing & Consistency

## Overview
This project is a scalable banking API built using **FastAPI** and **PostgreSQL**, designed to process millions of banking transactions efficiently while ensuring **high consistency, low latency, and resilience to failures**.

## Features
- **RESTful API** with endpoints for debit, credit, and balance inquiry operations.
- **Atomic Transactions** to prevent partial updates.
- **Concurrency Safety** using row-level locking (`SELECT ... FOR UPDATE`).
- **Error Handling** with meaningful HTTP responses.
- **Optimized Performance** with indexing and future support for caching.

## Technologies Used
- **FastAPI** (Web framework)
- **SQLAlchemy** (ORM for database interactions)
- **PostgreSQL** (Relational database)
- **Docker** (Optional for containerization)

## API Endpoints
### 1. Process a Transaction (Debit/Credit)
```bash
POST /transaction
Request Body:
{
  "account_id": 1,
  "amount": 100.50,
  "transaction_type": "debit"
}
Response:
{
  "message": "Transaction successful"
}
## 2. Get Account Balance
```bash
GET /balance/{account_id}
Response:
{
  "account_id": 1,
  "balance": 500.00
}
Database Schema
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    balance DECIMAL(20, 2) NOT NULL DEFAULT 0.00
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT REFERENCES accounts(account_id),
    amount DECIMAL(20, 2) NOT NULL,
    transaction_type VARCHAR(10) CHECK (transaction_type IN ('debit', 'credit')),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
