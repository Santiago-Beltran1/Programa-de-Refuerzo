SantiagoB= [
    [4, 111, 10],
    [3, 22, 77],
    [41, 78, 51]
]
SantiagoSumDig = 0
for SantiagoF in range(3):
    SantiagoSumDig += SantiagoB[SantiagoF][SantiagoF]
print(F"La suma de la diagonal principal es igual a: {SantiagoSumDig}")
