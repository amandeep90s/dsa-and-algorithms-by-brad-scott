# n * n = n^2 -- O(n^2) time complexity = number of operations is proportional to the square of the input size n

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_items(10)