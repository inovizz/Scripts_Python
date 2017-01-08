def print_triangles(n):
    """
    This function prints triangles of size n
    """
    for i in range (n,0,-1):
        print(' '*i + '#'*(n+1-i))

print_triangles(5)