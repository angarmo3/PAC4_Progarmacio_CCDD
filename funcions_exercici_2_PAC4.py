# Importem llibreries
import matplotlib.pyplot as plt
import re


def ORFspatrons(path, regex):
    '''
    Funció que retorna l nombre de classes que contenen

    com a mínim un ORF amb el patró indicat a la seva descripció

    Args:
        path: string amb la ruta on guardem els fitxers

        regex: paraula clau per a la funció

    Returns:
        Número de classes que contenen el patró
        almenys una vegada i gràfic de barres.
    '''

    # Definim diccionari que emprarem més endavant
    classe = {}
    # Cerquem i llegim el fitxer
    with open(path, "r") as fitxer:
        # Anem línia a lína
        for linia in fitxer:
            # En cas que cerquem el patró hydro
            if regex == "hydro":
                # Mirarem si la línia conté "hydro"
                if re.findall(regex, linia):
                    # I si pertany a una paraula de 13 caràcters
                    if re.findall(r"\b\w{13}\b", linia):
                        # Identiciarem quina és la seqüència identificadora
                        # [X,X,X,X] amb un regex:
                        classes = str(re.findall
                                      (r"\[\d{1,2},\d{1,2},\d{1,2},\d{1,2}\]",
                                       linia))
                        # Posem el comptador per a aqueixa
                        # classe en el diccionari
                        classe[classes] = 0
                        # Si la ĺínia correspon a una funció
                        if re.findall(r"^function", linia):
                            # Identiciarem quina és la seqüència identificadora
                            # [X,X,X,X] amb un regex:
                            classes = str(re.findall
                                          (r"\[\d{1,2},\d{1,2},\d{1,2},\d{1,2}\]",
                                           linia))
                            # Si correspon a la de la classe
                            # incrementarem el comptador
                            classe[classes] += 1
            # En cas que cerquem qualsevol altre patró
            # repetim els mateixos passos
            # però no filtrem per longitud de l'string
            else:
                if re.findall(regex, linia):
                    classes = str(re.findall
                                  (r"\[\d{1,2},\d{1,2},\d{1,2},\d{1,2}\]",
                                   linia))
                    classe[classes] = 0
                    if re.findall(r"^function", linia):
                        classes = str(re.findall
                                      (r"\[\d{1,2},\d{1,2},\d{1,2},\d{1,2}\]",
                                       linia))
                        classe[classes] += 1

    # Com que se'm demana les classes en què hi haja almenys un hit
    # itere amb un loop tots els ítems per a eliminar aquells que
    # valen 0.
    # Font: https://www.csestack.org/remove-all-0-from-a-dictionary-in-python/
    final = {}
    for funcio, recompte in classe.items():
        if recompte != 0:
            final[funcio] = recompte

    # Retorne el nombre de vegades que apareix el patró
    print("El nombre de classes amb més d'un "
          "ORF amb el format {} és el següent: {}".format(regex, len(final)))

    # Representació gràfica:
    # https://stackoverflow.com/questions/16010869/
    # plot-a-bar-using-matplotlib-using-a-dictionary
    plt.bar(range(len(final)), list(final.values()), align='center')
    plt.xticks(range(len(final)), list(final.keys()), rotation='45')
    plt.show()