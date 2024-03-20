# external import
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

# internal import
from config.databaseConnection import db, firestore
from schema.electricVehicleSchema import vehicleConverter
from models.electricVehicleModels import PostVehicleModel, UpdateVehicleModel


EV = electricVehicleRoutes = APIRouter(prefix="/vehicle")

EV_ref = db.collection("EV")


async def get_all_vehicles() -> list:

    try:
        docs = EV_ref.stream()

        result = vehicleConverter(docs)

    except Exception as err:
        raise err

    return result


async def get_single_vehicle(id: str) -> list:
    try:
        result = EV_ref.document(id).get().to_dict()
        return {"vehicle": result}

    except Exception as err:
        raise JSONResponse(content={"error": err}, status_code=500)


async def get_searched_vehicle(
    attribute: str,
    value: str | None = None,
    min: int | None = None,
    max: int | None = None,
):

    result = []

    if attribute and value:

        query = EV_ref.where(attribute, "==", value)
        query_results = query.stream()

        result = vehicleConverter(query_results)

        return result

    elif attribute and min and max:
        query = EV_ref.where(attribute, ">=", min).where(attribute, "<=", max)
        query_results = query.stream()

        result = vehicleConverter(query_results)

        return result


async def comparing_vehicle(id_1: str, id_2: str):

    try:
        vehicle1 = EV_ref.document(id_1).get().to_dict()
        vehicle2 = EV_ref.document(id_2).get().to_dict()

        return {"vehicle1": vehicle1, "vehicle2": vehicle2}

    except Exception as err:
        raise err


@EV.get("/compare")
async def compareing_two_vehicle(id_1: str, id_2: str):
    return await comparing_vehicle(id_1, id_2)


@EV.get("/search")
async def searched_vehicle(
    attribute: str,
    value: str | None = None,
    min: int | None = None,
    max: int | None = None,
):
    return await get_searched_vehicle(
        attribute=attribute, value=value, min=min, max=max
    )


@EV.get("/")
async def get_vehicles():
    return await get_all_vehicles()


@EV.get("/{id}")
async def single_vehicle(id: str):
    return await get_single_vehicle(id)


@EV.post("/review")
async def post_review(id: str, name: str, comment: str, rating: int):

    try:
        result = EV_ref.document(id).update(
            {
                "reviews": firestore.ArrayUnion(
                    [{"name": name, "comment": comment, "rating": rating}]
                )
            }
        )

        return {"msg": "review added"}
    except Exception as err:
        raise err

    pass


@EV.post("/")
async def post_vehicle(formData: PostVehicleModel):

    try:
        vehicle = dict(formData)

        nameFound = EV_ref.where("name", "==", vehicle["name"])
        nameFound = EV_ref.where("name", "==", vehicle["name"])
        query_result = nameFound.stream()
        query_result_dict = vehicleConverter(query_result)
        print(query_result_dict)

        if len(query_result_dict) != 0:
            return JSONResponse(
                status_code=500, content={"error": "Name must be unique"}
            )

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
