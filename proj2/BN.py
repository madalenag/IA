'''
Madalena Galrinho - 87546
Taissa Ribeiro - 86514
Grupo 11
'''
import numpy as np


#______________________________________________________________
#
# Class Node
#______________________________________________________________

class Node():

    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents

    

    def computeProb(self, evid):
        l = []
        
        for i in self.parents:
            l.append(evid[i])
        
        p = eval(('self.prob'+'[{}]'*len(l)).format(*l))
        return [1-p, p]


#______________________________________________________________
#
# Auxiliar Functions
#______________________________________________________________


def inferenceEnum(unknown, pos, val, evid, bn):
    res = 0
    evid[pos] = val

    for i in (1, 0):
        evid[unknown[0]] = i

        for j in (1, 0):
            evid[unknown[1]] = j
            res += bn.computeJointProb(evid)
            
    return res


def parseEvid(evid):
    unknown = []

    for i in range(len(evid)):
        if evid[i] == []:
            unknown.append(i)
        elif evid[i] == -1:
            posterior = i

    return posterior, unknown

#______________________________________________________________
#
# Class BN
#______________________________________________________________


class BN():
    
    def __init__(self, gra, prob):
        self.graph = gra
        self.prob = prob


    def computePostProb(self, evid):
        pos, unknown = parseEvid(evid)

        pos_true = inferenceEnum(unknown, pos, 1, list(evid), self)
        pos_false = inferenceEnum(unknown, pos, 0, list(evid), self)

        alfa = 1/(pos_true + pos_false)

        return alfa * pos_true  
   

    def computeJointProb(self, evid):
        jp = 1
        lenght = len(evid)
        
        for i in range(lenght):
            value = self.prob[i].computeProb(evid)
            jp *= value[evid[i]]

        return jp