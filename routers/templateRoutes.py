# external import
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

# internal import
from routers.electricVehicleRoutes import get_all_vehicles
from routers.electricVehicleRoutes import get_single_vehicle

templateRoutes = APIRouter()

template = Jinja2Templates(directory="templates")


@templateRoutes.get("/", response_class=HTMLResponse)
async def home_page(req: Request):

    try:
        user_info = req.state.user_info
    except:
        user_info = None

    result = await get_all_vehicles()

    return template.TemplateResponse(
        request=req,
        name="home.html",
        context={"user_info": user_info, "all_vehicles": result},
    )


@templateRoutes.get("/single/{id}", response_class=HTMLResponse)
async def single_vehicle(req: Request, id: str):

    try:
        user_info = req.state.user_info
    except:
        user_info = None

    result = await get_single_vehicle(id)
    print(result)
    return template.TemplateResponse(
        request=req,
        name="single.html",
        context={"user_info": user_info, "vehicle": result, "id": id},
    )


@templateRoutes.get("/add", response_class=HTMLResponse)
async def add_vehicle(req: Request):

    try:
        user_info = req.state.user_info

        if user_info == {}:
            return RedirectResponse("/")

    except:
        user_info = None

    return template.TemplateResponse(
        request=req, name="add.html", context={"user_info": user_info}
    )


@templateRoutes.get("/login", response_class=HTMLResponse)
async def login(req: Request):
    return template.TemplateResponse(request=req, name="login.html")


@templateRoutes.get("/signup", response_class=HTMLResponse)
async def signup(req: Request):
    return template.TemplateResponse(request=req, name="signup.html")
