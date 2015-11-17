from SHModel import CS, LN
from preprocess import PSH, ProData
import cPickle as pickle
import numpy as np

def CreatData(filename, savename, threshold):
    psh=PSH(filename)
    psh.process(threshold,savename)

def CreatSequence():
    pd = ProData()
    pd.ProAcFile()

def testSHM():
    threshold = 150
    #Load data
    pkl_file = open('data.plk', 'rb')
    pos, neg, Ni, Nr = pickle.load(pkl_file)

    idx = np.random.permutation(len(Ni))
    train_len = round(len(Ni) * 0.8)
    train_idx = idx[:train_len]
    test_idx = idx[train_len:]

    x_train = [Ni[i] for i in train_idx]
    y_train = [Nr[i] for i in train_idx]
    x_test = [Ni[i] for i in test_idx]
    y_test = [Nr[i] for i in test_idx]

    #CS model test
    cs = CS()
    cs.train(x_train, y_train)
    cs.predict(x_test)
    print "RSE: %f" % cs.RSE(y_test)
    print "precision: %f, recall: %f" % cs.PR(y_test,threshold)

    #LN model test
    ln = LN()
    ln.train(x_train, y_train)
    ln.predict(x_test)
    print "RSE: %f" % ln.RSE(y_test)
    print "precision: %f, recall: %f" % ln.PR(y_test,threshold)

if __name__ == "__main__":


    threshold = 150
    #CreatData('../../corpus_g2','data.plk',threshold)  #just run once the pos: 425, the neg: 682

    #Load data
    pkl_file = open('sequence.plk', 'rb')
    _ ,time = pickle.load(pkl_file)


    idx = np.random.permutation(len(Ni))
    train_len = round(len(Ni) * 0.8)
    train_idx = idx[:train_len]
    test_idx = idx[train_len:]

    x_train = [Ni[i] for i in train_idx]
    y_train = [Nr[i] for i in train_idx]
    x_test = [Ni[i] for i in test_idx]
    y_test = [Nr[i] for i in test_idx]

    #CS model test
    cs = CS()
    cs.train(x_train, y_train)
    cs.predict(x_test)
    print "RSE: %f" % cs.RSE(y_test)
    print "precision: %f, recall: %f" % cs.PR(y_test,threshold)

    #LN model test
    ln = LN()
    ln.train(x_train, y_train)
    ln.predict(x_test)
    print "RSE: %f" % ln.RSE(y_test)
    print "precision: %f, recall: %f" % ln.PR(y_test,threshold)
    print 'exit'