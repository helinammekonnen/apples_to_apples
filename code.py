import random
import sys


def clear_console():
    for i in range(30):
        print()

def judge(shuffled_cards, original_cards, scores):
    print("Your options are the following cards:")
    shuffled_cards.print_deck()
    try:
        choice = int(input("Please enter the number of the card (1" + "-" + str(shuffled_cards.find_number_of_cards()) + "): "))
    except ValueError:
        print("Oops, that wasn't a valid input! Please enter a number with no decimals.")
    choice = int(choice)
    winner = [str(shuffled_cards.see_card(choice - 1)),
              str(original_cards.find_card_index(shuffled_cards.see_card(choice - 1)))]
    print("The winning card is " + winner[0] + ", so Player #" + winner[1] + " wins the round!")
    scores[int(winner[1]) - 1] += 1 #choice is equivalent to user number to incrementing by that index (should) work


def is_game_over(quit_condition, point, limit):
    return quit_condition == 0 or point == limit


def run_game():
    try:
        top_score_limit = int(input("Score to win: "))
    except ValueError:
        print("Oops, that wasn't a valid input! Please enter a number with no decimals.")
        top_score_limit = int(input("Score to win: "))
    print()
    try:
        num_users = int(input("Number of players (enter 0 to quit): "))  # get number of players
    except ValueError:
        print("Oops, that wasn't a valid input! Please enter a number with no decimals.")
        num_users = int(input("Number of players (enter 0 to quit): "))  # get number of players
    print()
    list_of_decks = [] # will make this a list of each player's hand. is a list of Decks
    cards_for_play = Deck([])
    scores = [0] * num_users #set list to length of number of users
    prompt_card_deck_green = Deck([])

    for card in green_cards:
        prompt_card_deck_green.add_card(Card(card))

    prompt_card_deck_green.shuffle()

    red_card_deck = Deck([])

    for card in red_cards:
        red_card_deck.add_card(Card(card))

    red_card_deck.shuffle()

    for user in range(0, num_users):
        new_hand = []
        for i in range(0, 7):
            card = red_card_deck.draw_card()
            new_hand.append(card)
        list_of_decks.append(Deck(new_hand))

    while not is_game_over(num_users, max(scores), top_score_limit):
        prompt_card = prompt_card_deck_green.draw_card()
        for user_count in range(0, num_users):
            my_deck = list_of_decks[user_count]
            print("Greetings Player #" + str(user_count + 1) + "! It is now your turn.")
            print("Your current score: " + str(scores[user_count]))
            print("The prompt card is " + str(prompt_card) + ".")
            print()
            print("Your current deck: ")
            my_deck.print_deck()
            print()
            try:
                my_card_index = int(input("Enter the corresponding index: ")) - 1
            except ValueError:
                print("Oops, that wasn't a valid input! Please enter a number with no decimals.")
                my_card_index = int(input("Enter the corresponding index: ")) - 1
            except IndexError:
                print("Oops, that wasn't a valid input! Please enter a number between 1 and 7.")
            cards_for_play.add_card(my_deck.draw_specific_card(my_card_index))
            clear_console()
        print("Submission round concluded. Cards will now be judged!")
        cards_for_play_copy = cards_for_play
        judge(cards_for_play, cards_for_play_copy, scores)

    print("Congratulations Player #" + str(scores.index(top_score_limit) + 1) + ", you win!")
    try:
        choice = input("Enter r to restart or e to end: ")
    except ValueError:
        print("Oops, that wasn't a valid input! Please enter either a 'r' or an 'e'.")
        choice = input("Enter r to restart or e to end: ")

    if choice == "r":
        run_game()
        clear_console()
    elif choice == "e":
        clear_console()
        sys.exit()


class Deck(object):

    constituent_cards = []

    def __init__(self, card_list_in):
        self.constituent_cards = card_list_in

    def __str__(self):
        for e in self.constituent_cards:
            return "Card: " + str(e)

    def print_deck(self):
        count = 1
        for e in self.constituent_cards:
            print("Card #" + str(count) + ": "+ str(e))
            count += 1

    def add_card(self, card):
        self.constituent_cards.append(card)

    def shuffle(self):
        random.shuffle(self.constituent_cards)

    def see_card(self, index):
        return self.constituent_cards[index]

    def draw_specific_card(self, index):
        return self.constituent_cards.pop(index)

    def draw_card(self):
        return self.constituent_cards.pop()

    def find_number_of_cards(self):
        return len(self.constituent_cards)

    def find_card_index(self, card):
        return self.constituent_cards.index(card)

class Card(object):

    constituent_text = ""

    def __init__(self, message):
        self.constituent_text = message

    def __str__(self):
        return self.constituent_text

red_cards = red_list = ["A bad haircut", "A bull fight", "A car crash", "A cheap motel", "A crawl space", "A dozen red roses", "A flat tire", "A full moon", "A haunted house", "A high school bathroom", "A honeymoon", "A locker room", "A morgue", "A nine iron", "A school bus", "A school cafeteria", "A sunrise", "A sunset", "A tree house", "A used car lot", "Abraham Lincoln", "Adam Sandler", "Adolph Hitler", "AIDS", "Bats", "Beanie Babies", "Beets", "Being in love", "Bell-Bottoms", "Ben Stiller", "Bill Clinton", "Blizzard", "Board games", "Bottled water", "Body odor", "Body piercing", "Body surfing", "Boy scouts", "Brain surgeons", "Brains", "Broadway", "Buying a house", "Bungee jumping", "Cactus", "California", "Captain Kirk"]
green_cards = green_list = ["Absurd", "Addictive", "Adorable", "Aged", "American", "Ancient", "Animated", "Annoying", "Appetizing", "Arrogant", "Awesome",
              "Awkward", "Believable", "Bogus", "Boisterous", "Bold", "Boring", "Bright", "Brilliant", "Busy", "Calm", "Casual", "Charismatic",
              "Charming", "Cheesy", "Chewy", "Chunky", "Classic", "Clean", "Clueless", "Cold", "Colorful", "Comfortable", "Comical", "Complicated",
              "Confused", "Cool", "Corrupt", "Cosmic", "Cosmopolitan"]


run_game()
