# external import
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

# internal import
from config.databaseConnection import db
from models.electricVehicleModels import PostVehicleModel, UpdateVehicleModel


EV = electricVehicleRoutes = APIRouter(prefix="/vehicle")

EV_ref = db.collection("EV")


async def get_all_vehicles() -> list:

    try:
        docs = EV_ref.stream()

        result = []

        for doc in docs:
            doc_data = doc.to_dict()

            doc_info = {"id": doc.id, "fields": doc_data}
            result.append(doc_info)

            print(doc_info)

    except Exception as err:
        raise err

    return result


async def get_single_vehicle(id: str):
    try:
        result = EV_ref.document(id).get().to_dict()
        return {"vehicle": result}

    except Exception as err:
        raise JSONResponse(content={"error": err}, status_code=500)


@EV.get("/")
async def get_vehicles():
    return await get_all_vehicles()


@EV.get("/{id}")
async def single_vehicle(id: str):
    return await get_single_vehicle(id)


@EV.post("/")
async def post_vehicle(formData: PostVehicleModel):

    try:
        vehicle = dict(formData)

        vehicle_ref = EV_ref.document().set(vehicle)

        return JSONResponse(
            content={"msg": "New vehicle has been added", "id": f"{vehicle_ref}"},
            status_code=201,
        )
    except Exception as err:
        raise err


@EV.put("/{id}")
async def update_vehicle(id: str, formData: UpdateVehicleModel):
    try:

        EV_ref.document(id).set(dict(formData))

        return JSONResponse(content={"msg": "Update successfull"}, status_code=200)

    except Exception as err:
        raise err


@EV.delete("/{id}")
async def remove_vehicle(id: str):
    try:

        EV_ref.document(id).delete()

        return JSONResponse(
            content={"msg": "Vehicle has been deleted"},
            status_code=200,
        )
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error deleting vehicle: {err}")
