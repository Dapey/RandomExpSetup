import random

def generate_grid_and_positions():
    # Define the grid size and number of objects
    grid_width = 5
    grid_height = 6
    num_objects = 6

    # Define the objects and additional obstacle
    objects = ['S', 'S', 'M', 'M', 'B', 'B']
    obstacle = 'X'

    # Create a list of all possible grid positions, excluding the first row for the objects
    positions = [(x, y) for x in range(grid_width) for y in range(1, grid_height)]

    # Randomly select positions for the objects
    random_positions = random.sample(positions, num_objects)

    # Add a random position for the obstacle in the first row
    obstacle_position = (random.randrange(grid_width), 0)
    random_positions.append(obstacle_position)

    # Create an empty grid
    grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]

    # Place the objects and obstacle in the grid
    for i in range(num_objects):
        x, y = random_positions[i]
        grid[y][x] = objects[i]

    x, y = obstacle_position
    grid[y][x] = obstacle

    return grid, objects, random_positions, obstacle, obstacle_position





elements = [
    "NG-NO-1", "NG-NO-2", "0-NO-1", "0-NO-2", "L-NO-1", "L-NO-2", "M-NO-1", "M-NO-2", "H-NO-1", "H-NO-2",
    "NG-O-1", "NG-O-2", "0-O-1", "0-O-2", "L-O-1", "L-O-2", "M-O-1", "M-O-2", "H-O-1", "H-O-2",
]

random.shuffle(elements)

print(elements)


# Repeat the process 20 times and print the results for each iteration
for i in range(10):
    grid, objects, random_positions, obstacle, obstacle_position = generate_grid_and_positions()

    print(f"\nIteration {i + 1}:\n")
    for row in grid:
        print(' '.join(row))



