from business_object.game_mode.game_mode_factory import GameModeFactory
from business_object.game_mode.dice_mode import DiceMode
from business_object.game_mode.coin_flip_mode import CoinFlipMode
from business_object.player import Player

p1 = Player(username="Jacky", elo=1500, email="jacky@ensai.fr")
p2 = Player(username="Jackie", elo=1500, email="jackie@ensai.fr")

dice = DiceMode()
coin = CoinFlipMode()

for _ in range(10):
    print(dice.play(p1, p2))

print("---")

for _ in range(10):
    print(coin.play(p1, p2, choice="heads"))

print(GameModeFactory.get_mode("dice"))
print(GameModeFactory.get_mode("coinflip"))
GameModeFactory.get_mode("poker")   # doit lever une ValueError