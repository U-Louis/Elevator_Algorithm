from random import *

max_charge = 100
number_of_charges = 10
number_of_voyages = 0
numero_du_voyage = [1]
charges = []
voyages = []


def create_charges():
    i = 0
    u = 0
    while i < number_of_charges:
        u = randint(1, max_charge)
        i += 1
        charges.append(u)
    print("Charges générées : ", charges[:])
    print(
        "Charge Totale : ",
        sum(charges),
        "(voyages:",
        int(sum(charges) / max_charge),
        "+)",
    )
    charges.sort()
    print("Charges par ordre croissant : ", charges[:])
    print("")


def creer_base_voyages():
    i = 0
    while i < number_of_charges:
        voyages.append([0])
        i += 1


def creer_un_voyage(voyage):
    if sum(charges) < max_charge:
        print(
            "Le dernier voyage contient :",
            charges[:],
            ", soit un total de :",
            sum(charges),
        )
        del charges[:]
    else:
        voyage = [charges[-1]]
        del charges[-1]
        if sum(voyage) > max_charge:
            envoyer(voyage)
        else:
            peser(voyage)


def peser(voyage):
    while sum(voyage) < max_charge:
        ajouter_paquet(voyage)
    else:
        envoyer(voyage)


def envoyer(voyage):
    while sum(voyage) > max_charge:
        supprimer_le_dernier_paquet(voyage)
    print(
        "Le voyage",
        sum(numero_du_voyage),
        "contient :",
        voyage[:],
        ", soit un total de :",
        sum(voyage),
    )
    numero_du_voyage.append(1)


def ajouter_paquet(voyage):
    voyage.append(charges[0])
    voyage.sort()
    del charges[0]


def supprimer_le_dernier_paquet(voyage):
    charges.append(voyage[0])
    charges.sort()
    del voyage[0]


create_charges()
creer_base_voyages()

while charges:
    creer_un_voyage(voyages)
