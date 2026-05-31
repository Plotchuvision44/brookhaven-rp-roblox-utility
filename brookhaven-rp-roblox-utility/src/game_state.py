"""Tracks the current game state of Brookhaven RP."""

class GameState:
    """Represents the state of the Brookhaven RP server."""
    def __init__(self):
        self.server_id = ""
        self.players_online = 0
        self.max_players = 0
        self.is_private = False
        self.current_weather = "Clear"
        self.time_of_day = "Day"

    def update_players(self, online: int, max_players: int):
        """Update player count."""
        self.players_online = online
        self.max_players = max_players

    def set_weather(self, weather: str):
        """Set weather condition."""
        self.current_weather = weather

    def set_time(self, time: str):
        """Set time of day."""
        self.time_of_day = time

    def summary(self) -> str:
        """Return a text summary of the game state."""
        return (f"Server: {self.server_id} | Players: {self.players_online}/{self.max_players} "
                f"| {self.time_of_day} | {self.current_weather}")