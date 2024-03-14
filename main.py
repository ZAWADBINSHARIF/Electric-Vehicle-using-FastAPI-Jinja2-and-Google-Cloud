# external import
import uvicorn
import google.oauth2.id_token
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from google.auth.transport import requests


# internal import
from routers.templateRoutes import templateRoutes
from routers.authRoutes import authRoute
from routers.electricVehicleRoutes import electricVehicleRoutes


app = FastAPI(
    title="An interactive database for Electric Vehicles",
    description="Assignment of Cloud Platforms & Applications",
)


# static and template files are defined
app.mount("/static", StaticFiles(directory="static"), name="static")


firebase_request_adapter = requests.Request()


# ** Middleware
@app.middleware("http")
async def log_middleware(req: Request, call_next):

    id_token = req.cookies.get("token")

    if id_token and id_token != "":
        try:

            user_info = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter
            )
            req.state.user_info = user_info

        except Exception as err:
            print(err)
    else:
        req.state.user_info = {}

    response = await call_next(req)
    return response


# ** Template Routes
app.include_router(templateRoutes)
# ** Auth routers for login and sign up
app.include_router(authRoute)
# ** Electric Vehicle Routes where vehicles can be editable
app.include_router(electricVehicleRoutes)


if __name__ == "__main__":
    uvicorn.run("main:app", port=4000, reload=True, log_level="info")
