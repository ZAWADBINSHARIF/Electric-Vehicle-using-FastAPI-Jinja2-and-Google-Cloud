# external import
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templateRoutes = APIRouter()

template = Jinja2Templates(directory="templates")


@templateRoutes.get("/", response_class=HTMLResponse)
async def home_page(req: Request):
    return template.TemplateResponse(request=req, name="home.html")


@templateRoutes.get("/login", response_class=HTMLResponse)
async def home_page(req: Request):
    return template.TemplateResponse(request=req, name="login.html")


@templateRoutes.get("/signup", response_class=HTMLResponse)
async def home_page(req: Request):
    return template.TemplateResponse(request=req, name="signup.html")
