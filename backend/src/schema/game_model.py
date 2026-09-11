from pydantic import BaseModel

from datetime import datetime

from pydantic import BaseModel

from schema.player_model import PlayerReadModel


class GameReadModel(BaseModel):
    """Output contract to display a game."""

    id_game: int | None = None
    game_mode: str
    description: str | None = None
    timestamp: datetime | None = None
    player1: PlayerReadModel
    player2: PlayerReadModel
    winner: PlayerReadModel | None = None

    model_config = {"from_attributes": True}
    
class GamePlayModel(BaseModel):
    id_opponent: int
    game_mode: str
    params: dict = {}


class GameResponse(BaseModel):
    username1: str
    username2: str
    description: str
    winner: str | None
    new_elo1: int
    new_elo2: int
