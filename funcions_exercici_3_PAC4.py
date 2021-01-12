# Importe llibreries
import matplotlib.pyplot as plt
import re


def ORFsM(path):
    '''
    Funció que retorna el nombre de classes que tenen

    com a mínim una dimensió major > 0

    i alhora múltiple d'un enter entre 2 i 9

    (ambdós inclosos)

    Args:
        path: string amb la ruta on tenim els fitxers


    Returns:
        Llista amb el número de classes

        que contenen el patró.
    '''

    # Definim llista i diccionari que
    # emprarem més endavant
    identificadors = []
    dim = {}

    # Obrim i llegim el fitxer d'interés
    with open(path, "r") as fitxer:
        # El recorrem línia a línia
        for linia in fitxer:
            # Em quede amb les classes
            if re.findall(r"class", linia):
                # Identique quina és la seqüència identificadora
                # [X,X,X,X] amb un regex:
                classes = str(re.findall("\d{1,2},\d{1,2},\d{1,2},\d{1,2}", linia))
                # Amb un altre regex obtinc les dimensions
                classes2 = str(re.findall(r"\d{1,2}", classes))
                # Guarde l'identificador a una llista
                identificadors.append(classes2)
        # Inicie uns loops per a interar entre 2 i 9
        for M in list(range(2, 10)):
            # Establesc el comptador a
            # 0 per a cada valor de M
            dim[M] = 0
            # Recorre cada identificador
            for i in identificadors:
                # Separe els elements per coma
                partits = (re.split("'", i))
                # Per a cada element
                for p in partits:
                    # Si és un enter
                    if re.findall("\d{1,2}", p):
                        # I major absolut que 0
                        if int(p) > 0:
                            # I divisible per M
                            if int(p) % M == 0:
                                # Incremente el comptador
                                dim[M] += 1

        # Imprimesc el resultat de la cerca
        print("El nombre de classes amb almenys una "
              "dimensió divisible per M és:\n {}". format(dim))

        # Elabore el gràfic de barres associat
        plt.bar(range(len(dim)), list(dim.values()), align='center')
        plt.xticks(range(len(dim)), list(dim.keys()), rotation='45')
        plt.show()