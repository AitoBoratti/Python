import Data as d
import random as r
from os import system as sys

class Higher_Lower():
    QUESTION = "Who has more followers? Type 'A' or 'B':"
    FAIL_STR = "Sorry, that's wrong. Final score:"
    CORRECT_STR = "You're right! Current score:"
    WARNING_STR = """               
                    ¡¡¡WARNING!!!
              ¡Only A or B is accepted! 
              
             Click any key to continue...
    """


    def __init__(self):
        self.score = 0
        self.game_data = d.data
        self.first_data = self.get_random_data()
        self.second_data = None


    def print_logo(self):
        sys("cls")
        print(d.logo)


    def print_fail(self):
        self.print_logo()
        print(f"{self.FAIL_STR} {self.score}")


    def print_warning(self):
        sys("cls")
        input(self.WARNING_STR)


    def display_data(self, data, label):
        print(f"{label}: {data['name']}, a {data['description']}, from {data['country']}.")


    def print_stage(self, win=False):
        self.print_logo()
        if win:
            print(f"{self.CORRECT_STR} {self.score}")
        self.display_data(self.first_data, "Compare A")
        print(d.vs)
        self.display_data(self.second_data, "Against B")


    def get_random_data(self):
        return self.game_data.pop(r.randint(0, len(self.game_data) - 1))


    def check_answer(self):
        res = input(self.QUESTION).capitalize()
        if res not in ['A', 'B']:
            self.print_warning()
            return None
        return ((res == "A" and self.first_data["follower_count"] > self.second_data["follower_count"]) or
                (res == "B" and self.first_data["follower_count"] < self.second_data["follower_count"]))


    def play(self):
        while True:
            self.second_data = self.get_random_data()
            self.print_stage(bool(self.score))
            
            correct = self.check_answer()
            
            if correct:
                self.first_data = self.second_data
                self.score += 1
            elif correct is None:
                self.first_data = self.get_random_data()
            else:
                break
        self.print_fail()


game = Higher_Lower()
game.play()





# ----------------------------------- Codigo Pre Refactorizacion -----------------------------------------



# score = 0
# game_data = d.data
# QUESTION = "Who has more followers? Type \'A\' or \'B\':"
# FAIL_STR = f"Sorry, that's wrong. Final score:"
# CORRECT_STR = "You're right! Current score:"
# WARNING_STR = """               
#                 ¡¡¡WARNING!!!
#           ¡Only A or B is accepted! 
          
#          Click any key to continue...
# """


# def _print_logo():
#     sys("cls")
#     print(d.logo)


# def print_fail():
#     _print_logo()
#     print(f"{FAIL_STR} {score}")


# def print_warning():
#     sys("cls")
#     input(WARNING_STR)


# def _display_data(data,label):
#     print(f"{label}: {data["name"]}, a {data["description"]}, from {data["country"]}.")


# def print_stage(win=False):
#     _print_logo()
#     if win:
#         print(f"{CORRECT_STR} {score}") 
#     _display_data(first_data,"Compare A")
#     print(d.vs)
#     _display_data(second_data,"Against B")


# def get_random_data():
#     return game_data.pop(r.randint(0,len(game_data)-1))


# def check_answer():
#     res = input(QUESTION).capitalize()
#     if res not in['A','B']:
#         print_warning()
#         return None
#     return (((res == "A") and first_data["follower_count"] > second_data["follower_count"]) or 
#             ((res == "B") and first_data["follower_count"] < second_data["follower_count"]))


# first_data = get_random_data()
# while True:
#     second_data = get_random_data()
#     print_stage(bool(score))     
#     correct = check_answer() 

#     if correct:
#         first_data = second_data 
#         score += 1

#     elif correct is None:
#         first_data = get_random_data()

#     else:
#         break
# print_fail()        
