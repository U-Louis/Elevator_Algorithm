from random import *


def create_charges(number_of_charges: int, max_weight_charge: int) -> int:
    """Créer des charges aléatoires avec un poid maximum 
    
    Args:
        number_of_charges (int): Nombre de charge
        max_weight_charge (int): poids maximum d'une charge 
    
    Examples:
        >> print(create_charges(5, 3))
        [1,2,0,1,2]
    """

    charges = []
    for _ in range(number_of_charges):
        charges.append(randint(1, max_weight_charge))

    return sorted(charges)


def create_voyages(charges: list, max_weight: int, voyages=[]) -> list:
    """Retournes une liste de voyages

    Il s'agit d'une fonction recursive ! 

    Args:
        charges (list): Listes des charges 
        max_weight (int): Description
    """

    #  On met le plus lourd au début ...

    charges = [charges[-1]] + charges[:-1]

    total = 0
    #  On parcourt du début à la fin
    for i, val in enumerate(charges):

        # Si le poids total depasse le seuil
        # Alors on crée un voyage
        if total + val > max_weight:
            #  Création d'un voyage
            voyages.append(tuple(charges[:i]))

            #  On fait un appel recursive sur les valises restantes
            charges = charges[i:]
            create_voyages(charges, max_weight, voyages)
            return voyages
        else:
            total += val

    # La derniere valise qui reste ..
    voyages.append(charges)

    return voyages


if __name__ == "__main__":

    max_weight_charge = 10
    number_of_charges = 5

    charges = create_charges(number_of_charges, max_weight_charge - 1)
    print("Charges générées:", charges)

    voyages = create_voyages(charges, max_weight=max_weight_charge)
    for numero, voyage in enumerate(voyages):
        print(
            "Le voyage {} contient : {}, soit un total de : {} ".format(
                numero, voyage, sum(voyage)
            )
        )
