from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, DECIMAL, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import text

DATABASE_URL = "postgresql://user:password@localhost/banking_db"  # paste your DB Link 
#mine is postgresql://dev:1*34@56**@/5432/banking_db
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

app = FastAPI()

class Account(Base):
    __tablename__ = "accounts"
    account_id = Column(Integer, primary_key=True, index=True)
    balance = Column(DECIMAL(20, 2), nullable=False, default=0.00)

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.account_id"))
    amount = Column(DECIMAL(20, 2), nullable=False)
    transaction_type = Column(String(10))

Base.metadata.create_all(bind=engine)

class TransactionRequest(BaseModel):
    account_id: int
    amount: float
    transaction_type: str

@app.post("/transaction")
def process_transaction(request: TransactionRequest):
    session = SessionLocal()
    
    if request.transaction_type not in ["debit", "credit"]:
        raise HTTPException(status_code=400, detail="Invalid transaction type")

    try:
        session.execute(text("BEGIN"))

        account = session.query(Account).filter(Account.account_id == request.account_id).with_for_update().first()
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        if request.transaction_type == "debit":
            if account.balance < request.amount:
                raise HTTPException(status_code=400, detail="Insufficient funds")
            account.balance -= request.amount
        else:  # Credit
            account.balance += request.amount

        transaction = Transaction(
            account_id=request.account_id,
            amount=request.amount,
            transaction_type=request.transaction_type
        )

        session.add(transaction)
        session.commit()
        return {"message": "Transaction successful"}

    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=500, detail="Transaction failed")
    finally:
        session.close()

@app.get("/balance/{account_id}")
def get_balance(account_id: int):
    session = SessionLocal()
    account = session.query(Account).filter(Account.account_id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account_id": account_id, "balance": account.balance}
