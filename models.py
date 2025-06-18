from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Task(Document):
    title: str
    content: str

    class Settings:
        name = "tasks"  # nome da collection

    class Config:
        schema_extra = {
            "example": {
                "title": "Estudar FastAPI",
                "content": "Ler a documentação oficial e fazer um CRUD"
            }
        }
