
import numpy as np

def trapeze_area(a, b, h):
    return 0.5*(a+b)*h

class Ranges:

    def __init__(self, T, S, P=None):
        self.T = T
        self.S = S
        self.P = P

    def temp_low(self):
        if self.T <= 21:
            return 1
        # elif 18 < self.T <= 21:
        #     return (21 - self.T) / (21 - 18)
        elif 21 < self.T <= 23:
            return (23 - self.T) / (23 - 21)
        else:
            return 0

    def temp_mid(self):
        if 21 < self.T <= 23:
            return (self.T - 21) / (23 - 21)
        elif 23 < self.T <= 25:
            return 1
        elif 25 < self.T <= 27:
            return (27 - self.T) / (27 - 25)
        else:
            return 0

    def temp_high(self):
        if self.T >= 27:
            return 1
        elif 25 < self.T <= 27:
            return (self.T - 25) / (27 - 25)
        elif 27 < self.T <= 29:
            return (29 - self.T) / (29 - 27)
        else:
            return 0

    def room_low(self):
        if self.S <= 10:
            return 1
        elif 10 < self.S <= 13:
            return (13 - self.S) / (13 - 10)
        elif 13 < self.S <= 16:
            return (16 - self.S) / (16 - 13)
        else:
            return 0

    def room_mid(self):
        if 13 < self.S <= 16:
            return (self.S - 13) / (16 - 13)
        elif 16 < self.S <= 19:
            return 1
        elif 19 < self.S <= 22:
            return (22 - self.S) / (22 - 19)
        else:
            return 0

    def room_high(self):

        a = self.S - 19

        tg_a = 22 - 19

        if self.S >= 22:
            return 1
        elif 19 < self.S <= 22:
            return (a/tg_a)
        else:
            return 0

    def power_low(self):
        if self.P <= 20:
            return 1
        elif 20 < self.P <= 40:
            return (40 - self.P) / (40 - 20)
        else:
            return 0

    def power_mid(self):
        if 20 < self.P <= 40:
            return (self.P - 20) / (40 - 20)
        elif 40 < self.P <= 60:
            return 1
        elif 60 < self.P <= 80:
            return (80 - self.P) / (80 - 60)
        else:
            return 0

    def power_high(self):
        if self.P >= 100:
            return 1
        elif 80 < self.P <= 100:
            return (self.P - 80) / (100 - 80)
        else:
            return 0

def rules(T, S):

    ranges = Ranges(T, S)

    rules = []

    rules.append((min(ranges.temp_low(), ranges.room_low()), "Low"))
    rules.append((min(ranges.temp_low(), ranges.room_mid()), "Low"))
    rules.append((min(ranges.temp_low(), ranges.room_high()), "Mid"))
    rules.append((min(ranges.temp_mid(), ranges.room_low()), "Low"))
    rules.append((min(ranges.temp_mid(), ranges.room_mid()), "Mid"))
    rules.append((min(ranges.temp_mid(), ranges.room_high()), "High"))
    rules.append((min(ranges.temp_high(), ranges.room_low()), "Mid"))
    rules.append((min(ranges.temp_high(), ranges.room_mid()), "High"))
    rules.append((min(ranges.temp_high(), ranges.room_high()), "High"))

    return rules

    # R1 = min(ranges.temp_low(), ranges.room_low())
    # R2 = min(ranges.temp_low(), ranges.room_mid())
    # R3 = min(ranges.temp_low(), ranges.room_high())
    # R4 = min(ranges.temp_mid(), ranges.room_low())
    # R5 = min(ranges.temp_mid(), ranges.room_mid())
    # R6 = min(ranges.temp_mid(), ranges.room_high())
    # R7 = min(ranges.temp_high(), ranges.room_low())
    # R8 = min(ranges.temp_high(), ranges.room_mid())
    # R9 = min(ranges.temp_high(), ranges.room_high())
    # return R1, R2, R3, R4, R5, R6, R7, R8, R9

# def rule_aggregation(rules):



# def power_result(p1, c1, p2, c2, p3, c3):

def wyostrzenie(rules):
    num = 0
    den = 0
    for aktywacja, moc in rules:
        if moc == "Low":
            P_range = np.linspace(0, 40, 100)
            for P in P_range:
                num += aktywacja * P
                den += aktywacja
        elif moc == "Mid":
            P_range = np.linspace(20, 80, 100)
            for P in P_range:
                num += aktywacja * P
                den += aktywacja
        elif moc == "High":
            P_range = np.linspace(60, 100, 100)
            for P in P_range:
                num += aktywacja * P
                den += aktywacja
    return num / den if den != 0 else 0


def sterownik(T, S):
    print(f"Temperatura: {T}, Powierzchnia: {S}")
    aktywacje = rules(T, S)
    for aktywacja, moc in aktywacje:
        print(f"Reguła: Moc = {moc}, Aktywacja = {aktywacja:.3f}")
    wynik = wyostrzenie(aktywacje)
    print(f"Wyjściowa moc klimatyzacji: {wynik:.2f}%")
    return wynik

sterownik(21.5, 21.5)
print(rules(21.5, 21.5))