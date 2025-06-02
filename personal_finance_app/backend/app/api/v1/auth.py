from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ...database import get_db
from ...schemas.user import UserCreate, Token
from ...utils.security import create_access_token
from ...config import settings

router = APIRouter()

@router.post("/login", response_model=Token)
def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """Login and get access token - Demo version"""
    # For demo purposes, accept any email/password combination
    if not form_data.username or not form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please provide email and password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject=form_data.username, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=dict)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user - Demo version"""
    return {"message": "User registered successfully", "email": user.email}

@router.get("/me", response_model=dict)
def read_users_me():
    """Get current user info - Demo version"""
    return {"id": 1, "email": "demo@example.com", "full_name": "Demo User"}
