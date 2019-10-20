#!/usr/bin/env python3

from polygone import Polygone
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import sys
import math

def parsingInput():
    points = []
    with open(sys.argv[1], 'r') as argument:
        texte = argument.read()
        points_str = texte.split("\n")
        for point_str in points_str:
            if point_str != "":
                point = np.array([float(f) for f in point_str.split(" ")])
                points.append(point)
    return points

def distanceInBetween(pointA, pointB):
    return  math.sqrt(pow((pointA[0] - pointB[0]), 2) + pow((pointA[1] - pointB[1]), 2))

def getError(pointsA, pointsB):
    if(len(pointsA)) != len(pointsB):
        print("Problème de taille")
        return
    Sum = 0
    for i in range(len(pointsA)):
        Sum += distanceInBetween(pointsA[i], pointsB[i])
    return math.sqrt(Sum)

def main4():
    print("############## Changement des points puis recompositionTotale ###################")
    print("\n")
    startPoints = parsingInput()
    polygone1 = Polygone(startPoints)
    polygone2 = Polygone(startPoints)
    polygone2.decompositionTotale(0)
    number = int(input("Veuillez entrer le nombre de sommets à déplacer aléatoirement: "))
    for i in range(number):
        polygone2.points[rd.randrange(0, len(polygone2.points))] += np.array([rd.randrange(0, 5),rd.randrange(0, 5)])
    polygone2.recompositionTotale()
    print("Voici votre image recomposée après " + str(number) + " sommet(s) modifiés :")
    input("appuyez sur enter pour continuer....")
    polygone2.draw(len(polygone2.points))

def main3():
    print("############## Calcul d'erreur après recomposition avec un seuil ###################")
    print("\n")
    startPoints = parsingInput()
    errors = []
    indexes = []
    print("Les seuil et les erreurs qui y correspondent seront affiché de la manière suivante:")
    print("Seuil =======> erreur")
    input("appuyez sur enter pour continuer....")
    for i in range(500):
        polygone1 = Polygone(startPoints)
        polygone2 = Polygone(startPoints)
        polygone2.decompositionTotale(i/100)
        polygone2.recompositionTotale()
        errors.append(getError(polygone1.points, polygone2.points))
        print("Seuil : " + str(i/100) + "=======> erreur : " + str(errors[-1]))
        indexes.append(i/100)
    print("Voici le graphe des résultats :")
    input("appuyez sur enter pour continuer....")
    plt.plot(indexes, errors)
    plt.xlabel("Seuil")
    plt.ylabel("Erreur")
    plt.show()


def main1():
    polygone = Polygone(parsingInput())
    print("############## Décomposition puis reconposition sans Seuil ###################")
    print("\n")
    print("=============> Image initial")
    input("Veuillez fermer la fênetre puis appuyez sur Enter pour continuer...")
    polygone.draw(len(polygone.points))
    input()
    print("=============> Traitement en cours...")
    polygone.decompositionTotale(0)
    polygone.recompositionTotale()
    print("=============> Image finale")
    input("Veuillez fermer la fênetre puis appuyez sur Enter pour continuer...")
    polygone.draw(len(polygone.points))


def maintest():
    polygone = Polygone(parsingInput())
    polygone.draw(len(polygone.points))
    input("continue ?")
    polygone.partialDecompose(len(polygone.points))
    polygone.draw(len(polygone.points)//2)
    input("continue ?")
    polygone.partialRecompose(len(polygone.points)//2)
    polygone.draw(len(polygone.points))

def main2():
    ## On parse l'input et on  crée un polygone correspondant
    polygone = Polygone(parsingInput())
    print("############## Décomposition puis reconposition sans Seuil ###################")
    print("\n")
    print("=============> Image initial")
    ## On affiche le polygone avant la décomposition
    input("Veuillez fermer la fênetre puis appuyez sur Enter pour continuer...")
    polygone.draw(len(polygone.points))
    seuil = float(input("Veuilez entrer une valeur pour le seuil (float) ?   "))
    print("=============> Traitement en cours...")
    polygone.decompositionTotale(seuil)
    polygone.recompositionTotale()
    print("=============> Image finale")
    input("Veuillez fermer la fênetre puis appuyez sur Enter pour continuer...")
    polygone.draw(len(polygone.points))

if len(sys.argv) < 2:
    exit("Veuillez saisir un nom de fichier .d")

main1()
print("\n\n\n\n\n\n")
main2()
print("\n\n\n\n\n\n")
main3()
print("\n\n\n\n\n\n")
main4()
print("\n\n\n\n\n\n")
main4()
print("\n\n\n\n\n\n")
main4()
print("\n\n\n\n\n\n")
main4()
print("\n\n\n\n\n\n")
main4()
print("\n\n\n\n\n\n")
