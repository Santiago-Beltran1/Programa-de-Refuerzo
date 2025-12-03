def SantiagoB_fibonacci(SantiagoN):
    SantiagoSecuen = []
    SantiagoA, SantiagoB = 0, 1
    SantigoCont = 0
    while SantigoCont < SantiagoN:
        SantiagoSecuen.append(SantiagoA)
        SantiagoA, SantiagoB = SantiagoB, SantiagoA + SantiagoB
        SantigoCont += 1
    return SantiagoSecuen

print(SantiagoB_fibonacci(8))
