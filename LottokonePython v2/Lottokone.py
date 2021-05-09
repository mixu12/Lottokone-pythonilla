from random import randint
import Numero

class Lottokone:
    def __init__(self):
        self.arvotut_numerot =[]
        
    def arvo_numerot(self):
        self.arvotut_numerot.clear()
        while (len(self.arvotut_numerot) < 7):
            arvottu_numero = randint(1, 40)

            if arvottu_numero not in self.arvotut_numerot:
                self.arvotut_numerot.append(arvottu_numero)


    def tulosta_numerot(self):
        for i in self.arvotut_numerot:
            print (i)

    def get_arvotut_numerot(self):
        return self.arvotut_numerot




