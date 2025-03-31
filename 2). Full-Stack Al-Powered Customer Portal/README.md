# AI-Powered Customer Portal (No-Code-First MVP)

This project is a **Full-Stack AI-Powered Customer Portal** MVP that allows users to:  
Check their account balance  
Apply for a loan with AI-based eligibility recommendations  
View dispute history and track resolution  

## Features
- **Loan Eligibility API**: Accepts customer data and returns a **loan eligibility score** with a recommendation.  
- **RESTful API**: Built using FastAPI for easy and fast responses.  
- **No-Code UI**: Designed with Bubble.io / Figma (Optional).  
- **AI-Driven Insights**: Uses basic AI logic for financial predictions.  

   
Create a Virtual Environment 
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

## Install Dependencies
- **pip install fastapi uvicorn pydantic**

## API Endpoints
## URL: POST /loan-eligibility/
## Request Body (JSON):
```bash
{
  "name": "John Doe",
  "age": 30,
  "income": 60000,
  "credit_score": 700,
  "loan_amount": 20000
}
Response Example:
{
  "name": "John Doe",
  "eligibility_score": 72.5,
  "recommendation": "Recommended with Caution"
}
