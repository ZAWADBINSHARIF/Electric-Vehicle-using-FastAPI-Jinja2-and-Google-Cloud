# external import
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


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


# ** Template Routes
app.include_router(templateRoutes)
# ** Auth routers for login and sign up
app.include_router(authRoute)
# ** Electric Vehicle Routes where vehicles can be editable
app.include_router(electricVehicleRoutes)


if __name__ == "__main__":
    uvicorn.run("main:app", port=4000, reload=True, log_level="info")
