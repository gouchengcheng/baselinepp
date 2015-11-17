import numpy as np
import random
import cPickle as pickle

class ProData(object):

    def __init__(self):
        pass

    def transtf2(self,tl):
        if len(tl) == 0:
            return
        tf = [0]
        ori = 0
        for i in xrange(len(tl)):
            if i == 0:
                ori = int(tl[i])
            else:
                tf.append(int(tl[i]) - ori)
        return tf

    def ProAcFile(self, filename = '../data/actionslog.txt',savefile = 'sequence.plk'):

        acfile = open(filename)
        count = 0
        pre_aid = 0

        temp = []
        temp_time = []
        user = []
        time = []

        for lines in acfile:
            line = lines.strip().split(' ')

            aid = int(line[1])
            if aid != pre_aid:
                #print aid, ' ', pre_aid
                if count != 0:
                    user.append(temp)
                    time.append(self.transtf2(temp_time))

                temp = [] #clear series
                temp_time = []
                count = 0 #restart count
                pre_aid = aid
                #print pre_id
            temp.append(int(line[0])) # add uid
            temp_time.append(int(line[2]))
            count += 1
            #if count > 10:
                #print count
            #pre_id = aid
        #save the data
        output = open(savefile,'wb')
        pickle.dump((user, time), output, -1)
        output.close()

class PSH(object):
    filename = ''
    pos = []
    neg = []
    Ni = []
    Nr = []

    def __init__(self, filename):
        self.filename = filename

    def process(self, threshold = 150, savefile= 'data.plk'):
        file = open(self.filename)
        pos = []
        neg = []
        Ni = []
        Nr = []
        count = 0

        for line in file:
            interlist = line.strip().split(' ')

            count_1 = 1
            count_2 = 1
            count_3 = 1
            total_count = 1

            life = 0
            series = []
            for x in interlist:
                life += int(x)
                if life <= 60:
                    count_1 += 1
                    series.append(x)
                if life <= 120:
                    count_2 += 1
                if life <= 180:
                    count_3 += 1
                if life <= 60*24*30:
                    total_count += 1

            #save time series
            if total_count >= threshold: # breaking messages
                pos.append(series)
                Ni.append(count_1)
                Nr.append(total_count)
            elif total_count < (threshold - 10):
                if random.random() < 0.003:
                    neg.append(series)
                    Ni.append(count_1)
                    Nr.append(total_count)

        self.pos = pos
        self.neg = neg
        self.Ni = Ni
        self.Nr = Nr

        #save the data
        output = open(savefile,'wb')
        pickle.dump((self.pos, self.neg, self.Ni, self.Nr), output, -1)
        output.close()

        print "the pos: %d, the neg: %d" % (len(pos),len(neg))

class PML(object):
    filename = ''
    pos = []
    neg = []
    Ni = []
    Nr = []

    def __init__(self, filename):
        self.filename = filename

    #interval = 20 minutes
    def process(self, interval = 20, internum = 3, threshold = 150, savefile = 'dataML.plk'):
        file = open(self.filename)
        pos = []
        neg = []
        Ni = []
        Nr = []
        count = 0

        for line in file:
            interlist = line.strip().split(' ')

            count_1 = 1
            count_2 = 1
            count_3 = 1
            total_count = 1

            life = 0
            series = []
            for x in interlist:
                life += int(x)
                if life <= 60:
                    count_1 += 1
                    series.append(x)
                if life <= 120:
                    count_2 += 1
                if life <= 180:
                    count_3 += 1
                if life <= 60*24*30:
                    total_count += 1

            #save time series
            if total_count >= threshold: # breaking messages
                pos.append(series)
                Ni.append(count_1)
                Nr.append(total_count)
            elif total_count < (threshold - 10):
                if random.random() < 0.003:
                    neg.append(series)
                    Ni.append(count_1)
                    Nr.append(total_count)

        self.pos = pos
        self.neg = neg
        self.Ni = Ni
        self.Nr = Nr

        #save the data
        output = open(savefile,'wb')
        pickle.dump((self.pos, self.neg, self.Ni, self.Nr), output, -1)
        output.close()

        print "the pos: %d, the neg: %d" % (len(pos),len(neg))


