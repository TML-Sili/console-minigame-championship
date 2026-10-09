from tic_tac_toe import *
from math_duel import *
from connect_four import *
import os
import random


class Player:
    """Klasse die Informationen über einzelnen Spieler hat"""

    def __init__(self, name):
        global all_players
        self.wins = 0
        self.name = name
        self.sign = "UNKNOWN"  # wird in Spielen nacher definiert
        self.game_points = 0



class Spieler:
    """Klasse mit allen spieler und Rangliste"""

    def __init__(self, players):
        self.spieler = players
        self.ranking_l = []  # Liste in mit Spieler in richtiger Reihenfolge nach Wins geordet.

    def ranking(self):
        """" gibt Liste zurück in richtiger Reihenfolge [0] = 1. Platz. [1] = Zweiter Platz."""
        """hier wird ranking sortiert."""
        if self.spieler[0].wins > self.spieler[1].wins:
            self.ranking_l = [self.spieler[0], self.spieler[1]]
        else:
            self.ranking_l = [self.spieler[1], self.spieler[0]]
        if self.spieler[0].wins == self.spieler[1].wins:
            return "Es ist unentschieden:"
        else:
            return self.ranking_l[0].name + " ist am gewinnen:"

    def print_ranking(self, end=False):
        """printet das ranking"""
        if end:
            print("Der Endpunktestand ist: ")
        else:
            print("Der Gesamtpunktestand sieht wie folgt aus:")
            print(self.ranking())
        for draw in self.ranking_l:
            print(draw.name, ":", draw.wins)


class Game(Spieler):
    #KlassenVariablen
    objects = 0

    """Klasse spiel mit infos und Spiel das aktuell gespielt wird."""
    @classmethod
    def clear_console(cls):
        """cleart die Konsole"""
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    @classmethod
    def explain_game(cls):
        print("Zwei Spieler werden sich in drei Games so lange batteln, bis sie keine Lust mehr haben. Die 3 Games bestehen aus: Tic Tac Toe, 4 Gewinnt und einem 1*1 Mathe-duel. Die Spiele werden zufällig ausgewählt.")
        print("Zudem kann zwischen zwei Moden ausgewählt werden und zwar zwischen nur einem Spiel spielen und der Meisterschaft, wo alle drei gespielt werden.")

    def __init__(self):
        super().__init__(all_players)
        type(self).objects += 1
        self.mode = "Meisterschaft"  # oder Singlegame muss aber im spiel ausgewählt werden.
        self.games = ["Tic tac toe", "Math Duel", "4 Gewinnt"]
        self.current_game = random.choice(self.games)

    def choose_game(self):
        """Methode mit der man beim Singleplayer-mode das Spiel auswählen kann."""
        while True:
            choose_game = input("[\"1\" = Tic-Tac_Toe, \"2\" = Math Duel, \"3\" = 4 gewinnt] schreibe die Nummer, um das Spiel zu wählen. ")
            if choose_game == "1":
                self.current_game = "Tic tac toe"
            elif choose_game == "2":
                self.current_game = "Math Duel"
            elif choose_game == "3":
                self.current_game = "4 Gewinnt"
            else:
                print("Ungültiges Zeichen")
                continue
            print(f"Ihr werdet nun {self.current_game} spielen. have fun!")
            break

    def end_game(self):
        """Zeigt den Endbildschirm und wer gewonnen hat."""
        type(self).clear_console()
        self.print_ranking(True)
        if self.ranking_l[0].wins == self.ranking_l[1].wins:
            print("Unentschieden, ihr wart euch auf Augenhöhe.")
        else:
            print(f"{self.ranking_l[0].name} hat das Spiel gewonnen, GRATULATION!")
        last_hit = input("Press ENTER")

    def game_loop(self):
        """Endlos-schleife, die Programm steuert."""
        global Main_game
        while True:
            if self.current_game == "Tic tac toe":
                """Hier wird Tic_tac Toe Gesteuert"""
                tic_tac_toe_grid = Tic_tac_Grid(self.spieler)
                while tic_tac_toe_grid.active:
                    tic_tac_toe_grid.paint_grid()
                    tic_tac_toe_grid.move()
                End = self.next_game(self.current_game, tic_tac_toe_grid)
                if End == "END":
                    self.end_game()
                    break
                elif End == "RESTART":
                    Main_game = start_game()
                    Main_game.game_loop()
                    break
            elif self.current_game == "Math Duel":
                """Hier wird math duel Gesteuert"""
                Math_game = Duel(self.spieler)
                while Math_game.active:
                    Math_game.create_rechnungen()
                End = self.next_game(self.current_game, Math_game)
                if End == "END":
                    self.end_game()
                    break
                elif End == "RESTART":
                    Main_game = start_game()
                    Main_game.game_loop()
                    break
            else:
                """Hier wird 4 gewinnt Gesteuert"""
                connect_four_grid = connect_four(self.spieler)
                while connect_four_grid.active:
                    connect_four_grid.paint_grid()
                    connect_four_grid.move()
                End = self.next_game(self.current_game, connect_four_grid)
                if End == "END":
                    self.end_game()
                    break
                elif End == "RESTART":
                    Main_game = start_game()
                    Main_game.game_loop()
                    break

    def next_game(self, last_game, Grid):
        """geht zum nächsten game oder bleibt falls man nur ein game spielen möchte. fragt auch ob man rangliste sehen möchte. Managet auch ob noch weiter gespielt werden will oder nicht."""
        self.print_ranking()
        restart_value = input("Wenn ihr das Spiel neustarten wollt, schreibt \"JA\" in CAPS LOCK. Sonst Enter. ")
        if restart_value == "JA":
            return "RESTART"
        end = input("Falls ihr das ganze Spiel beenden möchtest schreibe\"QUIT\" in CAPS LOCK. sonst ENTER. ")
        Grid.active = True
        if end == "QUIT":
            return "END"
        if self.mode == "Singlegame":
            next_game = input("Wenn ihr dein aktuelles Spiel wechseln möchtest, schreibe\"JA\" in CAPS LOCK. Sonst ENTER. ")
            if next_game == "JA":
                self.choose_game()
            else:
                self.current_game = last_game
        else:
            if len(self.games) - 1 == 0:
                self.games = ["Tic tac toe", "Math Duel", "4 Gewinnt"]
            else:
                for delete in range(len(Main_game.games)):
                    if self.games[delete] == last_game:
                        self.games.pop(delete)
                        break
            self.current_game = random.choice(Main_game.games)
        input(f"Drücke ENTER um mit dem nächsten Spiel: {self.current_game} fortzufahren.")


def start_game():
    """wird einmal aufgerufen um alle notwendigen Informationen zu erhalten, um Game zu starten. Bestimmt modus."""
    global all_players
    all_players = []
    Game.clear_console()
    print("Herzlich willkommen zu den Minispielmeisterschaften in Python.")
    if Game.objects < 1:
        Game.explain_game()
    print("Created by: Silas and Gregor.")
    for take_players in range(1, 3):
        player = str(take_players)
        spieler_name = input("Wie soll der " + player + ".Spieler heissen? ")
        all_players += [Player(spieler_name)]
    game = Game()
    mode = input("Falls ihr nur ein Game spielen möchtet, schreibt \"1\" sonst ENTER. ")
    if mode == "1":
        game.mode = "Singlegame"
        game.choose_game()
    else:
        input("Viel Spaß bei der Meisterschaft. Möge der Bessere gewinnen. Drücke ENTER, um erstes Spiel zu starten.")
    return game


# Startvariablen
all_players = []
Main_game = start_game()

# Hauptprogramm aufrufen
Main_game.game_loop()

