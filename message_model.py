from typing import Optional
from pydantic import BaseModel

class MessageModel(BaseModel):
    author: Optional[str]
    text: Optional[str]
