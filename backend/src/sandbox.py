from business_object.game import Game
from business_object.player import Player

p1 = Player(username="Jacky", elo=1500, email="jacky@ensai.fr")
p2 = Player(username="Jackie", elo=1500, email="jackie@ensai.fr")

game = Game(player1=p1, player2=p2, game_mode="coinflip", winner=p2)
print(game)

nul = Game(player1=p1, player2=p2, game_mode="dice")
print(nul)