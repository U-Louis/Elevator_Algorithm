from random import *

MaxCharge = 100
NumberOfCharges = 10
NumberOfVoyages = 0
NumeroDuVoyage = [1]
Charges = []
Voyages = []


def CreateCharges():
    i = 0
    u = 0
    while i < NumberOfCharges:
        u = randint(1, MaxCharge)
        i += 1
        Charges.append(u)
    print("Charges générées : ", Charges[:])
    print("Charge Totale : ", sum(Charges), "(voyages:", int(sum(Charges) / MaxCharge), "+)")
    Charges.sort()
    print("Charges par ordre croissant : ", Charges[:])
    print("")
def CreerBaseVoyages():
    i = 0
    while i < NumberOfCharges:
        Voyages.append([0])
        i += 1


def CreerUnVoyage(voyage):
    if sum(Charges) < MaxCharge:
        print("Le dernier voyage contient :", Charges[:], ", soit un total de :", sum(Charges))
        del Charges[:]
    else:
        voyage = [Charges[-1]]
        del Charges[-1]
        if sum(voyage) > MaxCharge:
            Envoyer(voyage)
        else:
            Peser(voyage)


def Peser(voyage):
    while sum(voyage) < MaxCharge:
        AjouterPaquet(voyage)
    else:
        Envoyer(voyage)


def Envoyer(voyage):
    while sum(voyage) > MaxCharge:
        SupprimerLeDernierPaquet(voyage)
    print("Le voyage", sum(NumeroDuVoyage), "contient :", voyage[:], ", soit un total de :", sum(voyage))
    NumeroDuVoyage.append(1)

def AjouterPaquet(voyage):
    voyage.append(Charges[0])
    voyage.sort()
    del Charges[0]

def SupprimerLeDernierPaquet(voyage):
    Charges.append(voyage[0])
    Charges.sort()
    del voyage[0]


CreateCharges()
CreerBaseVoyages()

while Charges:
    CreerUnVoyage(Voyages)
