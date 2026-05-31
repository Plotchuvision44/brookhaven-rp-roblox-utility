"""Manages vehicles in Brookhaven RP."""

from typing import Dict

class Vehicle:
    """Represents a vehicle in the game."""
    def __init__(self, vehicle_id: str, model: str, owner_id: str = ""):
        self.vehicle_id = vehicle_id
        self.model = model
        self.owner_id = owner_id
        self.damaged = False
        self.speed = 0

    def damage(self):
        """Mark vehicle as damaged."""
        self.damaged = True

    def repair(self):
        """Repair vehicle."""
        self.damaged = False

    def set_speed(self, speed: int):
        """Set current speed."""
        self.speed = speed

    def __repr__(self) -> str:
        return f"Vehicle({self.model}, ID: {self.vehicle_id}, Damaged: {self.damaged})"


class VehicleHandler:
    """Manages all vehicles in the session."""
    def __init__(self):
        self.vehicles: Dict[str, Vehicle] = {}

    def spawn_vehicle(self, vehicle_id: str, model: str, owner_id: str = ""):
        """Spawn a new vehicle."""
        if vehicle_id not in self.vehicles:
            self.vehicles[vehicle_id] = Vehicle(vehicle_id, model, owner_id)

    def remove_vehicle(self, vehicle_id: str):
        """Remove a vehicle."""
        if vehicle_id in self.vehicles:
            del self.vehicles[vehicle_id]

    def get_vehicle(self, vehicle_id: str) -> Vehicle:
        """Get a vehicle by ID."""
        return self.vehicles.get(vehicle_id)

    def list_vehicles(self) -> list:
        """Return all vehicles."""
        return list(self.vehicles.values())