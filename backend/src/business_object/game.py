from datetime import datetime


class Game:
    """
    Class representing a Game between two players.
    Attributes:
        id_game (int): The unique identifier for the game, set when persisted.
        player1 (Player): The first player.
        player2 (Player): The second player.
        game_mode (str): The type of game played ("coinflip" or "dice").
        winner (Player, optional): The winning player, None if draw.
        description (str): Additional details about the game.
        timestamp (datetime): When the game was played.
    """

    def __init__(
        self,
        player1,
        player2,
        game_mode,
        winner=None,
        description="",
        timestamp=None,
    ):
        """Constructor"""
        self.id_game = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        """Returns a string representation of the game.
        Returns:
            str: A string containing the game mode, both players and the winner.
        """
        winner = self.winner.username if self.winner else "draw"
        return (
            f"{self.game_mode} between {self.player1.username} "
            f"and {self.player2.username}. Winner: {winner}"
        )