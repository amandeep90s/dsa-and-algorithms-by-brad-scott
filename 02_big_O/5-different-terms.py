# This function has two different terms in the for loops. 
# The first loop runs 'a' times and the second loop runs 'b' times. 
# The time complexity of this function is O(a + b) because the two loops are independent of each other.

def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print_items(1, 10)
