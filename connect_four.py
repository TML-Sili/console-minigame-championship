import os
import random

class connect_four:
    """Erstellt eine Klasse four_wins die alle wichtigen Infos hat um das Game zu leiten. in der Main schleife."""
    #Klassenvariablen
    __objects = 0
    @classmethod
    def welcome(cls):
        """Startet das Spiel und erklärt spiel. ("Eröffnungsnachricht") """
        want_Rules = input("Falls du die Regeln anschauen möchtest schreibe \"JA\" in CAPS LOCK.sonst ENTER. ")
        if want_Rules == "JA":
            cls.print_rules()
    @classmethod
    def print_rules(cls):
        print("Das Ziel ist entweder 4 von deinen Zeichen Diagonal, vertikal oder horizontal in einer Linie zu schaffen. Die Zeichen kommen immer an die nächsthohe Stelle. Die Inputs funktionieren wie folgt:")
        print("|1|2|3|4|5|6|7|")
        print("---------------")
        print("| | | | | | | |")

    @classmethod
    def welcome_message(cls):
        """gibt den Spielern bescheid, dass sie in 4 gewinnt sind"""
        if cls.__objects==1:
            return "Herzlich willkommen zu 4 gewinnt. Viel Spass"
        else:
            return "Herzlich willkommen zurück zu 4 Gewinnt. Viel Spass"

    @classmethod
    def start_game(cls, player, starter):
        """Gibt den Spieler Infos darüber wer startet"""
        print(f"{player[starter].name} startet zuerst.")

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
        self.available = [1, 2, 3, 4, 5, 6, 7] #Liste mit Freien Spalten.
        self.top_line = "|  1  |  2  |  3  |  4  |  5  |  6  |  7  |"
        self.blank_horizontal = "-------------------------------------------"
        self.grid_signs = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
        type(self).__objects += 1
        print(type(self).welcome_message())
        if type(self).__objects == 1:
            type(self).welcome()
        type(self).start_game(self.players, self.current_player)

    def check_top(self, spalte):
        """sucht in spalte die nächste position auf der y position."""
        for position in range (len(self.grid_signs[spalte])-1, -1, -1):
            if self.grid_signs[spalte][position] != " ":
                return position+1
            elif position == 0:
                return position

    def paint_grid(self):
        """printet das Gitter."""
        print(self.top_line)
        for paint in range(5, -1, -1):
            print(self.blank_horizontal)
            print(f"|  {self.grid_signs[0][paint]}  |  {self.grid_signs[1][paint]}  |  {self.grid_signs[2][paint]}  |  {self.grid_signs[3][paint]}  |  {self.grid_signs[4][paint]}  |  {self.grid_signs[5][paint]}  |  {self.grid_signs[6][paint]}  |")
        print(self.blank_horizontal)

    def still_active(self, player):
        """überprüft ob Spieler der gespielt hat gewinnt."""
        for x in range(7):
            for y in range(3):
                if self.grid_signs[x][y] == player.sign and self.grid_signs[x][y + 1] == player.sign and self.grid_signs[x][y + 2] == player.sign and self.grid_signs[x][y + 3] == player.sign:
                    """überprüft vertikal"""
                    self.paint_grid()
                    print(player.name + " hat vertikal gewonnen.")
                    player.wins += 1
                    return False
        for y in range(6):
            for x in range(4):
                if self.grid_signs[x][y] == player.sign and self.grid_signs[x+1][y] == player.sign and self.grid_signs[x+2][y] == player.sign and self.grid_signs[x+3][y] == player.sign:
                    """überprüft horizontal"""
                    self.paint_grid()
                    print(player.name + " hat horizontal gewonnen")
                    player.wins += 1
                    return False
        for y in range(3):
            for x in range(7):
                """überprüft diagonal"""
                if x < 4: #links nach rechts"/"
                    if self.grid_signs[x][y] == player.sign and self.grid_signs[x+1][y+1] == player.sign and self.grid_signs[x+2][y+2] == player.sign and self.grid_signs[x+3][y+3] == player.sign:
                        self.paint_grid()
                        print(player.name + " hat diagonal gewonnen")
                        player.wins += 1
                        return False
                if x > 2: #rechts nach link"\"
                    if self.grid_signs[x][y] == player.sign and self.grid_signs[x-1][y+1] == player.sign and self.grid_signs[x-2][y+2] == player.sign and self.grid_signs[x-3][y+3] == player.sign:
                        self.paint_grid()
                        print(player.name + " hat diagonal gewonnen")
                        player.wins += 1
                        return False


        if self.available == []:
            """überprüft ob es noch freie Felder hat."""
            print("Unentschieden")
            self.paint_grid()
            return False
        else:
            return True

    def move(self):
        """überprüft ob Spieler ein gültiges Zeichen hat und setzt es dann anschliessend."""
        available = False
        player = self.players[self.current_player % 2]
        print(f"{player.name} ist an der Reihe. Zeichen: {player.sign}")
        while True:
            Index = input("Suche dir eine freie Spalte aus. (1-7) ")
            if player == self.players[0]:
                sign = "X"
            else:
                sign = "O"
            if len(Index) != 1 or Index == "0":
                print("Ungültiges zeichen.")
                continue
            if ord(Index) >= 48 and ord(Index) <= 55:
                Index = int(Index)
            else:
                print("Gebe eine Zahl ein (1-7).")
                continue
            for check_available in self.available:
                if check_available == Index:
                    available = True
                    pass
                else:
                    continue
            if available:
                self.grid_signs[Index-1][self.check_top(Index-1)] = sign
            else:
                print("Diese Spalte ist bereits voll.")
                continue
            for delete in range(len(self.available)):
                if Index == self.available[delete] and self.grid_signs[Index-1][5] != " ":
                    self.available.pop(delete)
                    break
            type(self).clear_console()
            self.active = self.still_active(player)
            self.current_player += 1
            break

