
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class PersonModel(BaseModel):
    name: Optional[str]
    child: Optional[bool]
    confirmed: Optional[str]
    confirmedAt: Optional[datetime]
    
class FamilyModel(BaseModel):
    name: Optional[str]
    people:  Optional[List[PersonModel]]

class ListModel(BaseModel):
    list: Optional[List[FamilyModel]]