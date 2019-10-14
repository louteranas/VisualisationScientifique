class Polygone:
    def __init__(self, points = []):
        self.points = points;

    def partialDecompose(n):
        for i in range(n//2):
            self.points[i] = (0.25 * (-self.points[(2*i-2)%length(self.points)] +
                                    3*self.points[(2*i-1)%length(self.points)] + 
                                    3*self.points[(2*i)%length(self.points)] - 
                                    self.points[(2*i+1)%length(self.points)]));
            self.points[i + (n//2)] = (0.25 * (self.points[(2*i-2)%length(self.points)] -
                                    3*self.points[(2*i-1)%length(self.points)] + 
                                    3*self.points[(2*i)%length(self.points)] - 
                                    self.points[(2*i+1)%length(self.points)]));
    
    def partialRecompose(n):
        for i in range(n):
            self.points[2*i] = 0.75 * (self.points[i] + self.points[n + i]) + 
                               0.25 * (self.points[i + 1] - self.points[n + i + 1]);
            self.points[2*i +1] = 0.25 * (self.points[i] + self.points[n + i]) +
                                  0.75 * (self.points[i + 1] - self.points[n + i + 1]);
                                  