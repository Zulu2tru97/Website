import numpy as np
class vector(): #ray make take in a line or make same thing a line could be vector not directed
    def __init__(self, i=0.0, j=0.0, k=0.0):
        self.xcomp = np.array([0,i])
        self.ycomp = np.array([0,j])
        self.zcomp = np.array([0,k])
        
        self.Comp = [self.xcomp,self.ycomp,self.zcomp]
    # def __init__(self, scalar=0): #make self.setScalar retScalar
        # self.scalar = scalar

    def makeNeg(self):  
        self.xcomp *= -1
        self.ycomp *= -1
        self.zcomp *= -1
        return self

    def toStr(self):
        result = str(self.xcomp[1]) + ',' + str(self.ycomp[1]) + ',' + str(self.zcomp[1]) 
        return result

