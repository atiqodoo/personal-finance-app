from fastapi import APIRouter
from .auth import router as auth_router
from .wallets import router as wallets_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])
api_router.include_router(wallets_router, prefix="/wallets", tags=["wallets"])
