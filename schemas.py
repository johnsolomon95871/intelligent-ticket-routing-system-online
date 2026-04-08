from pydantic import BaseModel
from typing import List, Optional

class TicketBase(BaseModel):
    title: str
    description: str
    customer_name: str

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    status: str

class AbstractTicket(TicketBase):
    id: int
    status: str
    ai_summary: Optional[str] = None
    ai_category: Optional[str] = None
    ai_sentiment: Optional[str] = None
    ai_urgency: Optional[str] = None
    agent_id: Optional[int] = None

    class Config:
        orm_mode = True
        from_attributes = True

class AgentBase(BaseModel):
    name: str
    expertise: str
    capacity: int = 5

class AgentResponse(AgentBase):
    id: int
    current_workload: int
    
    class Config:
        orm_mode = True
        from_attributes = True
