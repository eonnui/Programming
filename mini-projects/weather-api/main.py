from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()

API_KEY = "2ec19d9f9c7fc9dfd2d68ff3d96d4d8a"
OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5/weather"

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home (request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/weather")
async def get_weather(city: str):
    url = f"{OPENWEATHERMAP_URL}?q={city}&units=metric&appid={API_KEY}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        return {"error" : "City not found"}
    
    return response.json()