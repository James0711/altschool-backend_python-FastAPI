from enum import Enum
from typing import Optional
from pydantic import BaseModel

# Doctor Pydantic definition
class Doctors(BaseModel):
     id: int
     name: str
     specialization: str
     phone: str
     is_available: bool = True


# pydantic definition for Creating Doctor data
class DoctorsCreate(BaseModel):
     name: str
     specialization: str
     phone: str

     
# pydantic definition for Updating Doctor data
class DoctorsEdit(BaseModel):
     name: Optional[str] = None
     specialization: Optional[str] = None
     phone: Optional[str] = None
     



doctors: dict[int, Doctors] = {
     0: Doctors(id=0, name='Dr. James Eche', specialization='Optician', phone='07056489321', is_available=False),
     1: Doctors(id=1, name='Prof. Tim Joe', specialization='Gynaecology', phone='07012356798'),
     2: Doctors(id=2, name='Prof. Patience Audu', specialization='Surgeon', phone='08012345678')

}