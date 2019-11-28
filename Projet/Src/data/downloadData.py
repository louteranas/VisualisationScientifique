#!/bin/env python3
import fnmatch
import os
import sys
import time

def fileExists(fileName, fileDir = '.'):
    exists = False
    for file in os.listdir(fileDir):
        if fnmatch.fnmatch(file, fileName):
            exists = True
            return exists
    return exists

def downloadFiles(nom, heureDebut, package):
    scriptArome = "RequeteArome.py"
    os.system("rm *.grib2")
    compteur = len([name for name in os.listdir('.') if os.path.isfile(name)])
    #while len([name for name in os.listdir('.') if os.path.isfile(name)]) < compteur + 1:
    #    print(compteur)
    contenuExists = False
    print("###########  Telechargement du contenu " + package + "###########")
    while(not contenuExists):
        os.system("python2 " + scriptArome + " " + str(heureDebut) + " " + package)
        time.sleep(3)
        for file in os.listdir('.'):
            if fnmatch.fnmatch(file, 'Arome_' + package +'*.grib2'):
                contenuExists = True
                compteur += 1
        if(not contenuExists):
            print("Could not download the " + package + " data, re trying in 5s :")
            time.sleep(5)
    
    
    
    #os.system("cat $(ls *.grib2) > donneesSP1IP2.grib2")

def extractGribFiles(package):
    if(fileExists('Arome_'+package+'*.grib2')):
        print('#### Extracting '+package+' data\n')
        os.system('./wgrib2 Arome_'+package+'*.grib2 -netcdf resultatSP1.nc;')
        
        return True
    return False
    
if __name__ == "__main__":

# ARGUMENT 1 = NBRE D'HEURE A PARTIR DU MOMENT OU LA COMMANDE EST EXECUTEE
# ARGUMENT 2 = NOM DU PACKAGE METEOFRANCE A TELECHARGER (SP1, SP2, SP3, HP1)

    if (len(sys.argv) != 4):
    	print("MAUVAIX NOMBRE D'ARGUMENTS. Format : 0^1 Heure Package")
    	sys.exit(1)
    else:
        (nom, isHD, heureDebut, Package) = (sys.argv[0], int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
        if isHD == 0:
            downloadFiles(nom, heureDebut, Package)
            extractGribFiles(Package)
        elif isHD == 1:
            if(extractGribFiles(Package)):
                pass
            else:
                downloadFiles(nom, heureDebut, Package)
                extractGribFiles(Package)
        elif isHD == 2:
            if(fileExists('resultat'+Package+'.nc')):
                pass
            else:
                if(extractGribFiles(Package)):
                    pass
                else:
                    downloadFiles(nom, heureDebut, Package)
                    extractGribFiles(Package)

        else:
            sys.exit("0 ou 1 ou 2 pour le premier parametre svp")
