from fastapi import FastAPI, Depends, Request, Form
from sqlalchemy.orm import Session
from backend.auth import register_user, login_user, get_db
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/register")
async def register(
    username: str = Form(),
    password: str = Form(),
    db: Session = Depends(get_db)
):
    try:
        register_user(username, password, db)
        return JSONResponse(content={"success": True, "message": "User registered succesfully!"})
    except Exception as e:
        return JSONResponse(content={"success": False, "message": str(e)}, status_code=400)
    
@app.post("/login")
async def login(
    username: str = Form(),
    password: str =  Form(),
    db: Session = Depends(get_db)
):
    try:
        login_user(username, password, db)
        return JSONResponse(content={"success": True, "message": "Login succesful!"})
    except Exception as e:
        return JSONResponse(content={"success": False, "message": "Invalid Credentials"}, status_code=401)