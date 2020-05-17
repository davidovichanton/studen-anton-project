def find(greek_alphabet, x) -> int:
    """ищет элемент в списк и возвращает индекс"""
    for i, item in enumerate(greek_alphabet):
        if item == x:
            return i

    return -1

def find(greek_alphabet, y) -> int:
    """ищет элемент в списке и возвращает индекс"""
    for i, item in enumerate(greek_alphabet):
        if item == y:
            return i

    return -1

def greek_comparator(x, y) -> int:
    # a = position letter x in alphabet
    # b = position letter y in alphabet
    a = find(greek_alphabet, x)
    b = find(greek_alphabet, y)

    if a == b:
        return 0
    if a > b:
        return 1
    if a < b:
        return -1

greek_alphabet = (
    "alpha",
    "beta",
    "gamma",
    "delta",
    "epsilon",
    "zeta",
    "eta",
    "theta",
    "iota",
    "kappa",
    "lambda",
    "mu",
    "nu",
    "xi",
    "omicron",
    "pi",
    "rho",
    "sigma",
    "tau",
    "upsilon",
    "phi",
    "chi",
    "psi",
    "omega",
)

r1 = greek_comparator("alpha", "beta")
r2 = greek_comparator("alpha", "omega")
r3 = greek_comparator("gamma", "omega")
