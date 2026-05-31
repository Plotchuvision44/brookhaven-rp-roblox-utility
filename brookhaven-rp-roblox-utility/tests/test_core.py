"""Tests for Brookhaven RP Utility core modules."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.game_state import GameState
from src.player_tracker import PlayerTracker, Player
from src.vehicle_handler import VehicleHandler, Vehicle


def test_game_state():
    gs = GameState()
    gs.server_id = "BRP-001"
    gs.update_players(12, 20)
    gs.set_weather("Rainy")
    gs.set_time("Night")
    assert gs.players_online == 12
    assert gs.max_players == 20
    assert "Rainy" in gs.summary()
    assert "Night" in gs.summary()
    print("[PASS] GameState tests passed.")


def test_player_tracker():
    pt = PlayerTracker()
    pt.add_player("p1", "Alex", "Police")
    pt.add_player("p2", "Jordan", "Doctor")
    assert pt.player_count() == 2
    player = pt.get_player("p1")
    assert player.username == "Alex"
    player.change_job("Firefighter")
    assert player.job == "Firefighter"
    pt.remove_player("p2")
    assert pt.player_count() == 1
    print("[PASS] PlayerTracker tests passed.")


def test_vehicle_handler():
    vh = VehicleHandler()
    vh.spawn_vehicle("v1", "Tesla Model 3", "p1")
    vh.spawn_vehicle("v2", "Police Cruiser")
    assert len(vh.list_vehicles()) == 2
    v1 = vh.get_vehicle("v1")
    assert v1.model == "Tesla Model 3"
    v1.damage()
    assert v1.damaged is True
    v1.repair()
    assert v1.damaged is False
    vh.remove_vehicle("v2")
    assert len(vh.list_vehicles()) == 1
    print("[PASS] VehicleHandler tests passed.")


if __name__ == "__main__":
    test_game_state()
    test_player_tracker()
    test_vehicle_handler()
    print("\nAll tests passed successfully.")