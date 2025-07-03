from fastapi import APIRouter, HTTPException
from .models import Supplier
from .database import get_suppliers, get_supplier_by_id

router = APIRouter()

@router.get("/suppliers", response_model=list[Supplier])
async def read_suppliers():
    suppliers = await get_suppliers()
    return suppliers

@router.get("/suppliers/{supplier_id}", response_model=Supplier)
async def read_supplier(supplier_id: int):
    supplier = await get_supplier_by_id(supplier_id)
    if supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier