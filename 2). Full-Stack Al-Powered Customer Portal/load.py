from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# Define the input model
class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    credit_score: int
    loan_amount: float

# Function to calculate loan eligibility
def calculate_loan_eligibility(data: LoanApplication):
    score = (data.credit_score / 850) * 50 + (data.income / 100000) * 30 - (data.loan_amount / 50000) * 20
    score = max(0, min(100, score))  # Ensure score is between 0-100

    if score > 75:
        recommendation = "Highly Recommended"
    elif score > 50:
        recommendation = "Recommended with Caution"
    else:
        recommendation = "Not Recommended"

    return {"eligibility_score": round(score, 2), "recommendation": recommendation}

# API endpoint
@app.post("/loan-eligibility/")
async def loan_eligibility(application: LoanApplication):
    try:
        response = calculate_loan_eligibility(application)
        return {"name": application.name, **response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

