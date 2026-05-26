# backend/app.py
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List
import json
import pathlib
import uuid

DATA_FILE = pathlib.Path(__file__).parent / "data.json"
if not DATA_FILE.exists():
    DATA_FILE.write_text(json.dumps({"sections": []}, indent=2))

app = FastAPI(title="Landing CMS (Minimal)")

class SectionIn(BaseModel):
    key: str
    title: str
    content: str | None = None

class SectionOut(SectionIn):
    id: str

class ContactIn(BaseModel):
    name: str
    email: str
    message: str

def read_data():
    return json.loads(DATA_FILE.read_text())

def write_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2))

@app.get("/api/content/", response_model=List[SectionOut])
def list_sections():
    data = read_data()
    return data["sections"]

@app.get("/api/content/{key}", response_model=SectionOut)
def get_section(key: str):
    data = read_data()
    for s in data["sections"]:
        if s["key"] == key:
            return s
    raise HTTPException(status_code=404, detail="Section not found")

@app.post("/api/content/", response_model=SectionOut)
def upsert_section(section: SectionIn):
    data = read_data()
    for i, s in enumerate(data["sections"]):
        if s["key"] == section.key:
            s["title"] = section.title
            s["content"] = section.content
            data["sections"][i] = s
            write_data(data)
            return s
    new = {"id": str(uuid.uuid4()), **section.dict()}
    data["sections"].append(new)
    write_data(data)
    return new

@app.post("/api/contact/")
def contact(payload: ContactIn, background_tasks: BackgroundTasks):
    async def _send_mock(p):
        # placeholder: integrate real email provider here
        print("Sending contact (mock):", p)
    background_tasks.add_task(_send_mock, payload.dict())
    return {"status": "queued"}
