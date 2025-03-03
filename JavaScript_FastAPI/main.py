from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

API_KEY = "2ec19d9f9c7fc9dfd2d68ff3d96d4d8a"
OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5/weather"

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/weather")
async def get_weather(city: str):
    weather = get_weather_data(city)

    if weather.get("cod") != 200:
        return {"error": "City not found"}
    
    weather_data = {
        "city": weather["name"],
        "temperature": f"{weather['main']['temp']}28°C",
        "description": weather["weather"][0]["description"].title(),
        "icon": f"https://openweathermap.org/img/wn/{weather['weather'][0]['icon']}@2x.png"
    }
    return weather_data


def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()
