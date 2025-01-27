
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
        elif 18 < self.T <= 21:
            return (21 - self.T) / (21 - 18)
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
            return a/tg_a
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

    R1 = min(ranges.temp_low(), ranges.room_low())
    R2 = min(ranges.temp_low(), ranges.room_mid())
    R3 = min(ranges.temp_low(), ranges.room_high())
    R4 = min(ranges.temp_mid(), ranges.room_low())
    R5 = min(ranges.temp_mid(), ranges.room_mid())
    R6 = min(ranges.temp_mid(), ranges.room_high())
    R7 = min(ranges.temp_high(), ranges.room_low())
    R8 = min(ranges.temp_high(), ranges.room_mid())
    R9 = min(ranges.temp_high(), ranges.room_high())

    return R1, R2, R3, R4, R5, R6, R7, R8, R9

def rule_aggregation(rules):

    R1, R2, R3, R4, R5, R6, R7, R8, R9 = rules
    L = max(R1, R2, R4)
    M = max(R3, R5, R7)
    H = max(R6, R8, R9)

    return L, M, H


def power_result(rule_aggregation):

    L, M, H = rule_aggregation

    tg_a = 20

    low_start, low_end = 0, 40
    mid_start, mid_end = 20, 80
    high_start, high_end = 60, 100

    P1 = trapeze_area((low_end - low_start) - tg_a * L, low_end - low_start, L)
    P2 = trapeze_area((mid_end - mid_start) - 2 * tg_a * M, mid_end - mid_start, M)
    P3 = trapeze_area((high_end - high_start) - tg_a * H, high_end - high_start, H)

    C1 = 0.5 * ((low_end + low_start) - (0.5 * tg_a * L))
    C2 = 0.5 * (mid_end + mid_start)
    C3 = 0.5 * (high_end + high_start + (0.5 * tg_a * H))
#0.5*(80 + ((H * 20 + 60) + 100)/2) też działa ale mówiąc szczerze nie wiem jak to wymyśliłem
    result = (P1*C1 + P2*C2 + P3*C3)/(P1+P2+P3)

    return result


print(power_result(rule_aggregation(rules(50, 111))))
print(power_result(rule_aggregation(rules(0, 1))))
print(power_result(rule_aggregation(rules(21.5, 21.5))))
print(power_result(rule_aggregation(rules(15, 10))))
