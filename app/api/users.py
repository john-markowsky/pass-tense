from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.DB.database import register_user

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/register", response_class=HTMLResponse)
async def get_register(request: Request):
    """Serve the register page"""
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
async def post_register(request: Request, data: dict):
    """Process the registration form"""
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    user_type = data.get('user_type')

    # register the user in the database
    register_user(first_name, last_name, email, password, user_type)
