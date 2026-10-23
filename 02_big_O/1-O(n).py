# O(n) time complexity = number of operations is directly proportional to the input size n
# O(n) drop constants are same as O(n) + O(n) = O(2n) = O(n)

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)