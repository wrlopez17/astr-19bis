import numpy as np

# Function to create a table of sin(x) vs x
def create_sin_table(start, end, num_points):
    # Generating points between start and end
    x_values = np.linspace(start, end, num_points)
    # Calculating sin(x) for each x value
    sin_values = np.sin(x_values)

    # Printing the table
    for x, sin_x in zip(x_values, sin_values):
        print(f"{x:.4f} \t {sin_x:.4f}")

def main():
    # Creating a table of sin(x) vs x from 0 to 2*pi with 1000 entries
    create_sin_table(0, 2*np.pi, 1000)

# Running the main function
if __name__ == "__main__":
    main()
