#

for A in range(2):
    for B in range(2):
        X = 0
        if A ^ B:
            X = 1
        print(A, B, "|", X)
        