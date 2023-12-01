"""Gopher population simulator

Psuedocode

import random
SIMULATION_LENGTH = 10
MINIMUM_BIRTH_RATE = .1
MAXIMUM_BIRTH_RATE = .2
MINIMUM_DEATH_RATE = .05
MAXIMUM_DEATH_RATE = .25


gopher_population = 1000
repeat SIMULATION_LENGTH times
    gopher_population_growth = calculate_gopher_population_growth(gopher_population)
    gopher_population_shrinkage = calculate_gopher_population_shrinkage(gopher_population)
    gopher_population = gopher_population_growth + gopher_population_shrinkage + gopher_population
    print gopher_population_growth, gopher_population_shrinkage, gopher population

function calculate_gopher_population_growth(gopher population)
    return a random number between MINIMUM_BIRTH_RATE * gopher population and MAXIMUM_BIRTH_RATE * gopher_population

function calculate_gopher_population_shrinkage(gopher population)
    return a random number between MINIMUM_DEATH_RATE * gopher population and MAXIMUM_DEATH_RATE * gopher_population

"""

from random import randint

SIMULATION_LENGTH = 10
MINIMUM_BIRTH_RATE = .1
MAXIMUM_BIRTH_RATE = .2
MINIMUM_DEATH_RATE = .05
MAXIMUM_DEATH_RATE = .25


def main():
    """Gopher population simulator"""
    gopher_population = 1000
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {gopher_population}")
    print()
    for i in range(1, SIMULATION_LENGTH + 1):
        population_growth = calculate_population_change(gopher_population, MINIMUM_BIRTH_RATE, MAXIMUM_BIRTH_RATE)
        population_shrinkage = calculate_population_change(gopher_population, MINIMUM_DEATH_RATE, MAXIMUM_DEATH_RATE)
        gopher_population += population_growth + (population_shrinkage * -1)
        print(f"Year {i}")
        print()
        print(f"{population_growth} gophers were born. {population_shrinkage} died.")
        print(f"Population: {gopher_population}")


def calculate_population_change(population, minimum, maximum):
    """Calculates population change as a percentage of population between minimum and maximum"""
    return randint(int(population * minimum), int(population * maximum))


main()
