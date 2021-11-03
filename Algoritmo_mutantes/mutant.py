import random

'''dna = [
    ['A', 'G', 'G', 'T', 'T', 'A'],
    ['T', 'A', 'C', 'C', 'G', 'G'],
    ['G', 'G', 'A', 'T', 'G', 'G'],
    ['C', 'C', 'T', 'A', 'T', 'T'],
    ['C', 'C', 'T', 'T', 'G', 'G'],
    ['C', 'C', 'T', 'T', 'G', 'G']
]'''

class generateDNA:
    def __init__(self):
        data = 'ATCG'
        self.dna = [[random.choice(data) for i in range(6)] for j in range(6)]
        
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
    #No logro aun realizar esta opcion.
    

def main():
    for i in range(10):
        dna = generateDNA()
        print('===========================================================')
        print(dna)
        print(isMutant(dna.dna))

if __name__ == '__main__':
    main()