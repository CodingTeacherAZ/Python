import numpy as np
import pandas as pd

# Create initial snake-ordered grid
def generate_snake_grid(student_ids, rows=5, cols=8):
    grid = np.zeros((rows, cols), dtype=int)
    index = 0
    for r in range(rows):
        if r % 2 == 0:
            # Left to right
            for c in range(cols):
                grid[r][c] = student_ids[index]
                index += 1
        else:
            # Right to left
            for c in reversed(range(cols)):
                grid[r][c] = student_ids[index]
                index += 1
    return grid

# Initial student IDs
student_ids = list(range(40))

# Apply rotation
rotation_amount = 7
rotated_ids = student_ids[-rotation_amount:] + student_ids[:-rotation_amount]

# Generate new seating chart
rotated_grid = generate_snake_grid(rotated_ids)

# Convert to DataFrame for display
seating_chart_df = pd.DataFrame(rotated_grid)
seating_chart_df.columns = [f"Seat {i}" for i in range(1, 9)]
seating_chart_df.index = [f"Row {i}" for i in range(1, 6)]

import caas_jupyter_tools as tools; tools.display_dataframe_to_user(name="Rotation 1 Seating Chart", dataframe=seating_chart_df) 
