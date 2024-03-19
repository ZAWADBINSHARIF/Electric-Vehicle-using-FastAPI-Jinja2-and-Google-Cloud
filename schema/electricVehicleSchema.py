def individual_vehicle(item) -> dict:
    return {"id": item.id, "fields": item.to_dict()}


def vehicleConverter(vehicles) -> list:
    allVehicles = []

    allVehicles = [individual_vehicle(vehicle) for vehicle in vehicles]

    return allVehicles
