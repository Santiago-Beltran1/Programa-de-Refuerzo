import statistics as SantiagoStats

def SantiagoEstasts(SantiagoList):
    return {
        "SantiagoMedia": SantiagoStats.mean(SantiagoList),
        "SantiagoMediana": SantiagoStats.median(SantiagoList),
        "SantiagoDesviacion": SantiagoStats.stdev(SantiagoList)
    }

print(SantiagoEstasts([5.5, 62.4, 54, 21.6, 48]))
