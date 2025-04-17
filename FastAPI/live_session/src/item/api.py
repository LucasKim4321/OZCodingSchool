from fastapi import APIRouter


router = APIRouter(prefix="/items", tags=["Item"])

@router.get("")
def get_items():
    return [
        {"id":1, "name": "apple", "price": 100},
        {"id":2, "name": "banana", "price": 200},
        {"id":3, "name": "cherry", "price": 300},
    ]