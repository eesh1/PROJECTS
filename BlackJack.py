import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}
Available_chips = 100
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for rank in ranks:
            for suit in suits:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def draw_a_card(self):
        return self.all_cards.pop()


class bet():
    def __init__(self, name):
        self.name = name
        print(f"{name}, your chip balance is {Available_chips} chips")
        self.x = 110
        while self.x > Available_chips:
            self.x = int(input("Enter your bet: "))
        print(f"{name}, your bet is {self.x} chips")

    def bet_amount(self):
        return self.x
deck = Deck()
deck.shuffle()

class Player:

    def __init__(self,name):
        self.name = name
        self.all_cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,card):
        if type(card) == type([]):
            self.all_cards.extend(card)
            self.value += values[card.rank]

        else:
            self.all_cards.append(card)
            self.value += values[card.rank]

dealer = Player("Dealer")
human = Player("Human")
human_bet = bet("Human")
dealer_bet = bet("Dealer")

for x in range(2):
    dealer.add_cards(deck.draw_a_card())
    human.add_cards(deck.draw_a_card())

gameON = True

while gameON:
    human_bet
    dealer_bet
    print(f" Dealer's show card is {dealer.all_cards[0]}")
    print(f" Human's show card is {human.all_cards[0]}")
    hit_human = True
    while hit_human:
        hit1 = input("Would you like to hit? ")
        if hit1[0].lower() == 'y':
            human.add_cards(deck.draw_a_card())
            for k in human.all_cards:
                print(k)

        elif hit1[0].lower() == 'n':
            for k in human.all_cards:
                print(k)
            hit_human = False

    print(f"Value of human's cards is {human.value}")
    if human.value>21:
        print("Dealers wins!")
        dealer_bet.x += human_bet.x
        print(f"You won {dealer_bet.x} chips")
        human_bet.x -= 100

    else:
        print("NOW DEALER'S TURN")
        hit_dealer = True
        while hit_dealer:
            hit2 = input("Would you like to hit? ")
            if hit2[0].lower() == 'y':
                dealer.add_cards(deck.draw_a_card())
                for k in dealer.all_cards:
                    print(k)
            elif hit2[0].lower() == 'n':
                for k in dealer.all_cards:
                    print(k)
                    hit_dealer = False
        print(f"Value of dealer's cards is {dealer.value}")
        if dealer.value>21:
            print("Human wins!")
            human_bet.x += dealer_bet.x
            print(f"You won {human_bet.x} chips")
            dealer_bet.x -= 100
        else:
            if human.value > dealer.value:
                print("Human wins!")
                human_bet.x += dealer_bet.x
                print(f"You won {human_bet.x} chips")
                dealer_bet.x -= 100

            elif dealer.value > human.value:
                print("Dealer wins!")
                dealer_bet.x += human_bet.x
                print(f"You won {dealer_bet.x} chips")
                human_bet.x -= 100

            else:
                print("It's a draw!")

    contine_game = input("Wanna play again?")
    if contine_game[0].lower() == 'n':
        print("Thank You for playing! :)")
        gameON = False
        break
    elif contine_game[0].lower() == 'y':
        human.all_cards = []
        dealer.all_cards = []
        human.value = 0
        dealer.value = 0
        for x in range(2):
            dealer.add_cards(deck.draw_a_card())
            human.add_cards(deck.draw_a_card())
        continue

    else:
        break

