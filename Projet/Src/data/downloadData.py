#!/bin/env python3

import os
import sys
import time

if __name__ == "__main__":

# ARGUMENT 1 = NBRE D'HEURE A PARTIR DU MOMENT OU LA COMMANDE EST EXECUTEE
# ARGUMENT 2 = NOM DU PACKAGE METEOFRANCE A TELECHARGER (SP1, SP2, SP3, HP1)

    if (len(sys.argv) != 4):
    	print("MAUVAIX NOMBRE D'ARGUMENTS. Format : 0^1 HeureDebut HeureFin")
    	sys.exit(1)
    else:
        (nom, isHD, heureDebut, heureFin) = (sys.argv[0], int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        if isHD == 0:
            scriptArome = "RequeteArome.py"
            os.system("rm *.grib2")
            compteur = len([name for name in os.listdir('.') if os.path.isfile(name)])
            #while len([name for name in os.listdir('.') if os.path.isfile(name)]) < compteur + 1:
            #    print(compteur)
            print("###########  Telechargement du contenu SP1  ###########")
            os.system("python2 " + scriptArome + " " + str(heureFin) + " " + "SP1")
            time.sleep(3)
            compteur += 1
            print("###########  Telechargement du contenu IP2  ###########")
            os.system("python2 " + scriptArome + " " + str(heureFin) + " " + "IP2")
            time.sleep(3)
            compteur += 1
            os.system("cat $(ls *.grib2) > donneesSP1IP2.grib2")
        elif isHD == 1:
            ## check if donneesSP1.grib2 AND donneesIP2.grib2 exists and use them
        elif isHD == 2:
            ## check if donneesSP1.nc AND donneesIP2.nc exists and use them

        # elif isHD == 1:
        #     scriptArome = "RequeteAromeHD.py"
        #     os.system("rm *.grib2")
        #     compteur = len([name for name in os.listdir('.') if os.path.isfile(name)])
        #     for i in range(heureDebut, heureFin + 1):
        #         print("NEW I : ", i)
        #         while len([name for name in os.listdir('.') if os.path.isfile(name)]) < compteur + 1:
        #             print(compteur)
        #             os.system("python2 " + scriptArome + " " + str(i) + " " + mode)
        #             time.sleep(3)
        #         compteur += 1
        #     os.system("cat $(ls *.grib2) > donneesGroupees.grib2")
        else:
            sys.exit("0 ou 1 pour le premier parametre svp")
