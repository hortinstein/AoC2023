#read input file
f = open("../src/d12/p1input", "r")

from functools import cache

# https://github.com/MeisterLLD/aoc2023/blob/main/12.py
# https://topaz.github.io/paste/#XQAAAQDHBwAAAAAAAAAzHIoib6poHLpewxtGE3pTrRdzrponK3G2+gEMNmwefrkefwQ1vDXdKWgv9knBLeHLQ4ukWlwUj2P2xpxepuW10RZGQj3WjidBrErjUpO2ohIUiakR0Sd50/MYcyfsljlcBYHcXm2SbFnYFDUvMiwKFJtYhcuqzNa2MNdPHKA7SjGCmvMWlLJwLQG1aq5VL/IThiOp3PH1IcaTZ4covrdj072idHE35OlYQzdcKkYyhyoJN83RF2P+0Yv4F6j02xPg1iNifR6QC4zn/1pWPvdQmQxrCQXRyrrQ2BlVTaLj3ADmoSbd61DcL/QiUM8JCgh9tiR5P0ZLR1qg/vS9jvl1jX+y4b1FkDTiRrnJYvcsNl/+d2+DFf76Rr+Exh5oPAjT67t+kghhLAUoABECfKPtFi2Vlal/BZts+3HwYQtHKukdWlhmOjXwMM8TaiwlhnH2/BYBa9Hs/jV0bJREi1TJoRYTrAOeNEW1oAS1KpRNQHWwwsifri1yw3ubIrl62CyssgXVnymgZIEq0HXFCSmLP0BXz9irJDGf9k1UAEUPtdBF+TccY/cyoRGe4KsCDwrUz00oRKynFpH+mT5PYHWF3j8T8YZNM9gBaRn0AlQiRVhHyGilKZBBuymqtvCuvoRn+9kg6iwCl4totR7IrrnyjWmFkts7gNdi5CLH4ObwegBUrLn/+SgI+eL7u9gFmDTj/puyankjSdG8phBiuEqKWPdemm2w6UO9m89OjzCGoqJqaEZDtOfoZnHBCMij+aN5z5emmax9n3j3rp7ho++7/rmQwfb2dzjrkzQczLpU8tyt3PJnNwXkjswmlENjqaP9TtcQDSlaTo9RTBZZ0CDzCMOWt76WYTFRSKQG9zwKMt9kIJubXxRp97n8wHihwK0xETLGH8auISso9liQyfNy7zFUowCAn3aIDbTApSFQ1eYBVAktyT5YPwmLyL/YEoPng40ZZM0iduno/64+0ergTE33yCUJENAAlR3ArlCftwi8oI9jOOdX5o2v6tj9nLp+
# https://github.com/rabuf/advent-of-code/blob/master/python/aoc2023/day12.py
# trying to understand this solution

@cache
def solver(springs,broken_groups):
    return 

for line in f:
    springs,broken = line.split(' ')
    broken = [int(x) for x in broken.split(',')]
    print(solver(tuple(springs),tuple(broken)))
