import math


def dehash(hash):
    const = 37
    letters = "acdegilmnoprstuw"

    result = ""
    h = 7

    while True:
        h = int(math.floor(hash / const))
        k = int(hash - h * const)

        if (h < 7 or hash <= 0):
            break

        result = "%s%s" % (letters[k], result)
        hash = (hash - k) / const

    return result
