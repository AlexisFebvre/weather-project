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
        output.append(int(nom[numero][i]))

    return output


def minMax(liste: lists):
    """
        retourne la valeur max, min et moyenne d'une liste
    """
    max = liste.



"""MAIN PROGRAM"""

# récuperer le fichier
datas = recupData("donneesMeteo23mars22.csv")

# récuperer les données individuellements
tempExt = recupListe(datas,1)
humExt = recupListe(datas,2)
vent = recupListe(datas,3)
pluie = recupListe(datas,4)





