import Lottorivi
import Lottokone
import Voiton_tarkastus

kone = Lottokone.Lottokone()

rivi = Lottorivi.Lottorivi()
rivi.setLottorivi()


tarkastus = Voiton_tarkastus.Voiton_tarkastus()

arvontakerrat = 0

print ("Aloitetaan arvonta")

while (tarkastus.getTulos() == False):
    kone.arvo_numerot()
    tarkastus.tarkasta_voitto(kone, rivi)

    arvontakerrat = arvontakerrat + 1

print ("Jotta valitsemasi rivi saatiin, piti arvonta suorittaa kertaa.")
print (arvontakerrat)


