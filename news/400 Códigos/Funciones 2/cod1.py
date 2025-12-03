import random

def SantiagoAleat(SantiagoMin, SantiagoMax, SantiagoCant):
    return [random.randint(SantiagoMin, SantiagoMax) for _ in range(SantiagoCant)]

SantiagoNums = SantiagoAleat(14, 33, 12)
print(SantiagoNums)
