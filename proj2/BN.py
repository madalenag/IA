'''
Taissa Ribeiro - 86514
Madalena Galrinho - 87546
Grupo 11
'''


class Node():

    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents

    
    def computeProb(self, evid):
        prob = 0;

        if len(self.parents) == 0:
            prob = self.prob[0];

        elif len(self.parents) == 1:
            prob = self.prob[evid[self.parents[0]]];

        elif len(self.parents) == 2:
            prob = self.prob[evid[self.parents[0]]][evid[self.parents[1]]]

        return [1 - prob, prob];
    



class BN():
    
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob


    def computePostProb(self, evid):
        pass
               
        return 0
        
        
    def computeJointProb(self, evid):
        jp = 1;
        lenght = len(self.prob);
        
        for i in range(lenght):
            prob = self.prob[i].computeProb(evid[i]);
            
            if i < 2 and evid[i] == 0:
                jp *= prob[0];
            else:
                jp *= prob[1];

        return jp;