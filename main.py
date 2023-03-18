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
    "No Obstacles - No Goggles", "No Obstacles - No Goggles",
    "No Obstacles - No Blur", "No Obstacles - No Blur",
    "No Obstacles - Low Blur", "No Obstacles - Low Blur",
    "No Obstacles - Medium Blur", "No Obstacles - Medium Blur",
    "No Obstacles - High Blur", "No Obstacles - High Blur",
    "Obstacles - No Goggles", "Obstacles - No Goggles",
    "Obstacles - No Blur", "Obstacles - No Blur",
    "Obstacles - Low Blur", "Obstacles - Low Blur",
    "Obstacles - Medium Blur", "Obstacles - Medium Blur",
    "Obstacles - High Blur", "Obstacles - High Blur",

]

random.shuffle(elements)

print(elements)


# Repeat the process 20 times and print the results for each iteration
for i in range(20):
    grid, objects, random_positions, obstacle, obstacle_position = generate_grid_and_positions()


    print(f"\n\nTrail {i + 1}:")
    print(f"Condition: {elements[i]}:\n")

    if "No Obstacles" in elements[i]:
        continue

    for row in grid:
        print(' '.join(row))



