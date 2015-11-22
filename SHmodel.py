import numpy as np
import math

class LN(object):
    alpha = 0.0    # coefficient
    variance = 0.0
    Nr = None   # y
    Np = None   # predicted y
    precision = 0.0
    recall = 0.0

    def __init__(self):
        print "LN model"

    def train(self, Ni, Nr):
        Ni = np.asarray(Ni,dtype=np.float64)
        self.alpha =  np.sum((np.log(Nr) - np.log(Ni))**2)/len(Ni)
        self.variance = np.sum((np.log(Nr) - np.log(Ni)-np.ones(len(Ni))*self.alpha)**2)/(len(Ni)-1)
        print "alpha: %f, variance: %f" % (self.alpha,self.variance)
        return (self.alpha, self.variance)

    def predict(self, Ni):
        self.Np = np.exp(np.log(Ni) + np.ones(len(Ni))*(self.alpha + self.variance/2) ) #Ni*self.alpha
        return self.Np

    def RSE(self, Nr):
        self.Nr = np.asarray(Nr, dtype=np.float64)
        rse = np.sum((self.Np/self.Nr - 1)**2)
        return rse

    def PR(self, Nr, threshold):
        self.Nr = np.asarray(Nr, dtype=np.float64)
        a=b=c=0.0
        for y, y1 in zip(self.Nr,self.Np):
            if y >= threshold and y1 >= threshold:
                a += 1
            elif y < threshold and y1 >= threshold:
                b += 1
            elif y >= threshold and y1 < threshold:
                c += 1
        if a != 0.0:
            self.precision = a/(a+b)
            self.recall = a/(a+c)
        else:
            self.precision = 0.0
            self.recall = 0.0

        return (self.precision, self.recall)


class CS(object):

    alpha = 0.0    # coefficient
    Nr = None   # y
    Np = None   # predicted y
    precision = 0.0
    recall = 0.0
    def __init__(self):
        print "CS model"

    def train(self, Ni, Nr):
        Ni = np.asarray(Ni,dtype=np.float64)
        Nr = np.asarray(Nr, dtype=np.float64)
        self.alpha = np.sum(Ni/Nr)/np.sum((Ni/Nr)**2)
        print "alpha: %f" % self.alpha
        return self.alpha

    def predict(self, Ni):
        self.Np = Ni*self.alpha
        return self.Np

    def RSE(self, Nr):
        self.Nr = np.asarray(Nr, dtype=np.float64)
        rse = np.sum((self.Np/self.Nr - 1)**2)
        return rse

    def PR(self, Nr, threshold):
        self.Nr = np.asarray(Nr, dtype=np.float64)
        a=b=c=0.0
        for y, y1 in zip(self.Nr,self.Np):
            if y >= threshold and y1 >= threshold:
                a += 1
            elif y < threshold and y1 >= threshold:
                b += 1
            elif y >= threshold and y1 < threshold:
                c += 1
        if a != 0.0:
            self.precision = a/(a+b)
            self.recall = a/(a+c)
        else:
            self.precision = 0.0
            self.recall = 0.0

        return (self.precision, self.recall)
