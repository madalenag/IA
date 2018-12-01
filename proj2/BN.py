'''
Taissa Ribeiro - 86514
Madalena Galrinho - 87546
Grupo 11
'''

import numpy as np
np.set_printoptions(precision=4, suppress=True)


def evidposB(evid):
    return evid[0]
def evidposE(evid):
    return evid[1]
def evidposA(evid):
    return evid[2]


class Node():

    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents

    
    def computeProb(self, evid):
        p = 0;

        if len(self.parents) == 0:
            p = self.prob[0]

        elif len(self.parents) == 1:
            p = self.prob[evid[self.parents[0]]]

        elif len(self.parents) == 2:
            p = self.prob[evid[self.parents[0]]][evid[self.parents[1]]]

        return [1 - p, p];
   
    



class BN():
    
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob


    def computePostProb(self, evid):
        pass
               
        return 0
        
        
    '''
    def computeJointProb(self, evid):
        jp = 1;
        lenght = len(self.prob)
        
        for i in range(lenght):
            prob = self.prob[i].computeProb(evid)

            if i < 2 and evid[i] == 0:
                jp = jp * prob[0]
            else:
                jp = jp * prob[1]

        print(jp)

        return jp;
    '''

    def computeJointProb(self, evid):
        jp = 1
        
        for i in range(len(evid)):
            value = self.prob[i].computeProb(evid)
            jp *= value[evid[i]]

        return jp