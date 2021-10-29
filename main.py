from poker.card import Card
from poker.deck import Deck
from poker.game_round import GameRound
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name="Akshay", hand= hand1)
player2 = Player(name="ken", hand= hand2)
players = [player1,player2]

game_round = GameRound(deck = deck,players = players)
game_round.play()

for player in players:
    print(f"{player.name} receives a {player.hand}.")
    index, hand_name, valid_cards = player.best_hand()
    valid_cards_strings = [str(card) for card in valid_cards]
    valid_cards_string = " and ".join(valid_cards_strings)
    print(f"{player.name} has a {hand_name} with a {valid_cards_string}.")
winning_player = max(players)
print(f"The winner is {winning_player.name}.")