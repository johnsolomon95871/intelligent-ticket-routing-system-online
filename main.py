from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine
from routers import tickets, agents

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Intelligent Ticket Routing System API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets.router)
app.include_router(agents.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Intelligent Ticket Routing System API"}
