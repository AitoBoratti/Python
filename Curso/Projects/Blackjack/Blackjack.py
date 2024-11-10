from Data import cards as Deck, logo
from random import shuffle
import os 

# REFACTORIZACION DEL CODIGO: Pasado a orientacion a objetos.

class Blackjack():
    STARTING_STR = "\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
    ONE_MORE_STR = "Type 'y' to get another card, type 'n' to pass: "


    def __init__(self):
        self.game_deck = Deck[:]
        self.player_hand = []
        self.computer_hand = []
        
    
    def computer_sum(self):
        return sum(self.computer_hand)
    
    
    def player_sum(self):
        return sum(self.player_hand)


    def shuffle_deck(self):
        """Mezcla el mazo original."""
        shuffle(self.game_deck)


    def game_dont_over(self):
        """Verifica si el jugador tiene intencion de jugar una partida mas."""
        return input(self.STARTING_STR).lower() == "y"


    def _adjust_hand_for_ace(self,hand=[]):
        while ((11 in hand) and (sum(hand) > 21)):
            hand.index[11] = 1      
    
            
    def check_as(self):
        """Chequea si existe un as en alguna de las manos. En caso de encontrarlo, lo transforma en un 1 si fuera necesario."""
        self._adjust_hand_for_ace(self.player_hand)
        self._adjust_hand_for_ace(self.computer_hand)


    def start_hands(self):
        """Reinicia las manos iniciales."""
        self.player_hand.clear()
        self.computer_hand.clear()
        for _ in range(2):    
            self.player_hand.append(self.game_deck.pop())
        while self.computer_sum() < 17:
            self.computer_hand.append(self.game_deck.pop())
            self.check_as()


    def print_logo(self):
        """Imprime el logo del juego."""
        os.system('cls')
        print(logo)


    def reset_hands(self):
        """Inicia el juego, mezclando las manos, incializando las variables e imprmiendo el logo."""
        self.game_deck = Deck[:]
        self.print_logo()
        self.shuffle_deck()
        self.start_hands()    

    
    def print_stage(self): 
        """Imprime el estado actual del juego."""
        print(f"""\tYour cards: {self.player_hand}, current score: {self.player_sum()}\n\tComputer's first card: {self.computer_hand[0]}.  Total cards in computer hand: {len(self.computer_hand)}""")


    def players_wants_one_more(self):
        """Verifica si el jugador quiere una carta mas, otrogandole una y devolviendo True en caso de afirmacion."""
        res = input(self.ONE_MORE_STR).lower()
        if res == "y":
            self.player_hand.append(self.game_deck.pop())
            return True
        return False


    def player_wins(self):
        """Verifica si las condiciones de victoria del jugador estan dadas."""
        return (((self.player_sum() > self.computer_sum()) or (self.computer_sum() > 21)) and (self.player_sum() <= 21))


    def is_tie(self):
        """Verifica si las condiciones de empate estan dadas."""
        return (self.player_sum() == self.computer_sum() and (self.player_sum() <= 21))
    
    
    def print_end(self):
        """Imprime la ultima instancia del juego."""
        self.print_logo()
        print(f"\tYour final hand: {self.player_hand}, final score: {self.player_sum()}\n\tComputer's final hand: {self.computer_hand}, final score: {self.computer_sum()}.")
    

    def play_round(self):    
        self.reset_hands()
        while True:
            self.check_as()
            self.print_stage()
            if not(self.player_sum() <= 21 and self.players_wants_one_more()):
                break
        self.game_deck = Deck[:]
        self.print_end()
        if self.player_wins():
            print("\nYou Win! ☺")
        elif self.is_tie():
            print("\nPush...")
        else:
            print("\nYou Loose :(")


    def start_game(self):
        self.print_logo()
        while self.game_dont_over():
            self.play_round()
        print("Gracias por jugar.")


game = Blackjack()
game.start_game()

















"""------------------------------------------------- CODIGO VIEJO. No Aplicada la orientacion a objetos. ------------------------------------------------------------"""




# STARTING_STR = "\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
# ONE_MORE_STR = "Type 'y' to get another card, type 'n' to pass: "
# game_deck = Deck[:]
# player_hand = []
# computer_hand = []
# player_sum = lambda : sum(player_hand)         # Funcion lamda para obtener el total de la mano del jugador.
# computer_sum = lambda : sum(computer_hand)     # Funcion lamda para obtener el total de la mano del la computadora.


# def shuffle_deck():
#     """Mezcla el mazo original."""
#     shuffle(game_deck)


# def game_dont_over():
#     """Verifica si el jugador tiene intencion de jugar una partida mas."""
#     return input(STARTING_STR).lower() == "y"


# def check_as():
#     """Chequea si existe un as en alguna de las manos. En caso de encontrarlo, lo transforma en un 1 si fuera necesario."""
#     if (11 in player_hand) and (player_sum() > 21):
#         player_hand.remove(11)
#         player_hand.append(1)
#     if (11 in computer_hand) and (computer_sum() > 21):
#         computer_hand.remove(11)
#         computer_hand.append(1)


# def start_hands():
#     """Reinicia las manos iniciales."""
#     player_hand.clear()
#     computer_hand.clear()
#     for _ in range(2):    
#         player_hand.append(game_deck.pop())
#     while computer_sum() < 17:
#         computer_hand.append(game_deck.pop())
#         check_as()


# def print_logo():
#     """Imprime el logo del juego."""
#     os.system('cls')
#     print(logo)


# def start_game():
#     """Inicia el juego, mezclando las manos, incializando las variables e imprmiendo el logo."""
#     game_deck = Deck[:]
#     print_logo()
#     shuffle_deck()
#     start_hands()    

# # Podriamos remplazarlo por una funcion lambda.
# def print_stage(): 
#     """Imprime el estado actual del juego."""
#     print(f"""\tYour cards: {player_hand}, current score: {player_sum()}\n\tComputer's first card: {computer_hand[0]}.  Total cards in computer hand: {len(computer_hand)}""")


# def players_wants_one_more():
#     """Verifica si el jugador quiere una carta mas, otrogandole una y devolviendo True en caso de afirmacion."""
#     res = input(ONE_MORE_STR).lower()
#     if res == "y":
#         player_hand.append(game_deck.pop())
#         return True
#     return False


# def player_wins():
#     """Verifica si las condiciones de victoria del jugador estan dadas."""
#     return ((player_sum() > computer_sum()) or (computer_sum() > 21)) and (player_sum() <= 21)


# def is_tie():
#     """Verifica si las condiciones de empate estan dadas."""
#     return (player_sum() == computer_sum() and (player_sum() <= 21))
# # Podriamos remplazarlo por una funcion lambda.
# def print_end():
#     """Imprime la ultima instancia del juego."""
#     print_logo()
#     print(f"\tYour final hand: {player_hand}, final score: {player_sum()}\n\tComputer's final hand: {computer_hand}, final score: {computer_sum()}.")

# # Inicio del loop de juego.
# print_logo() 
# while game_dont_over():
#     start_game()
#     round_continue = True
#     while round_continue:
#         check_as()
#         print_stage()
#         round_continue = players_wants_one_more() if player_sum() <= 21 else False      
#     game_deck = Deck[:]
#     print_end()
#     if player_wins():
#         print("\nYou Win! ☺")
#     elif is_tie():
#         print("\nPush...")
#     else:
#         print("\nYou Loose :(")
# print("Thanks for playing. ☺") # Mensaje de despedida

