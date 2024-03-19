from pydantic import BaseModel


class PostVehicleModel(BaseModel):

    name: str
    manufacturer: str
    year: int
    batterySize: float
    wltpRange: float
    cost: int
    power: float


class UpdateVehicleModel(PostVehicleModel):
    pass
