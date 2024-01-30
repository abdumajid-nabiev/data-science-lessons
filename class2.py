#classlar

class Kalkulator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def qosh(a, b):
        return a+b


    def ayir(a, b):
        return a-b


    def kopaytir(a, b):
        return a*b


    def bolish(a, b):
        return a/b



    son1 = int(input("1-SON: "))
    son2 = int(input("2-SON: "))
    amal = input("Amalni yozing: ")

    if amal == "-":
        print(ayir(son1, son2))

    if amal == "+":
        print(qosh(son1, son2))

    if amal == "*":
        print(kopaytir(son1, son2))

    if amal == "/":
        print(bolish(son1, son2))


