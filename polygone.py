#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

class Polygone:
    def __init__(self, points = []):
        self.points = points

    def partialDecompose(self, n, seuil):
        pointstemp = list(self.points)
        lengthPoints = n
        for i in range(n // 2):
            pointstemp[i] = (0.25 * (- self.points[(2 * i - 2) % lengthPoints] +\
                                (3 * self.points[(2 * i - 1) % lengthPoints]) +\
                                (3 * self.points[(2 * i) % lengthPoints]) -\
                                 self.points[(2 * i + 1) % lengthPoints]))
            pointstemp[i + (n // 2)] = 0.25 * (self.points[(2 * i - 2) % lengthPoints] -\
                                    3 * self.points[(2 * i - 1) % lengthPoints] + \
                                    3 * self.points[(2 * i) % lengthPoints] - \
                                    self.points[(2 * i + 1) % lengthPoints])
            pointstemp[i + (n // 2)] = pointstemp[i + (n // 2)] if (seuil == None or (abs(pointstemp[i + (n // 2)][0]) >= seuil and abs(pointstemp[i + (n // 2)][1]) >= seuil)) else np.array([0.0, 0.0])
        self.points = pointstemp

    def partialRecompose(self, n):
        pointstemp = list(self.points)
        for i in range(n):
            pointstemp[2 * i] = 0.75 * (self.points[i] + self.points[n + i]) + \
                               0.25 * (self.points[(i + 1) % n] - self.points[n + ((i + 1) % n)])
            pointstemp[2 * i + 1] = 0.25 * (self.points[i] + self.points[n + i]) +\
                                  0.75 * (self.points[(i + 1) % n] - self.points[n + ((i + 1) % n)])
        self.points = pointstemp

    def decompositionTotale(self, seuil = None):
        n = len(self.points)
        while n > 4:
            self.partialDecompose(n, seuil)
            n //= 2

    def recompositionTotale(self):
        n = 4
        while n < len(self.points):
            self.partialRecompose(n)
            n *= 2


    def getCoordonneesPoints(self):
        x, y = [], []
        for point in self.points:
            x.append(point[0])
            y.append(point[1])
        return x, y


    def draw(self, n):

        x, y = self.getCoordonneesPoints()

        plt.plot(x[:n] + [x[0]], y[:n] + [y[0]])

        plt.show()
