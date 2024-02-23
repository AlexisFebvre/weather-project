import csv

## FONCTIONS ##
# récupère les données d'un ficher
def recupData(_filename):
    """
        récupération des données d'un fichier
        retourne une liste de liste sous forme de [nom, val1, val2, ...., valn]
    """
    output = []
    
    file = open(_filename, 'rt')
    csvReader = csv.reader(file, delimiter=";")

    output = [line for line in csvReader]
    return output


def recupListe(nom, numero):
    """
        arguments:
            nom -> les données
            numero -> l'index des données
        retourne une liste de variable selon l'index
    """
    output = []
    for i in range(1, len(nom[numero])):
        output.append(float(nom[numero][i]))

    return output


def minMax(liste: list):
    """
        retourne la valeur max, min et moyenne d'une liste
    """
    _max = max(liste)
    _min = min(liste)
    mean = sum(liste)/len(liste)

    return (_max, _min, mean)



"""MAIN PROGRAM"""

# récuperer le fichier
datas = recupData("donneesMeteo23mars22.csv")

# récuperer les données individuellements
tempExt = recupListe(datas,1)   # températures en °C
humExt = recupListe(datas,2)    # humidité en %
vent = recupListe(datas,3)      # force du vent en km/h
pluie = recupListe(datas,4)     # précipiptations en unité de 0.1mm

print(minMax(tempExt))

# récupération des moyennes, minimales et maximales
tempMeta = minMax(tempExt)
tempMini, tempMaxi, tempMoyenne = tempMeta[0],tempMeta[1],tempMeta[2]


# Cumul précipitations (Ulysse)

def cumulPrecipitation(pluie):
    pass

# Création des images (Ulysse)
