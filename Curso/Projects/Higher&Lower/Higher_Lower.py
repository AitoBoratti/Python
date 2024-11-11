import Data as d
import random as r
from os import system as sys

class Higher_Lower():
    QUESTION = "Who has more followers? Type 'A' or 'B':"
    FAIL_STR = "Sorry, that's wrong. Final score:"
    CORRECT_STR = "You're right! Current score:"
    CONGRATULATION_STR = "Congratulations, you have managed to answer all the questions correctly! Have a cookie!"
    WARNING_STR = """               
                    ¡¡¡WARNING!!!
              ¡Only A or B is accepted! 
              
             Click any key to continue...
    """


    def __init__(self):
        self.score = 0
        self.game_data = d.data
        self.first_data = self._get_random_data()
        self.second_data = None


    def _print_logo(self):
        sys("cls")
        print(d.logo)


    def _print_fail(self):
        self._print_logo()
        print(f"{self.FAIL_STR} {self.score}")


    def _print_flawless_victory(self):
        self._print_logo()
        print(self.CONGRATULATION_STR)
        print(d.cookie)


    def _print_warning(self):
        sys("cls")
        input(self.WARNING_STR)


    def _get_random_data(self):
        return self.game_data.pop(r.randint(0, len(self.game_data) - 1))
 
 
    def _display_data(self, data, label):
        print(f"{label}: {data['name']}, a {data['description']}, from {data['country']}.")


    def print_stage(self, win=False):
        self._print_logo()
        if win:
            print(f"{self.CORRECT_STR} {self.score}")
        self._display_data(self.first_data, "Compare A")
        print(d.vs)
        self._display_data(self.second_data, "Against B")


    def _have_data(self):
        return (len(self.game_data) != 0)
    
    
    def check_answer(self):
        res = input(self.QUESTION).capitalize()
        if res not in ['A', 'B']:
            self._print_warning()
            return None
        return ((res == "A" and self.first_data["follower_count"] > self.second_data["follower_count"]) or
                (res == "B" and self.first_data["follower_count"] < self.second_data["follower_count"]))


    def play(self):
        while self._have_data():
            self.second_data = self._get_random_data()
            self.print_stage(bool(self.score))
            
            correct = self.check_answer()
            
            if correct:
                self.first_data = self.second_data
                self.score += 1
            elif correct is None:
                self.first_data = self._get_random_data()
            else:
                self._print_fail()
                break
            
        if not self._have_data():
            self._print_flawless_victory()

# Test
game = Higher_Lower()
game.play()
