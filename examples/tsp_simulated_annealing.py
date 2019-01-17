#!/usr/bin/env python3
import itertools
import random

import matplotlib.pyplot as plt
import numpy as np


def pairwise(iterable):
    """Iterate over the given iterable in pairs.

    pairwise([1, 2, 3, 4]) -> (1, 2), (2, 3), (3, 4)
    """
    a, b = itertools.tee(iterable)
    # Advance b one step
    next(b, None)
    return zip(a, b)


def evaluate(tour: np.ndarray) -> float:
    """Evaluate the length of the given tour.

    Compute the Euclidean distance between every pair of cities in the tour
    and add them together.

    :param tour: An array of cities, where each city is n (x, y) pair.
    :type tour: np.ndarray with shape (n, 2)
    :return: The length of the tour.
    :rtype: float
    """
    return sum(np.linalg.norm(c1 - c2) for c1, c2 in pairwise(tour))


def perturb(x: np.ndarray) -> np.ndarray:
    """Perturb the given array.

    Perform a sublist inversion in the interior of the given array.

    :param x: The array to perturb. Is not modified.
    :type x: np.ndarray
    :return: A perturbed copy of the given array.
    :rtype: np.ndarray
    """
    # Compute two random indices, avoiding the endpoints.
    i = random.randint(0, len(x) - 2)
    j = random.randint(i, len(x) - 1)

    # Produce a copy of the given array and invert a random sublist inside.
    y = np.copy(x)
    y[i:j] = y[i:j][::-1]

    return y


def accept_solution(energy1: float, energy2: float, temperature: float) -> bool:
    """Determine whether to accept a solution given current and previous energies.

    :param energy1: The energy of the current solution.
    :type energy1: float
    :param energy2: The energy of the previous solution.
    :type energy2: float
    :param temperature: The current temperature of the whole system.
    :type temperature: float
    :return: Whether or not to accept the current solution.
    :rtype: bool
    """
    return random.random() < np.exp((energy1 - energy2) / temperature)


def simulated_annealing(cities: np.ndarray, temperature=800, cooling_factor=0.001) -> np.ndarray:
    """Run the simulated annealing algorithm to solve the TSP.

    :param cities: An array of (x, y) city coordinates.
    :type cities: np.ndarray
    :param temperature: The starting temperature of the system, defaults to 800
    :param temperature: int, optional
    :param cooling_factor: How quickly to cool the system, defaults to 0.001
    :param cooling_factor: float, optional
    :return: A locally optimal tour through the given array of cities.
    :rtype: np.ndarray
    """
    current = evaluate(cities)
    i = 0
    while temperature > 0.001:
        new_solution = perturb(cities)
        energy = evaluate(new_solution)
        if accept_solution(current, energy, temperature):
            cities = new_solution
            current = energy

        temperature *= 1 - cooling_factor
        if i % 50 == 0:
            plot(cities, path=True, wait=False)
        i += 1
    return cities


def plot(tour, path=True, wait=False):
    """Plot the given tour.

    :param tour: The tour of cities to plot.
    :type tour: np.ndarray with shape (n, 2)
    :param path: Whether to plot the path through the cities, defaults to True
    :param path: bool, optional
    :param wait: Whether to wait for the user to close the plot, defaults to False
    :param wait: bool, optional
    """
    plt.clf()
    if path:
        # Plot the path with a low zorder so that the cities are drawn on top.
        plt.plot(tour[:, 0], tour[:, 1], color="red", zorder=0)
    plt.scatter(tour[:, 0], tour[:, 1], marker="o", zorder=1)
    plt.axis("off")
    if not wait:
        plt.ion()
    plt.show()
    # Run the GUI event loop for a little bit.
    plt.pause(0.001)


if __name__ == "__main__":
    num_cities = 50
    cities = (np.random.rand(num_cities, 2) * 100).astype(int)
    # Plot the cities and wait for the user to close the plot.
    plot(cities, path=False, wait=True)
    cities = simulated_annealing(cities, temperature=100)
    print("Finished Simulated Annealing")
    plt.ioff()
    plot(cities, path=True, wait=True)
