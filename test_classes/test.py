import sys
import timeit
import itertools


RUNS = 3
with open('dataInput.txt') as fp:
    scenarios_cnt = int(fp.readline())
    world_size = [int(i) for i in fp.readline().split()]
    karel_coords = [int(i) for i in fp.readline().split()]

    scenarios = []
    for i in range(scenarios_cnt):
        beepers_cnt = int(fp.readline())
        temp = []
        temp.append([1, 1])
        for j in range(beepers_cnt):
            temp_coord = [int(i) for i in fp.readline().split()]
            temp.append(temp_coord)
        scenarios.append(temp)


import math
def cost(route):
    sum = 0
    # Go back to the start when done.
    route.append(route[0])
    while len(route) > 1:
        p0, *route = route
        sum += math.sqrt((int(p0[0]) - int(route[0][0]))**2 + (int(p0[1]) - int(route[0][1]))**2)
    return sum


d = float("inf")
for p in itertools.permutations(scenarios[0]):
    c = cost(list(p))
    if c <= d:
        d = c
        pmin = p
print("Optimal route:", pmin)
print("Length:", d)