############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random

# Document

class Player():

    def __init__(self):
        self.hand = []
        self.score = sum(self.hand)

    def calculate_score(self):
        self.score = sum(self.hand)

    def first_cards(self, dealer):
        """Players first two cards from the dealer"""
        self.hand.append(dealer.give_card())
        self.hand.append(dealer.give_card())
        self.calculate_score()

    def check_hand(self):
        """Checks hand if a condition is met, to stop the game"""
        if self.score > 21:
            for index, card in enumerate(self.hand):
                if card == 11:
                    self.hand[index] = 1
                    self.calculate_score()
                elif self.score >= 21:
                    return False
                else:
                    return True
        elif self.score < 21:
            return True

    def hit_card(self, dealer):
        """Receive a card from the dealer"""
        first_card = dealer.hand[0]
        print(f"Your cards: {self.hand}, current score: {self.score}")
        print(f"Computer's first card: {first_card}")
        if self.check_hand() and input(
                f"Type 'y' to get another card, type 'n' to pass: ") == "y":
            self.hand.append(dealer.give_card())
            self.calculate_score()
            if self.check_hand():
                self.hit_card(dealer)


class Dealer():

    def __init__(self):
        self.hand = []
        self.score = sum(self.hand)

    def calculate_score(self):
        self.score = sum(self.hand)

    def give_card(self):
        """Selects a random card out of list and returns card"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def first_cards(self, ):
        """Dealer's first two cards"""
        self.hand.append(self.give_card())
        self.hand.append(self.give_card())
        self.calculate_score()

    def check_hand(self):
        """Checks hand if a condition is met, to stop the game"""
        while self.score > 21 and 11 in self.hand:
            for index, card in enumerate(self.hand):
                if card == 11:
                    self.hand[index] = 1
                self.calculate_score()
        if self.score > 16:
          return False
        else:
          return True

    def hit_card(self, player):
        """Receive a card"""
        if player.score < 21 or (player.score == 21 and len(player.hand) > 2):
            while self.check_hand():
                self.hand.append(self.give_card())
                self.calculate_score()

    def compare(self, player):
        """Compares the score of player and dealer"""
        #Bug fix. If you and the computer are both over, you lose.
        if player.score > 21 and self.score > 21:
            return "You went over. You lose 😤"
        if player.score == self.score:
            return "Draw 🙃"
        elif self.score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif player.score == 0:
            return "Win with a Blackjack 😎"
        elif player.score > 21:
            return "You went over. You lose 😭"
        elif self.score > 21:
            return "Opponent went over. You win 😁"
        elif player.score > self.score:
            return "You win 😃"
        else:
            return "You lose 😤"


def blackjack():
    print(logo)
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': "
             ) == "y":
        keep_playing = True
    else:
        keep_playing = False

    while keep_playing:
        player = Player()
        dealer = Dealer()

        dealer.first_cards()
        player.first_cards(dealer)

        player.hit_card(dealer)
        dealer.hit_card(player)

        dealer.compare(player)

        print(f"Your final hand: {player.hand}, final score: {player.score}")
        print(
            f"Computer's final hand: {dealer.hand}, final score: {dealer.score}"
        )

        print(dealer.compare(player))

        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': "
                 ) == "y":
            keep_playing = True
            replit.clear()
            print(logo)
        else:
            keep_playing = False


blackjack()

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
