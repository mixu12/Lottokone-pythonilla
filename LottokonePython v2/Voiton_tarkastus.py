import Lottorivi
import Lottokone

class Voiton_tarkastus:
    def __init__(self):
        self.tuliko_voitto = False
    
    def tarkasta_voitto(self, kone: Lottokone.Lottokone, rivi: Lottorivi.Lottorivi):
        self.tuliko_voitto = True
        i = 0
        while (i < len(rivi.getLottorivi())):
            i = i + 1
            if i in kone.get_arvotut_numerot():
                continue
            else:
                self.tuliko_voitto = False
                break
        return self.tuliko_voitto

    def getTulos(self):
        return self.tuliko_voitto




