matrix = [
    ['A', 'G', 'G', 'T', 'T', 'A'],
    ['T', 'A', 'C', 'C', 'G', 'G'],
    ['G', 'G', 'A', 'T', 'G', 'G'],
    ['C', 'C', 'T', 'A', 'T', 'T'],
    ['C', 'C', 'T', 'T', 'G', 'G'],
    ['C', 'C', 'T', 'T', 'G', 'G']
]

#Recorrido en forma diagonal en matriz
y = 0
x = len(matrix[0])
print( x, y)

#print(matrix[y][x-1], matrix[y][x-2], matrix[y+1][x-1], matrix[y][x-3], matrix[y+1][x-2], matrix[y+2][x-1], matrix[y+2][x-2], matrix[y+3][x-1], matrix[y+3][x-2], matrix[y+4][x-1], matrix[y+4][x-2])

#recorrer matriz de punta superior derecha a punta inferior izquierda
while y < len(matrix):
    while x >= 0:
        print(matrix[y][x], end="")
        x -= 1
    y += 1
    x = len(matrix[0])
    print()
