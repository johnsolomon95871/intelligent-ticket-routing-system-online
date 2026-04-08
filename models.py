from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    expertise = Column(String) # Comma separated expertise tags
    current_workload = Column(Integer, default=0)
    capacity = Column(Integer, default=5)

    tickets = relationship("Ticket", back_populates="agent")

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    customer_name = Column(String)
    status = Column(String, default="New") # New, Assigned, In Progress, Resolved
    
    # AI derived fields
    ai_summary = Column(Text, nullable=True)
    ai_category = Column(String, nullable=True) # Billing, Technical, General, etc.
    ai_sentiment = Column(String, nullable=True) # Positive, Neutral, Negative
    ai_urgency = Column(String, nullable=True) # Low, Medium, High
    
    agent_id = Column(Integer, ForeignKey("agents.id"), nullable=True)

    agent = relationship("Agent", back_populates="tickets")
