from pydantic import BaseModel


class PostVehicleModel(BaseModel):

    name: str
    manufacturer: str
    year: int
    batterySize: float
    wltpRange: float
    cost: int
    power: float


class UpdateVehicleModel(BaseModel):

    name: str | None = None
    manufacturer: str | None = None
    year: int | None = None
    batterySize: float | None = None
    wltpRange: float | None = None
    cost: int | None = None
    power: float | None = None
