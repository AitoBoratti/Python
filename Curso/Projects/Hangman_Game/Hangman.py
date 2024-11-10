import data as m
import random as r
import os

# Variables generales.
choosen_word = ""          # Donde se almacena la palabra elegida. 
lifes = 0;                 # Vidas del jugador. No pueden ser mas de seis. 
player_guest = ""          # Espacio vacio donde se almacenan las letras acertadas y se muestran las faltantes.
wasted_letters = [];       # Lista donde almacenaremos las letras ya utilizadas. 


def restart():
    """ Reinicia o inicializa todas las variables."""
    global choosen_word, lifes, player_guest, wasted_letters
    choosen_word = r.choice(m.word_list)
    lifes = 6
    wasted_letters.clear()
    player_guest = ""
    for letter in choosen_word:
        player_guest += " _"


def print_current_stage():
    """ Imprime el estado actual del juego."""
    os.system("cls")
    print(m.logo)
    print(m.stages[lifes])
    print(f"Letras ya usadas: {wasted_letters}\n")
    print(player_guest)


def start_new_game():
    """ Comienza un nuevo juego. """
    restart()
    print_current_stage()


def check_letter(choosen_letter):
    """ Chequea si la letra pasada por parametro exista en la palabra o no."""
    if (choosen_letter in choosen_word) and not (choosen_letter in wasted_letters):
        return True
    return False


def replace_letter():
    """ Remplaza el guion en la posicion correspondiente."""
    space_list = list(player_guest.replace(" ",""))
    for i in range(len(choosen_word)):
        if choosen_word[i] == choosen_letter:
            space_list[i] = choosen_letter
    return " ".join(space_list)


def end_the_game():
    """ Imprime el mensaje de finalizacion de juego correspondiente. Devuelve un valor del que depende si se 
    reinicia o no el juego."""
    res = ""
    if lifes == 0:
        res = input(f"Haz perdido. Tu palabra era {choosen_word}. Te gustaria volver a intentarlo? Y/N: ")
    elif not("_" in player_guest):
        res = input("Haz Ganado! Te gustaria volver a intentarlo? Y/N: ")
    if res.capitalize() == "Y":
        return True
    else: 
        return False


# Loop principal del juego. 
start_new_game()
while not (lifes == 0) and ("_" in player_guest):
    choosen_letter = input("Ingrese su letra seleccionada: ").lower()
     
    if check_letter(choosen_letter):
        player_guest = replace_letter()
    else:
        lifes -= 1
        
    if not choosen_letter in wasted_letters:
        wasted_letters.append(choosen_letter)        
        
    print_current_stage()                       
        
    if end_the_game():
        start_new_game()
print("Gracias por jugar.")    # Mensaje de despedida.  