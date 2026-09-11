"""Client to fetch games from an external API."""

import requests

from business_object.game import Game

from business_object.player import Player

BASE_URL = "http://localhost:5555"


class GameClient:
    """
    Client for the external games API.

    The external API uses its own field names, which do not match our
    business objects. This class is responsible for the mapping.

    Attributes:
        base_url (str): Root URL of the external API.
        timeout (float): Maximum number of seconds to wait for the API.
    """

    def __init__(self, base_url=BASE_URL, timeout=10):
        """Constructor"""
        self.base_url = base_url
        self.timeout = timeout

    def get_games(self):
        """Fetches the games from the external API and converts them.
        Returns:
            list[Game]: The games retrieved from the external API.
        Raises:
            requests.HTTPError: If the API answers with an error status.
        """
        response = requests.get(f"{self.base_url}/", timeout=self.timeout)
        response.raise_for_status()

        return [self.to_game(item) for item in response.json()]

    def to_game(self, item):
        """Converts one dictionary from the external API into a Game.

        The external schema differs from ours: players come as a list,
        a draw is an empty winner name, and some keys are missing on
        some records.

        Args:
            item (dict): One game as returned by the external API.
        Returns:
            Game: The corresponding business object.
        """
        players = item.get("players_list", [])
        winner_name = item.get("winner_name")

        return Game(
            player1=Player(username=players[0], elo=None, email=None) if len(players) > 0 else None,
            player2=Player(username=players[1], elo=None, email=None) if len(players) > 1 else None,
            game_mode=item.get("mode_type"),
            winner=Player(username=winner_name, elo=None, email=None) if winner_name else None,
            description=item.get("details", ""),
            timestamp=None,
        )