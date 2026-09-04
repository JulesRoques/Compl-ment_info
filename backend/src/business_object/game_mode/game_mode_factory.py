from business_object.game_mode.coin_flip_mode import CoinFlipMode
from business_object.game_mode.dice_mode import DiceMode
from business_object.game_mode.game_mode import GameMode


class GameModeFactory:
    """Factory in charge of instantiating the right GameMode."""

    MODES = {
        "coinflip": CoinFlipMode,
        "dice": DiceMode,
    }

    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        Raises:
            ValueError: If the requested game_mode is not supported.
        """
        mode_class = cls.MODES.get(game_mode)

        if mode_class is None:
            raise ValueError(f"Unsupported game mode: {game_mode}")

        return mode_class()