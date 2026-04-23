# Aula de portas lógicas complexas 23/04/2026

for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                X = 0 
                if not(not(not(A and B)and C) or D):
                    X = 1
                print(A, B, C, D, "|", X)