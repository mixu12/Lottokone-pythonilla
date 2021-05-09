

class Lottorivi:
    def __init__(self):
        self.lottorivi = []

    def setLottorivi(self):
        print("Anna 7 eri numeroa. Paina jokaisen jälkeen Enter")

        while (len(self.lottorivi) < 7):
            numero = input()
            if numero not in self.lottorivi:
                self.lottorivi.append(numero)

    def tulosta_lottorivi(self):
        for i in self.lottorivi:
            print (i)

    def getLottorivi(self):
        return self.lottorivi





