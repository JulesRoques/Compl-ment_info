from abc import ABC, abstractmethod


class GameMode(ABC):
    """Abstract base class defining the contract for all game modes.

    Each concrete game mode must implement its own rules by overriding
    the play() method.
    """

    @abstractmethod
    def play(self, p1, p2, **kwargs):
        """Plays a game between two players according to the mode rules.
        Args:
            p1 (Player): The first player.
            p2 (Player): The second player.
            **kwargs: Additional parameters required by specific modes.
        Returns:
            Game: The resulting game, with its winner and description.
        """