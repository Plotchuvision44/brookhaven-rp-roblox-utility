"""Tracks player data within a Brookhaven RP session."""

from typing import List, Dict

class Player:
    """Represents a single player in the game."""
    def __init__(self, player_id: str, username: str, job: str = "Visitor"):
        self.player_id = player_id
        self.username = username
        self.job = job
        self.vehicle_id = "None"

    def assign_vehicle(self, vehicle_id: str):
        """Assign a vehicle to the player."""
        self.vehicle_id = vehicle_id

    def change_job(self, new_job: str):
        """Change the player's job."""
        self.job = new_job

    def __repr__(self) -> str:
        return f"Player({self.username}, {self.job}, Vehicle: {self.vehicle_id})"


class PlayerTracker:
    """Manages a list of players in the session."""
    def __init__(self):
        self.players: Dict[str, Player] = {}

    def add_player(self, player_id: str, username: str, job: str = "Visitor"):
        """Add a new player."""
        if player_id not in self.players:
            self.players[player_id] = Player(player_id, username, job)

    def remove_player(self, player_id: str):
        """Remove a player by ID."""
        if player_id in self.players:
            del self.players[player_id]

    def get_player(self, player_id: str) -> Player:
        """Get a player by ID."""
        return self.players.get(player_id)

    def list_players(self) -> List[Player]:
        """Return all players."""
        return list(self.players.values())

    def player_count(self) -> int:
        """Return number of players."""
        return len(self.players)