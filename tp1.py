#!/usr/bin/env python3

from polygone import Polygone
import numpy as np
import sys

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
    polygone = Polygone(parsingInput())
    input("Affichage avant traitement (Appuyer sur entree)")
    polygone.draw(len(polygone.points))
    seuil = float(input("Quel seuil (float) ?   "))
    polygone.decompositionTotale(seuil)
    #polygone.draw(4)
    input("Affichage après décomposition et recomposition (Appuyer sur entree)")
    polygone.recompositionTotale()
    polygone.draw(len(polygone.points))

if len(sys.argv) < 2:
    exit("Veuillez saisir un nom de fichier .d")

main2()
