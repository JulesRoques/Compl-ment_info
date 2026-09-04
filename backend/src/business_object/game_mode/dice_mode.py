import secrets

from business_object.game import Game
from business_object.game_mode.game_mode import GameMode


class DiceMode(GameMode):
    """Game mode where both players roll a die, the highest roll wins."""

    def play(self, p1, p2, **kwargs):
        """Plays a dice game between two players.
        Args:
            p1 (Player): The first player.
            p2 (Player): The second player.
            **kwargs: Unused for this game mode.
        Returns:
            Game: The resulting game, winner is None if both rolls are equal.
        """
        roll1 = secrets.choice(range(1, 7))
        roll2 = secrets.choice(range(1, 7))

        if roll1 > roll2:
            winner = p1
        elif roll1 < roll2:
            winner = p2
        else:
            winner = None

        return Game(
            player1=p1,
            player2=p2,
            game_mode="dice",
            winner=winner,
            description=f"{p1.username} rolled {roll1}, {p2.username} rolled {roll2}",
        )