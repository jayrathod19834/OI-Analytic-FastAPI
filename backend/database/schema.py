from typing import Optional
from pydantic import BaseModel

class login_user(BaseModel):
    email: str
    password: str

class show_user(BaseModel):
    name: str
    email: str
    role_id: str
    c_id: str
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
    dob: str
    class Config:
        orm_mode = True

