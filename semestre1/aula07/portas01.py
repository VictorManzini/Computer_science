# Aula de postas lógicas complexas 23/04/2026


# Porta NAND
for A in range(2):
    for B in range(2):
        for C in range (2):
            X = 0
            X1 = 0
            if not(A and not(B and C)):
                X = 1
            if not(A and B and C):
                X1 = 1
            print(A,B,C, "|",X, "   -   ", A, B, C, "|", X1)