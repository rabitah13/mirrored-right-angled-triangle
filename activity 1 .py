def print_mirrored_right_triangle(rows):
    """
    Prints a mirrored right-angled triangle pattern of a given number of rows.

    Args:
        rows (int): The number of rows the triangle should have.
    """
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        
        for k in range(i):
            print("*", end="")
        
        print()
