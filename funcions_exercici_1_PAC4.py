# Carregue llibreries d'interés
import matplotlib.pyplot as plt
import re


# Definesc la funció per a la primer exercici
def ORFs(path, func):
    '''
    Funció que retorna el nombre d'ORFs per classe.

    També permet compta els ORFs per a una certa classe de funció,

    e.g. "Respiration", "Degradation", "Carbon usage", etc.

    Args:
        path: string amb la ruta on guardem els fitxers

        func: funció de què volem fer el recompte de classes

    Returns:
        Diccionari amb ORFs per classe i gràfic de barres

        Categoria i nombre de classes que contenen una funció.
    '''

    # Definim diccionaris i variables
    # que emprarem més endavant
    classes_orf = {}
    funcio_orf = {}
    f = [0, 0, 0, 0]

    # Llegim el fitxer on tenim la informació
    with open(path, "r") as fitxer:
        # I el recorrem línia a línia amb un for loop
        for linia in fitxer:
            # En cas que la línia comence per una classe
            if re.findall(r"^class", linia):
                # Identiciarem quina és la seqüència identificadora
                # [X,X,X,X] amb un regex:
                classes = str(re.findall
                              (r"\[\d{1,2},\d{1,2},\d{1,2},\d{1,2}\]", linia))
                # La definirem com a key del diccionari classes_orf
                # i iniciarem el comptador
                classes_orf[classes] = 0
                # Per a l'exercici 1.2 miraré si la línia
                # conte la funció que cerque:
                if re.findall(func, linia):
                    # Tornarem a identiciar quina és la
                    # seqüència identificadora
                    # [X,X,X,x] amb un regex:
                    f = str(re.findall
                            (r"\[\d{1,2},\d{1,2},\d{1,2},\d{1,2}\]", linia))
                    # La definirem com a key del
                    # diccionari funcio_orf
                    # i iniciarem un altre comptador
                    funcio_orf[f] = 0
            # En cas que la línia comence per una funció
            elif re.findall(r"^function", linia):
                # Tornarem a identiciar quina és la
                # seqüència identificadora
                # [X,X,X,X] per a la funció
                classes = str(re.findall
                              (r"\[\d{1,2},\d{1,2},\d{1,2},\d{1,2}\]", linia))
                # Per cada coincidència que es
                # produesca amb la classe augmentarem
                # el comptador
                classes_orf[classes] += 1
                # I per a l'exercici 1.2, mirarem si la
                # seqüència identificadora
                # correspon a la de la funció que cerquem
                # per a pujar el recompte
                if classes == f:
                    funcio_orf[f] += 1

    # Representacións gràfiques:
    plt.bar(range(len(classes_orf)),
            list(classes_orf.values()), align='center')
    plt.xticks(range(len(classes_orf)),
               list(classes_orf.keys()), rotation='45')
    plt.show()
    # Font: https://stackverflow.com/questions/16010869/
    # plot-a-bar-using-matplotlib-using-a-dictionary

    # Retorn de resultats:
    print("El nombre d'ORFs per classe al "
          "fitxer és el següent:\n\n{}".format(classes_orf.items()))
    print("\n\nEl nombre d'ORFs per classe "
          "per a la funcio {} és de:\n {}".format(func, funcio_orf))
