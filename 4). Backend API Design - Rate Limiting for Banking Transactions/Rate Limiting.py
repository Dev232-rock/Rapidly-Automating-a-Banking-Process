import time
from collections import deque

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.request_logs = {}

    def is_allowed(self, user_id):
        current_time = time.time()
        
        if user_id not in self.request_logs:
            self.request_logs[user_id] = deque()
        
        user_requests = self.request_logs[user_id]
        
        # Remove outdated requests
        while user_requests and user_requests[0] < current_time - self.time_window:
            user_requests.popleft()
        
        if len(user_requests) < self.max_requests:
            user_requests.append(current_time)
            return True  # Allow request
        
        return False  # Deny request

# Example
limiter = RateLimiter(max_requests=5, time_window=1)

user = "user_123"
for i in range(10):
    if limiter.is_allowed(user):
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Blocked")
    time.sleep(0.2)  # Simulating request interval
