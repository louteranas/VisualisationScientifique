#!/usr/bin/env python3

import matplotlib.pyplot as plt

class Polygone:
    def __init__(self, points = []):
        self.points = points;

    def partialDecompose(self, n, seuil = None):
        lengthPoints = len(self.points)
        for i in range(n//2):
            self.points[i] = (0.25 * ( 3*self.points[(2*i-1)%lengthPoints] -\
                                    self.points[(2*i-2)%lengthPoints] +\
                                    3*self.points[(2*i)%lengthPoints] - \
                                    self.points[(2*i+1)%lengthPoints]))
            self.points[i + (n//2)] = (0.25 * (self.points[(2*i-2)%lengthPoints] -\
                                    3*self.points[(2*i-1)%lengthPoints] + \
                                    3*self.points[(2*i)%lengthPoints] - \
                                    self.points[(2*i+1)%lengthPoints]))
            self.points[i + (n//2)] = self.points[i + (n//2)] if (seuil == None or self.points[i + (n//2)] > seuil) else 0

    def partialRecompose(self, n):
        for i in range(n):
            self.points[2*i] = 0.75 * (self.points[i] + self.points[n + i]) + \
                               0.25 * (self.points[i + 1] - self.points[n + i + 1])
            self.points[2*i +1] = 0.25 * (self.points[i] + self.points[n + i]) +\
                                  0.75 * (self.points[i + 1] - self.points[n + i + 1])
    def decompositionTotale(self):
        n = len(self.points)
        while n > 4:
            self.partialDecompose(n)
            n /= 2

    def recompositionTotale(self):
        n = 4
        while n < len(self.points):
            self.partialRecompose(n)
            n *= 2

    def draw(self, n):
        tempArray = self.points[0:n];
        tempArray.append(self.points[0]);
        plt.plot(tempArray);
