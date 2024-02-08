import random

def approximate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        # Generate random coordinates inside the square B
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the circle A
        if x**2 + y**2 < 1:
            points_inside_circle += 1

    # Calculate the approximate value of pi
    approx_pi = 4 * points_inside_circle / num_points

    return approx_pi

def main():
    # Ask the user for the number of random points to generate
    num_points = int(input("Enter the number of random points to generate: "))

    # Calculate the approximate value of pi
    approx_pi = approximate_pi(num_points)

    # Print the approximation of pi
    print("Approximation of pi:", approx_pi)

if __name__ == "__main__":
    main()