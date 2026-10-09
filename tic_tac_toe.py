import os
import random

class Tic_tac_Grid:
    """Erstellt ein Gitter"""
    #Klassenvariablen
    __objects = 0

    @classmethod
    def welcome(cls):
        """Startet das Spiel und erklärt spiel. ("Eröffnungsnachricht") """
        want_Rules = input("Falls du die Regeln anschauen möchtest schreibe \"JA\" in CAPS LOCK. sonst ENTER. ")
        if want_Rules == "JA":
            cls.print_rules()
    @classmethod
    def print_rules(cls):
        """printet Regeln aus"""
        print("Das Ziel ist entweder 3 von deinen Zeichen Diagonal, vertikal oder horizontal in einer Linie zu schaffen. Die Inputs funktionieren wie folgt:" )
        print("1|2|3")
        print("-----")
        print("4|5|6")
        print("-----")
        print("7|8|9")

    @classmethod
    def start_game(cls, player, starter):
        """Gibt den Spieler Infos darüber wer startet und welches Zeichen sie sind"""
        print(player[0].name + " hat das Zeichen: X.")
        print(player[1].name + " hat das Zeichen: O.")
        print(player[starter].name + " Beginnt.")

    @classmethod
    def welcome_message(cls):
        """gibt den Spielern bescheid dass sie in Tic_tac_toe sind"""
        if cls.__objects == 1:
            return "Herzlich willkommen zu Tic Tac Toe. Viel Spass."
        else:
            return "Herzlich willkommen zurück zu Tic Tac Toe. Viel Spass."

    @classmethod
    def clear_console(cls):
        """cleart die Konsole"""
        command = 'clear'
        if os.name in ('nt', 'dos'): command = 'cls'
        os.system(command)

    def __init__(self, players):
        type(self).clear_console()
        self.players = players
        self.active = True
        self.current_player = random.randrange(0, 2)
        players[0].sign = "X"
        players[1].sign = "O"
        self.vertical_blank = "     |     |     "
        self.horizontal_blank = "----- ----- -----"
        self.grid_signs = [" "]*9
        self.available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        type(self).__objects += 1
        print(type(self).welcome_message())
        if type(self).__objects == 1:
            type(self).welcome()
        type(self).start_game(self.players, self.current_player)

    def paint_grid(self):
        """printet das Gitter"""
        for shape in range(11):
            if shape%2 == 0:
                print(self.vertical_blank)
            elif (shape+1)%4 == 0:
                print(self.horizontal_blank)
            else:
                print("  " + self.grid_signs[shape//4*3] + "  |  " + self.grid_signs[shape//4*3+1] + "  |  " + self.grid_signs[shape//4*3+2] + "  ")

    def still_active(self, player):
        """überprüft ob Spieler der gespielt hat gewinnt."""
        for check in range(3):
            if self.grid_signs[check] == player.sign and self.grid_signs[(check+3)] == player.sign and self.grid_signs[(check+6)] == player.sign:
                """überprüft Vertikal"""
                self.paint_grid()
                print(player.name + " hat vertikal gewonnen.")
                player.wins += 1
                return False
            elif self.grid_signs[check*3] == player.sign and self.grid_signs[check*3+1] == player.sign and self.grid_signs[check*3+2] == player.sign:
                """überprüft Horizontal"""
                self.paint_grid()
                print(player.name + " hat horizontal gewonnen.")
                player.wins += 1
                return False
            elif self.grid_signs[0] == player.sign and self.grid_signs[4] == player.sign and self.grid_signs[8] == player.sign:
                self.paint_grid()
                print(player.name + " hat diagonal gewonnen.")
                player.wins += 1
                return False
            elif self.grid_signs[2] == player.sign and self.grid_signs[4] == player.sign and self.grid_signs[6] == player.sign:
                self.paint_grid()
                print(player.name + " hat diagonal gewonnen.")
                player.wins += 1
                return False
        if self.available == []:
            """überprüft ob es noch freie Felder hat."""
            self.paint_grid()
            print("Unentschieden")
            return False
        else:
            return True

    def move(self):
        """überprüft ob Spieler ein gültiges Zeichen hat und setzt es dann anschliessend."""
        available = False
        player = self.players[self.current_player % 2]
        print(f"{player.name} ist an der Reihe. Zeichen: {player.sign}.")
        while True:
            Index = input("Suche dir ein freies Kästchen aus. (1-9) ")
            if player == self.players[0]:
                sign = "X"
            else:
                sign = "O"
            if len(Index) != 1 or Index == "0":
                print("Ungültiges Zeichen.")
                continue
            if ord(Index)>=48 and ord(Index)<=57:
                Index = int(Index)
            else:
                print("Gebe eine Zahl ein.")
                continue
            for check_available in self.available:
                if check_available == Index:
                    available = True
                    pass
                else:
                    continue
            if available:
                self.grid_signs[Index-1] = sign
            else:
                print("Nehme ein freies Kästchen.")
                continue
            for delete in range(len(self.available)):
                if Index == self.available[delete]:
                    self.available.pop(delete)
                    break
            type(self).clear_console()
            self.active = self.still_active(player)
            self.current_player += 1
            break

