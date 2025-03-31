require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// Simulated AI-based classification function
function classifyDispute(description) {
    const keywords = {
        "fraud": "Fraud",
        "unauthorized": "Unauthorized Transaction",
        "billing error": "Billing Issue",
        "service issue": "Service Dispute",
        "chargeback": "Chargeback",
    };

    for (let key in keywords) {
        if (description.toLowerCase().includes(key)) {
            return keywords[key];
        }
    }
    return "General Inquiry";
}

// Priority assignment based on customer history
function assignPriority(customerType, disputeType) {
    if (customerType === "VIP" || disputeType === "Fraud") {
        return "High";
    } else if (customerType === "Regular" && disputeType === "Billing Issue") {
        return "Medium";
    } else {
        return "Low";
    }
}

// AI-based recommendation system
function generateRecommendation(disputeType, amount) {
    if (disputeType === "Fraud") {
        return "Escalate immediately to Fraud Team.";
    } else if (amount > 1000) {
        return "Request further verification from the customer.";
    } else {
        return "Process normally through dispute resolution team.";
    }
}

// API Endpoint
app.post('/api/disputes', (req, res) => {
    const { customerId, customerType, description, amount } = req.body;

    if (!customerId || !customerType || !description || amount == null) {
        return res.status(400).json({ error: "Missing required fields." });
    }

    const disputeType = classifyDispute(description);
    const priority = assignPriority(customerType, disputeType);
    const recommendation = generateRecommendation(disputeType, amount);

    const response = {
        customerId,
        disputeType,
        priority,
        recommendation,
    };

    res.json(response);
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
