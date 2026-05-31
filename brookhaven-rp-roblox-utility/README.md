# Brookhaven RP Roblox Utility

A lightweight Python utility for managing and tracking game state, players, and vehicles in Brookhaven RP (Roblox).

## Features

- Track player count, weather, and time of day
- Manage player profiles (jobs, vehicles)
- Spawn, damage, repair, and remove vehicles

## Installation

1. Ensure Python 3.8+ is installed.
2. No external dependencies required.

## Usage

```python
from src import GameState, PlayerTracker, VehicleHandler

state = GameState()
state.update_players(15, 20)

tracker = PlayerTracker()
tracker.add_player("user1", "CoolPlayer", "Police")

vehicles = VehicleHandler()
vehicles.spawn_vehicle("car1", "Sports Car", "user1")
```

## Testing

Run tests:
```
python tests/test_core.py
```