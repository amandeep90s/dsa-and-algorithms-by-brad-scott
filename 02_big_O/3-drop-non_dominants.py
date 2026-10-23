# Drop Non Dominants
# O (n^2 + n) we can drop the non-dominant term n and simplify to O(n^2)

def print_items(n):
    for i in range(n): # 0(n^2)
        for j in range(n):
            print(i, j)

    for k in range(n): # O(n)
        print(k)


print_items(10)