import numpy as np
import matplotlib.pyplot as plt
from modules import find_min_or_max


# Contraint functions
def f1(x): # >=
    return 10 - x

def f2(x): # <=
    return 10 + 10 * x

def f3(x):  # <=
    return 20 + 4 * x

def f4(x): # >=
    return 5 - x / 4

# Cptimization functions
# Erwthma a
def fz1(x1, x2):
    return 2 * x1 - x2

# Erwthma b
def fz2(x1, x2):
    return 11 * x1 - x2

def main():
    # Define the constraints
    d = np.linspace(0, 35, 300)
    x1, x2 = np.meshgrid(d, d)

    x = np.linspace(-100, 100, 3000)

    constraint1 = x1 + x2 >= 10
    constraint2 = -10 * x1 + x2 <= 10
    constraint3 = -4 * x1 + x2 <= 20
    constraint4 = x1 + 4 * x2 >= 20
    constraint5 = x1 >= 0
    constraint6 = x2 >= 0
    feasible_region = constraint1 & constraint2 & constraint3 & constraint4 & constraint5 & constraint6

    ## Intersections
    # constraint1 & constraint2
    a1 = np.array([[1, 1], [-10, 1]])
    b1 = np.array([10, 10])
    intersection1 = np.linalg.solve(a1, b1)

    # constraint2 & constraint3
    a2 = np.array([[-10, 1], [-4, 1]])
    b2 = np.array([10, 20])
    intersection2 = np.linalg.solve(a2, b2)

    # constraint1 & constraint4
    a3 = np.array([[1, 1], [1, 4]])
    b3 = np.array([10, 20])
    intersection3 = np.linalg.solve(a3, b3)

    # constraint4 & constraint5
    intersection4 = [20, 0]

    intersections = np.array([intersection1, intersection2, intersection3, intersection4])

    ## Finding the minimum value of the optimization functions
    # Erwthma a
    print(f"----------------------Ερώτημα α----------------------")
    minima, point = find_min_or_max(fz1, 
                                    intersections, 
                                    "min")

    print(f"The minimum value of the function is: {minima} at point {point}")

    # Erwthma b
    print(f"----------------------Ερώτημα β----------------------")
    minima, point = find_min_or_max(fz2, 
                                    intersections, 
                                    "min")

    print(f"The minimum value of the function is: {minima} at point {point}")

    ## Plots
    # Feasible region
    plt.imshow( (feasible_region).astype(int), 
                    extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha = 0.3)

    # Constraint plots
    plt.plot(x, f1(x), label='x1 + x2 >= 10')
    plt.plot(x, f2(x), label='-10x1 + x2 <= 10')
    plt.plot(x, f3(x), label='-4x1 + x2 <= 20')
    plt.plot(x, f4(x), label='x1 + 4x2 >= 20')

    # Ιntersection points
    for intersection in intersections:
        plt.plot(*intersection, 'ro')

    # Sauces
    plt.xlim(-1, 35)
    plt.ylim(-1, 35)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()








