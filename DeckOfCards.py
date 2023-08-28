#Sebastian SantaCruz
#CIS 261
#Deck Of Cards
import random
class cards:
  def __init__(self, rank, suit):
   self.rank = rank
   self.suit = suit
class Deck:
  def __init__(self):
    ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    self.deck = [cards(rank, suit) for suit in suits for rank in ranks]
  def shuffle(self):
    random.shuffle(self.deck)
  def deal(self, num_cards):
    if num_cards <= len(self.deck):
      dealt_cards = self.deck[:num_cards]
      self.deck = self.deck[num_cards:]
      return dealt_cards
    else:
      return "Not enough cards in the deck."

if __name__ == "__main__":
  print("I have shuffled a deck of 52 cards")
  num_cards = int(input("How many cards would you like?: "))
  print("Here are your cards:\n")
  my_deck = Deck()
  my_deck.shuffle()
  dealt_cards = my_deck.deal(num_cards)
  for card in dealt_cards:
    print(f"{card.rank} of {card.suit}")
  print("\nThere are " + str(52 - num_cards) +" left in the deck.")
