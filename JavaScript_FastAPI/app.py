from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

API_KEY = "2ec19d9f9c7fc9dfd2d68ff3d96d4d8a"
OPENWEATHERMAP_URL = "http://api.openweathermap.org/data/2.5/weather"

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/weather")
async def get_weather(city: str, mock: bool = False):
    if mock:
        return {
            "name": city,
            "main": {"temp": 28, "humidity": 70},
            "weather": [{"description": "Partly cloudy", "icon": "02d"}],
            "sys": {"country": "US"}
        }

    try:
        url = f"{OPENWEATHERMAP_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        
        return {
            "name": data.get("name"),
            "main": {
                "temp": data.get("main", {}).get("temp"),
                "humidity": data.get("main", {}).get("humidity")
            },
            "weather": [
                {
                    "description": data.get("weather", [{}])[0].get("description"),
                    "icon": data.get("weather", [{}])[0].get("icon")
                }
            ],
            "sys": {
                "country": data.get("sys", {}).get("country")
            }
        }
    except requests.exceptions.RequestException as e:
        # Handle API request errors
        raise HTTPException(status_code=500, detail=f"Error fetching weather data: {str(e)}")
    except KeyError as e:
        # Handle missing data in the API response
        raise HTTPException(status_code=500, detail=f"Invalid data received from the weather API: {str(e)}")