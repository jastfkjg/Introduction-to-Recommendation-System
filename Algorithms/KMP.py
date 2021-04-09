"""
Knuth-Morris-Pratt(KMP) 算法
"""

def compute_prefix_function(P):
    m = len(P)
    pi = [0 for _ in range(m+1)]
    k = 0
    for q in range(1, m):
        while k > 0 and P[q] != P[k]:
            k = pi[k]

        if P[q] == P[k]:
            k += 1

        pi[q] = k

    return pi 

def KMP_matcher(T, P):
    n, m = len(T), len(P)
    pi = compute_prefix_function(P)
    q = 0
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q]

        if P[q] == T[i]:
            q += 1

        if q == m:
            print(i-m+1)
            q = pi[q]


if __name__ == "__main__":
    T = "asasdfddffsageasdadsaasddsasdf"
    P = "asdf"
    print("T: ", T)
    print("P: ", P)
    KMP_matcher(T, P)
