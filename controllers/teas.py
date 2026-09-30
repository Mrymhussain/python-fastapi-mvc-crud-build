from fastapi import APIRouter
from models.tea_data import teas_db

router = APIRouter()


@router.get("/teas")
def get_teas():
    return teas_db