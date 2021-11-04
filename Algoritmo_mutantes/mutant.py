import random
import numpy as np

# A modo de ejemplo para testear
'''dna = np.array([
    ['A', 'G', 'G', 'T', 'T', 'A'],
    ['T', 'A', 'C', 'C', 'A', 'G'],
    ['G', 'G', 'G', 'A', 'G', 'G'],
    ['C', 'C', 'A', 'A', 'T', 'T'],
    ['C', 'C', 'T', 'T', 'G', 'G'],
    ['C', 'C', 'T', 'T', 'G', 'G']
])'''


# Genera una matriz de DNA aleatoria
class generateDNA:
    def __init__(self):
        size = random.randint(4, 10)
        data = 'ATCG'
        self.dna = np.array([[random.choice(data) for i in range(size)] for j in range(size)])
        
    def __str__(self):
        return '\n'.join([''.join(i) for i in self.dna])



def isMutant(dna):
    mutantList = ['AAAA', 'TTTT', 'CCCC', 'GGGG']
    mutant = ''

    #buqueda horizontal
    for y in range(len(dna)):
        for i in range(len(dna[y])):
            mutant += dna[y][i]
        #print('mutant: ', mutant)
        for i in mutantList:
            if mutant.find(i) != -1:
                print('mutant hor: ', mutant)
                return True
        mutant = ''


    #buqueda vertical
    for x in range(len(dna[0])):
        for i in range(len(dna)):
            mutant += dna[i][x]
        #print('mutant: ', mutant)
        for i in mutantList:
            if mutant.find(i) != -1:
                print('mutant ver: ', mutant)
                return True
        mutant = ''

    #buqueda cada diagonal
    diags = [dna[::-1,:].diagonal(i) for i in range(dna.shape[0]+1,dna.shape[1])]
    diags2= [dna[::-1,:].diagonal(-i) for i in range(-dna.shape[0]+1,dna.shape[1])]

    diags.extend(dna.diagonal(i) for i in range(dna.shape[1]-1,-dna.shape[0],-1))
    diags2.extend(dna.diagonal(i) for i in range(dna.shape[1]-1,dna.shape[0],-1))
    arr = ([n.tolist() for n in diags])
    arrInv = ([n.tolist() for n in diags2])

    ltr = [str(arr).replace(",","").replace(" ", "").replace("'","").replace("[","").replace("]","|")]
    rtl = [str(arrInv).replace(",","").replace(" ", "").replace("'","").replace("[","").replace("]","|")]

    for i in range(len(arr)):
        for letter in arr[i]:
            mutant += letter
        #print('mutant: ', mutant)
        for i in mutantList:
            if mutant.find(i) != -1:
                print('mutant diag: ', mutant)
                return True
        mutant = ''
    for i in range(len(arrInv)):
        for letter in arrInv[i]:
            mutant += letter
        #print('mutant: ', mutant)
        for i in mutantList:
            if mutant.find(i) != -1:
                print('mutant diag: ', mutant)
                return True
        mutant = ''
    
    return False

def main():
    dna = generateDNA()
    print('===========================================================')
    print(dna)
    print(isMutant(dna.dna))

if __name__ == '__main__':
    main()