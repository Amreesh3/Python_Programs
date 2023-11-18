def print_n_no(n):
    if n==0:
        return
    
    print_n_no(n-1)
    print(n)
    
print_n_no(5)
