import random
import time
import os

class Duel:
    """Erstellt eine Klasse Duel die alle wichtigen Infos hat um das Game zu leiten. in der Main schleife."""
    #Klassenvariablen
    __objects = 0

    @classmethod
    def welcome(cls):
        """Startet das Spiel und erklärt spiel. ("Eröffnungsnachricht") """
        want_Rules = input("Falls du die Regeln anschauen möchtest, schreibe \"JA\" in CAPS LOCK. Sonst ENTER. ")
        if want_Rules == "JA":
            cls.print_rules()

    @classmethod
    def print_rules(cls):
        print("Jeder Spieler wird einmal so lange Mathe aufgaben lösen, bis er eine Rechnung falsch hat. Der, der mehr Aufgaben gelöst hat, gewinnt das Spiel.")
        print("\"+\" ist Plus, \"-\" ist Minus, \"*\" ist mal, \"/\" ist Durch.")

    @classmethod
    def welcome_message(cls):
        """gibt den Spielern bescheid, dass sie in Tic_tac_toe sind"""
        if cls.__objects == 1:
            return "Herzlich willkommen zum Math Duel. Viel Spass"
        else:
            return "Herzlich willkommen zurück zum Math Duel. Viel Spass"

    @classmethod
    def start_game(cls, player, starter):
        """Gibt den Spieler Infos darüber wer startet"""
        print(f"{player[starter].name} startet zuerst.")
        print("WICHTIG: JEDER HAT PRO RECHNUNG NUR 20 SEKUNDEN ZEIT.")

    @classmethod
    def clear_console(cls):
        """cleart die Konsole"""
        command = 'clear'
        if os.name in ('nt', 'dos'): command = 'cls'
        os.system(command)


    def __init__(self, players):
        self.players = players
        self.active = True
        self.current_player = random.randrange(0, 2)
        type(self).clear_console()
        self.congratulations = ["nicht schlecht!", "keep going", "bist du Einstein?", "Eine noch!", "Nicht mehr viel dann hast du den Rekord."]
        self.asked_players = 0
        self.difficulty = 1
        type(self).__objects += 1
        print(type(self).welcome_message())
        if type(self).__objects == 1:
            type(self).welcome()
        type(self).start_game(self.players, self.current_player)

    def create_rechnungen(self):
        """Erstellt eine Aufgabe und gibt über correctness an, ob es richtig ist. Difficulty bestimmt wie schwer die Rechnung ist. Falls es zu ende ist, geht es zurück. zudem gibt es auskunft darüber wer dran ist."""
        while True:
            exam = Rechnung(self.difficulty, self.players[self.current_player % 2])
            if exam.correctness:
                type(self).clear_console()
                self.players[self.current_player % 2].game_points += 1
                self.difficulty = self.players[self.current_player % 2].game_points//4 + 1
                print(f"Streak: {self.players[self.current_player % 2].game_points}")
                print(random.choice(self.congratulations))

            else:
                if self.asked_players + 1 == 2:
                    if self.players[0].game_points > self.players[1].game_points:
                        self.players[0].wins += 1
                        print(f"{self.players[0].name} hat gewonnen.")
                    elif self.players[1].game_points > self.players[0].game_points:
                        self.players[1].wins += 1
                        print(f"{self.players[1].name} hat gewonnen.")
                    else:
                        print("Unentschieden!")
                    print(f"Endstand: {self.players[0].name}: {self.players[0].game_points} | {self.players[1].name}: {self.players[1].game_points}")
                    self.players[0].game_points = 0
                    self.players[1].game_points = 0
                    self.active = False
                    return
                else:
                    print(f"{self.players[self.current_player % 2].name} hatte eine Streak von: {self.players[self.current_player % 2].game_points}")
                    self.current_player += 1
                    self.difficulty = 1
                    self.asked_players += 1
                    print(f"{self.players[self.current_player % 2].name} ist jetzt an der Reihe.")
                    input("Drücke ENTER, um fortzufahren.")
                    type(self).clear_console()


class Rechnung:
    """Erstellt eine Rechnung abhängig von der schwierigkeit"""
    def __init__(self, difficulty, player):
        self.strich_operatoren = ["-", "+"]
        self.punkt_operatoren = ["*", "/"]
        self.length = 1
        self.solution = 0
        self.a = 0
        self.b = 0
        self.operator = self.decide_operator(difficulty, player)
        self.correctness = self.check_solution(player)

    def decide_operator(self, difficulty, player):
        """bestimmt Mathematischen-operatoren. Zudem bestimmt es a und b."""
        #[1-4 strich-operatoren (1-stellig), 5-8 punkt operatoren (1-stellig), 9-12 strich-operatorn (2-stellig),...]
        self.length = player.game_points//8 + 1
        self.a = random.randrange(1, 10 + 50 * (self.length-1))
        self.b = random.randrange(1, 10 + 50 * (self.length-1))
        if difficulty % 2 == 1:
            return random.choice(self.strich_operatoren)
        else:
            return_value = random.choice(self.punkt_operatoren)
            if return_value == "/":
                self.a = self.a * self.b
            return return_value

    def check_solution(self, player):
        """bestimmt lösung und überprüft ob Lösung richtig ist."""
        starttime = time.time()
        print(f"{player.name} was gibt:")
        print (f"{self.a} {self.operator} {self.b} = x")
        if self.operator == "*":
            self.solution = self.a * self.b
        elif self.operator == "/":
            self.solution = self.a // self.b
        elif self.operator == "+":
            self.solution = self.a + self.b
        else:
            self.solution = self.a - self.b
        guess = input("x = ")
        needed_time = time.time()-starttime
        if needed_time > 20:
            print(f"Du hast leider zu lange gebraucht: Lösung war: {self.solution}.")
            return False
        if guess == str(self.solution):
            return True
        else:
            print(f"Falsch die Lösung war: {self.solution}.")
            return False

