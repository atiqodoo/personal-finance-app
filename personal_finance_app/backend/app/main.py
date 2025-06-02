from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI(
    title="Personal Finance App",
    version="1.0.0",
    description="A comprehensive personal finance management application"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Personal Finance App", 
        "version": "1.0.0",
        "status": "running",
        "docs": "Visit /docs for API documentation"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "version": "1.0.0",
        "service": "Personal Finance API"
    }

# Authentication endpoints
@app.post("/api/v1/auth/login")
async def login():
    return {
        "access_token": "demo-token-12345",
        "token_type": "bearer",
        "message": "Demo login successful"
    }

@app.post("/api/v1/auth/register")
async def register():
    return {
        "message": "User registered successfully",
        "email": "demo@example.com"
    }

@app.get("/api/v1/auth/me")
async def get_current_user():
    return {
        "id": 1,
        "email": "demo@example.com",
        "full_name": "Demo User",
        "is_verified": True
    }

# Wallet endpoints
@app.get("/api/v1/wallets")
async def get_wallets():
    return [
        {
            "id": 1,
            "name": "Main Checking",
            "description": "Primary bank account",
            "currency": "USD",
            "wallet_type": "bank",
            "initial_balance": 1000.00,
            "current_balance": 1250.50,
            "created_at": "2024-01-01T00:00:00Z",
            "is_active": True
        },
        {
            "id": 2,
            "name": "Cash Wallet",
            "description": "Physical cash",
            "currency": "USD",
            "wallet_type": "cash", 
            "initial_balance": 200.00,
            "current_balance": 150.25,
            "created_at": "2024-01-01T00:00:00Z",
            "is_active": True
        },
        {
            "id": 3,
            "name": "Savings Account",
            "description": "Emergency fund",
            "currency": "USD",
            "wallet_type": "bank",
            "initial_balance": 5000.00,
            "current_balance": 5750.00,
            "created_at": "2024-01-01T00:00:00Z",
            "is_active": True
        }
    ]

@app.post("/api/v1/wallets")
async def create_wallet():
    return {
        "id": 4,
        "name": "New Wallet",
        "description": "Demo wallet created",
        "currency": "USD",
        "wallet_type": "cash",
        "initial_balance": 0.00,
        "current_balance": 0.00,
        "message": "Wallet created successfully (demo)"
    }

@app.get("/api/v1/wallets/{wallet_id}")
async def get_wallet(wallet_id: int):
    return {
        "id": wallet_id,
        "name": f"Wallet {wallet_id}",
        "description": "Sample wallet description",
        "currency": "USD",
        "wallet_type": "bank",
        "current_balance": 1000.00,
        "created_at": "2024-01-01T00:00:00Z"
    }

# Transaction endpoints
@app.get("/api/v1/transactions")
async def get_transactions():
    return [
        {
            "id": 1,
            "description": "Grocery shopping",
            "amount": 85.50,
            "transaction_type": "expense",
            "wallet_id": 1,
            "category": "Food & Dining",
            "transaction_date": "2024-01-15T10:30:00Z",
            "created_at": "2024-01-15T10:30:00Z"
        },
        {
            "id": 2,
            "description": "Salary deposit",
            "amount": 3000.00,
            "transaction_type": "income",
            "wallet_id": 1,
            "category": "Salary",
            "transaction_date": "2024-01-01T09:00:00Z",
            "created_at": "2024-01-01T09:00:00Z"
        },
        {
            "id": 3,
            "description": "Coffee shop",
            "amount": 4.50,
            "transaction_type": "expense",
            "wallet_id": 2,
            "category": "Food & Dining",
            "transaction_date": "2024-01-14T08:15:00Z",
            "created_at": "2024-01-14T08:15:00Z"
        }
    ]

@app.get("/api/v1/transactions/summary/stats")
async def get_transaction_summary():
    return {
        "total_income": 3000.00,
        "total_expenses": 90.00,
        "net_income": 2910.00,
        "transaction_count": 3,
        "period": "Current month"
    }

# Category endpoints
@app.get("/api/v1/categories")
async def get_categories():
    return [
        {
            "id": 1,
            "name": "Food & Dining",
            "description": "Restaurants, groceries, coffee",
            "category_type": "expense",
            "color": "#FF6B6B",
            "icon": "fas fa-utensils"
        },
        {
            "id": 2,
            "name": "Transportation",
            "description": "Gas, public transport, parking",
            "category_type": "expense",
            "color": "#4ECDC4",
            "icon": "fas fa-car"
        },
        {
            "id": 3,
            "name": "Salary",
            "description": "Monthly salary",
            "category_type": "income",
            "color": "#45B7D1",
            "icon": "fas fa-dollar-sign"
        },
        {
            "id": 4,
            "name": "Freelance",
            "description": "Freelance work income",
            "category_type": "income",
            "color": "#96CEB4",
            "icon": "fas fa-laptop"
        }
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
