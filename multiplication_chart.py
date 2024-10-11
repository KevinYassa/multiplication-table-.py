upperLimit = int(input("What is the upper bound of multiplication table? "))
print(f"The multiplication table for 2 to {upperLimit}")

# Print header
print("------" * upperLimit + "--")
print(f"{' ':>6}", end=" ")
for i in range(2, upperLimit + 1):
    print(f"{i:>6}", end="")  # Right-aligning for better formatting
print()
print("------" * upperLimit + "--")
print()
# Print the multiplication table
for j in range(2, upperLimit + 1):
    print(f"{j:<6}|", end="")  # Row label with a separator
    for k in range(2, upperLimit + 1):
        print(f"{j * k:>6}", end="")  # Right-align products
    print()
    print()# New line after each row
