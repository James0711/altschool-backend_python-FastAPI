from typing import Optional
from pydantic import BaseModel


# patient pydantic definition
class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


# pydantic definition Creating patient data
class PatientsCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


# pydantic definition for updating patient data
class PatientsEdit(BaseModel):
    name: Optional[str]=None
    age: Optional[int] = None
    sex: Optional[str] = None
    weight: Optional[float]=None
    height: Optional[float]=None
    phone: Optional[str] = None
    

patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='Oche Barry', age=29, sex= 'male', weight=108.9, height=67.5, phone= '08036871246'
	),
    1: Patients(
        id=1, name='Ehoche John', age=30, sex= 'male', weight=99.0, height=68.0, phone= '08120752396'
	),
    2: Patients(
        id=2, name='Jimoh Abigail', age=25, sex= 'female', weight=90, height=65, phone= '08102904865'
	)
}