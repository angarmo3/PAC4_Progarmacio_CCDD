# Exercici 1

# Per a resoldre els dos punts de l'exercici
# tan sols cal definir el path
# i la funció a cercar en el 1.2

from funcions_exercici_1_PAC4 import ORFs
func = "Respiration"
path = "/home/datasci/prog_datasci_2/activities/activity_4/data/tb_functions.pl"
print("Exercici 1")
print(ORFs(path, func))


# Exercici 2

# Per a resoldre el primer punt de
# l'exercici 2 cal definir el path
# i el patro a cercar

from funcions_exercici_2_PAC4 import ORFspatrons
# Per a quan cerque "protein"
print("Exercici 2")
path = "/home/datasci/prog_datasci_2/activities/activity_4/data/tb_functions.pl"
regex = "protein"
print(ORFspatrons(path, regex))
# Per a quan cercque "hydro"
print("Exercici 2")
path = "/home/datasci/prog_datasci_2/activities/activity_4/data/tb_functions.pl"
regex = "hydro"
print(ORFspatrons(path, regex))


# Exercici 3

# Per a resoldre l'exercici 3
# tan sols cal definir el path

from funcions_exercici_3_PAC4 import ORFsM
path = "/home/datasci/prog_datasci_2/activities/activity_4/data/tb_functions.pl"
print("Exercici 3")
print(ORFsM(path))
