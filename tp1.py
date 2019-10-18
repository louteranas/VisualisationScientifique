#!/usr/bin/env python3

from polygone import Polygone
import numpy as np
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


def main3():
    startPoints = parsingInput()
    errors = []
    indexes = []
    for i in range(500):
        polygone1 = Polygone(startPoints)
        polygone2 = Polygone(startPoints)
        polygone2.decompositionTotale(i/100)
        polygone2.recompositionTotale()
        errors.append(getError(polygone1.points, polygone2.points))
        indexes.append(i/100)
    plt.plot(errors, indexes)
    plt.show()
        

def main1():
    polygone = Polygone(parsingInput())
    polygone.draw(len(polygone.points))
    input("continue ?")
    polygone.decompositionTotale()
    polygone.draw(4)
    input("continue ?")
    polygone.recompositionTotale()
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

    input("Affichage avant traitement (Appuyer sur entree)")
    ## On affiche le polygone avant la décomposition
    polygone.draw(len(polygone.points))
    seuil = float(input("Quel seuil (float) ?   "))
    polygone.decompositionTotale(seuil)
    
    input("Affichage après décomposition et recomposition (Appuyer sur entree)")
    polygone.recompositionTotale()
    polygone.draw(len(polygone.points))

if len(sys.argv) < 2:
    exit("Veuillez saisir un nom de fichier .d")

main3()
