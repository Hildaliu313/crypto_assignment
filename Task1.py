rows = 5  # Number of rows in the pyramid

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
