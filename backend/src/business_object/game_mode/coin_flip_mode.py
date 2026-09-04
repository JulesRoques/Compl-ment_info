import secrets

from business_object.game import Game
from business_object.game_mode.game_mode import GameMode


class CoinFlipMode(GameMode):
    """Game mode where a coin is flipped, the first player bets on the result."""

    def play(self, p1, p2, choice="heads", **kwargs):
        """Plays a coin flip game between two players.
        Args:
            p1 (Player): The first player, who bets on the coin result.
            p2 (Player): The second player.
            choice (str): The side bet by the first player ("heads" or "tails").
            **kwargs: Unused for this game mode.
        Returns:
            Game: The resulting game, there is no draw in this mode.
        """
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2

        return Game(
            player1=p1,
            player2=p2,
            game_mode="coinflip",
            winner=winner,
            description=f"{p1.username} bet on {choice}, the coin landed on {result}",
        )