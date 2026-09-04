from business_object.game_mode.game_mode_factory import GameModeFactory
from business_object.player import Player
from business_object.scoring_strategy import ScoringStrategy

p1 = Player(username="Jacky", elo=1500, email="jacky@ensai.fr")
p2 = Player(username="Jackie", elo=1500, email="jackie@ensai.fr")

game = GameModeFactory.get_mode("coinflip").play(p1, p2, choice="heads")
print(game)
print("avant :", p1.elo, p2.elo)

ScoringStrategy.update_player_ratings(game)
print("après :", p1.elo, p2.elo)