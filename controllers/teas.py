from fastapi import APIRouter, HTTPException
from models.tea_data import teas_db

router = APIRouter()


@router.get("/teas")
def get_teas():
    return teas_db


@router.get("/teas/{tea_id}")
def get_single_tea(tea_id: int):
    for tea in teas_db["teas"]:
        if tea["id"] == tea_id:
            return tea

    raise HTTPException(status_code=404, detail="Tea not found")


@router.post("/teas")
def create_tea(tea: dict):
    teas_db["teas"].append(tea)
    return tea


@router.put("/teas/{tea_id}")
def update_tea(tea_id: int, tea: dict):
    for existing_tea in teas_db["teas"]:
        if existing_tea["id"] == tea_id:
            existing_tea.update(tea)
            return existing_tea

    raise HTTPException(status_code=404, detail="Tea not found")


@router.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for tea in teas_db["teas"]:
        if tea["id"] == tea_id:
            teas_db["teas"].remove(tea)
            return {"message": f"Tea with ID {tea_id} has been deleted."}

    raise HTTPException(status_code=404, detail="Tea not found")