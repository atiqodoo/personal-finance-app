from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...database import get_db

router = APIRouter()

@router.get("/", response_model=List[dict])
def get_wallets(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all wallets - Demo version with sample data"""
    demo_wallets = [
        {
            "id": 1,
            "name": "Main Checking",
            "description": "Primary bank account",
            "currency": "USD",
            "wallet_type": "bank",
            "current_balance": 1250.50,
            "created_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 2,
            "name": "Cash Wallet",
            "description": "Physical cash",
            "currency": "USD", 
            "wallet_type": "cash",
            "current_balance": 150.25,
            "created_at": "2024-01-01T00:00:00Z"
        }
    ]
    return demo_wallets

@router.get("/{wallet_id}", response_model=dict)
def get_wallet(wallet_id: int, db: Session = Depends(get_db)):
    """Get a specific wallet - Demo version"""
    return {
        "id": wallet_id,
        "name": f"Wallet {wallet_id}",
        "description": "Sample wallet",
        "currency": "USD",
        "wallet_type": "bank",
        "current_balance": 1000.00
    }
