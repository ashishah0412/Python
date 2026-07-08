# Print a solid square grid of stars of size n x n
def print_square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()  # Move to the next line after printing each row        




# print a hollow square grid of stars of size n x n
def print_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if (i>0 and i<n-1) and (j>0 and j<n-1):
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()  # Move to the next line after printing each row  

print("Enter the size of the square grid:")
n = int(input())
print_square(n) 

n = int(input("Enter the size of the hollow square grid:\n"))
print_hollow_square(n)
