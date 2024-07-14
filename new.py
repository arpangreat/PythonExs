def matrix_chain_order(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(1, n):
        m[i][i] = 0
        s[i][i] = 1

    for l in range(2, n + 1):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = int("inf")

            for k in range(1, j + 1):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m


def printp(i, j, bracket, n):
    if i == j:
        print("A", i, end="")
    else:
        print("(", end="")
        printp(i, bracket[i][j], bracket, n)
        printp(bracket[i][j] + 1, j, bracket, n)
        print(")", end="")


def main():
    p = [10, 100, 5, 50]
    n = len(p)

    m = matrix_chain_order(p)

    printp(1, n - 1, m, n)


if __name__ == "__main__":
    main()
