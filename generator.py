import csv

## FONCTIONS ##
# récupère les données d'un ficher
def recupData(_filename):
    output = []
    
    file = open(_filename, 'rt')
    csvReader = csv.reader(file, delimiter=",")

    output = csvReader
    return output

print(recupData("donneesMeteo23mars22.csv"))
