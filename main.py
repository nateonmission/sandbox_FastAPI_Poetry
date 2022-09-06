from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Nate",
        "email": "nate@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

users = []

class User(BaseModel):
    email: str
    # name_first: str
    # name_last: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"status": "success"}

@app.get("/users/{id}", response_model=User)
async def get_user(
    id: int = Path(..., description="Enter USER ID"),
    ):
    return users[id]