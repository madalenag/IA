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


def inferenceEnum(unknown, posterior, val, evid, bn):
    res = 0
    evid[posterior] = val

    return recursiveEnum(unknown, evid, bn, res)



def recursiveEnum(unknown, evid, bn,res):
    res = 0
    if len(unknown) == 1:
        for i in (1,0):
            evid[unknown[0]] = i
            res += bn.computeJointProb(evid)
    else:
        for i in (1, 0):
            evid[unknown[0]] = i
            res += recursiveEnum(unknown[1:], evid, bn,res)
    return res



def parseEvid(evid):
    unknown = []
    lenght = len(evid)

    for i in range(lenght):
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
        post, unknown = parseEvid(evid)

        postTrue = inferenceEnum(unknown, post, 1, list(evid), self)
        postFalse = inferenceEnum(unknown, post, 0, list(evid), self)

        alfa = 1/(postTrue + postFalse)
        return alfa * postTrue  
   

    def computeJointProb(self, evid):
        jp = 1
        lenght = len(evid)
        
        for i in range(lenght):
            value = self.prob[i].computeProb(evid)
            jp *= value[evid[i]]

        return jp