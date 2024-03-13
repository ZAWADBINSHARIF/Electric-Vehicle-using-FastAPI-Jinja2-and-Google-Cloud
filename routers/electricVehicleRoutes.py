# external import
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

# internal import
from config.databaseConnection import db


EV = electricVehicleRoutes = APIRouter(prefix="/vehicle")
db.collection("cities")

@EV.get("/")
async def get_all_vehicle():
    cities_ref = db.collection("cities")
    all_cities = cities_ref.stream()
    for city in all_cities:
        print(city)
    return {"msg":""}

@EV.post("/")
async def post_vehicle(city:str):
    db.collection("cities").document("LA").set(
        {"name": city, "state": "CA", "country": "USA"}
    )
    return {"msg":"successully added"}


@EV.put("/")
async def update_vehicle(country:str):
    city_ref = db.collection("cities").document("LA")
    city_ref.set({"capital": True, "country": country}, merge=True) # merge for adding extra collunm named capital


@EV.delete("/")
async def remove_vehicle():
    pass
