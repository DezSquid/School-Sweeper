# Validate a minesweeper interior block
# block_data is a two-dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invalid)
def validate(block_data):
    # Check if the input is a 3x3 grid
    if len(block_data) != 3 or any(len(row) != 3 for row in block_data):
        return "Invalid: Input must be a 3x3 grid."

    # Check whether the center block is a bomb, a number, or an invalid input
    center_value = block_data[1][1]

    if center_value == -1:
        return "Invalid: Center block is a bomb."
    elif isinstance(center_value, int) and 1 <= center_value <= 8:
        return "Valid"
    else:
        return "Invalid: Center block must be either a bomb (-1) or a number (1-8)."


# Example usage:
grid = [
    [-1, 1, 0],
    [1, 1, 0],
    [0, 0, 0]
]
print(validate(grid))
