# Rate Limiter for Banking Transactions

## Overview
This project implements a **rate limiter** to control transaction requests in a banking system. It prevents fraudulent users from spamming transactions while ensuring genuine users can operate smoothly.

## Features
- Limits each user to **5 requests per second**.
- Uses a **Sliding Window Log** algorithm for precise control.
- Efficient **deque-based** implementation for fast request tracking.
- Simple and lightweight Python solution.

## Technologies Used
- Python 3.x
- `collections.deque` for efficient request tracking
- `time` module for timestamp management

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/rate-limiter.git
   cd rate-limiter
Install dependencies
pip install -r requirements.txt
Run the script
python rate_limiter.py

Example:
```sh
limiter = RateLimiter(max_requests=5, time_window=1)

user = "user_123"
for i in range(10):
    if limiter.is_allowed(user):
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Blocked")
    time.sleep(0.2)
