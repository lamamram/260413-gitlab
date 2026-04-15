from pydantic import BaseModel


class EmployeeBase(BaseModel):
    full_name: str
    seniority: int


class EmployeeCreate(EmployeeBase):
    user_id: int


class EmployeeUpdate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
