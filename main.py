import sys


def alfarray(alphabet="0123456789abcdefghijklmnopqrstwvuxyzABCDEFGHIJKLMNOPQRSTWVUXYZ,. \t\n", file="file.txt"):
    # generating array of signs based on given alphabet and file which is preparation to encode and decode
    toret = []
    signgs = 0
    for sign in alphabet:
        toret.append([sign, 0])
    with open(file, 'r') as f:
        for sign in f.read():
            signgs += 1
            for val in toret:
                if val[0] == sign:
                    val[1] = val[1] + 1
                    break
        f.close()
    return sorted([[val[0], val[1] / signgs] for val in toret if val[1] != 0], key=lambda v: v[1])


array = alfarray()
