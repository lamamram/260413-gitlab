from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.database import get_db
from app.models.employee import Employee as EmployeeModel
from app.schemas.employee import Employee

router = APIRouter()


@router.get("/employees/list", response_model=List[Employee])
async def list_employees(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """Liste tous les employés avec pagination."""
    employees = db.query(EmployeeModel).offset(skip).limit(limit).all()
    return employees


@router.get("/employees/{employee_id}", response_model=Employee)
async def get_employee(employee_id: int, db: Session = Depends(get_db)):
    db_user = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
