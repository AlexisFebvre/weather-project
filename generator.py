import csv, math
import matplotlib.pyplot as plt

## FONCTIONS ##
# récupère les données d'un ficher (Alexis)
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

# (Alexis)
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

# min, max, moyenne (Alexis)
def minMax(liste: list):
    """
        retourne la valeur max, min et moyenne d'une liste
    """
    _max = max(liste)
    _min = min(liste)
    mean = sum(liste)/len(liste)

    return (_max, _min, mean)



"""MAIN PROGRAM"""

# récuperer le fichier (Alexi)
datas = recupData("donneesMeteo27jan12.csv")

# récuperer les données individuellements (Alexis)
tempExt = recupListe(datas,1)   # températures en °C
humExt = recupListe(datas,2)    # humidité en %
vent = recupListe(datas,3)      # force du vent en km/h
pluie = recupListe(datas,4)     # précipiptations en unité de 0.1mm

print(minMax(tempExt))

# récupération des moyennes, minimales et maximales (Alexis)
tempMeta = minMax(tempExt)
tempMini, tempMaxi, tempMoyenne = tempMeta[0],tempMeta[1],tempMeta[2]


# Cumul précipitations (Ulysse)
def cumulPrecipitation(pluie):
    cumulprecip = []
    for i in range(len(pluie)):
        cumulprecip.append(0.1 * (pluie[i]))
    return sum(cumulprecip)

cumul = cumulPrecipitation(pluie)

# Création des images (Ulysse)
def genImagePlot(liste,moyenne,titreDuGraphique,nomFichierImage, passerMoyenne=False):
    axeX = [j for j in range(0,len(liste))]

    plt.plot(axeX, liste, label=titreDuGraphique)   # les valeures
    # pour pouvoir faire des graphiques sans afficher la moyenne
    if not passerMoyenne:
        plt.plot(axeX, [moyenne for i in range(len(axeX))], label=f"moyenne: {math.ceil(moyenne*10)/10}") # la moyenne des valeurs

    plt.legend()
    plt.savefig(nomFichierImage)
    plt.close()



# Generer toutes les images (Ulysse)
genImagePlot(tempExt, tempMoyenne, "Températures exterieures en °C", "tempExt.png") # températures exterieurs
genImagePlot(humExt, minMax(humExt)[2], "Humidité exterieures en %", "humExt.png") # humidité
genImagePlot(vent, minMax(vent)[2], "Vitesse du vent en km/h", "vent.png") # vent
genImagePlot(pluie, minMax(pluie)[2], "Précipitations en "+str(math.ceil(cumul*10)/10)+" mm", "pluie.png", True) # précipitation

