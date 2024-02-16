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

datas = recupData("donneesMeteo23mars22.csv")

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

print(recupListe(datas, 0))




