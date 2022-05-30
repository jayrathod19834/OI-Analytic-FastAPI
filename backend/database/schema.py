from datetime import date
from pydantic import BaseModel

class login_user(BaseModel):
    email: str
    password: str

class show_user(BaseModel):
    fullname: str
    email: str
    role_id: int
    c_id: int
    working_under: int
    class Config:
        orm_mode = True

class add_user_superadmin(BaseModel):
    c_id: int
    fullname: str
    email: str
    password: str
    role_id: int
    conact_no : str
    working_under: int
    dob: date
    class Config:
        orm_mode = True

class update_user(BaseModel):
    c_id: int
    fullname: str
    email: str
    role_id: int
    contact_no : str
    working_under: int
    dob: date

class add_company(BaseModel):
    company_name: str
    country: str
    state: str
    city: str
    pincode: str
    department: str
    branch: str
    address: str

class list_company(add_company,BaseModel):
    company_id: int
    class Config:
        orm_mode = True
