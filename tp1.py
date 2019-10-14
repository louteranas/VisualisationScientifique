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
            point = np.array(point_str.split(" "))
            if np.size(point) == 2:
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

def main2():
    polygone = Polygone(parsingInput())
    polygone.draw(len(polygone.points))
    input("continue ?")
    polygone.decompositionTotale()
    polygone.draw(4)
    input("continue ?")
    polygone.recompositionTotale()
    polygone.draw(len(polygone.points))
