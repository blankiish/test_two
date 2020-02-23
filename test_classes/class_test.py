filePath = 'dataInput.txt'


class Route:

    def __init__(self, beepers, init_coord):
        self.beepers = beepers
        self.init_coord = init_coord
        self.beepers_cnt = len(beepers)

    def print_array(self):
        print(self.beepers)

    def distance(self, beeper_one, beeper_two):
        return abs(beeper_one[0] - beeper_two[0]) + abs(beeper_one[1] - beeper_two[1])

    def total_distance(self):
        return sum([self.distance(point, self.beepers[index + 1]) for index, point in
                    enumerate(self.beepers[:-1])]) + self.addStartEnd()

    def addStartEnd(self):
        return self.distance(self.init_coord, self.beepers[0]) + self.distance(self.init_coord,
                                                                               self.beepers[beepers_cnt - 1])


def permutations(beeper_list):
    if len(beeper_list) == 0:
        return []

    if len(beeper_list) == 1:
        return [beeper_list]

    prem_lst = []

    for i in range(len(beeper_list)):
        m = beeper_list[i]
        remLst = beeper_list[:i] + beeper_list[i + 1:]

        for p in permutations(remLst):
            prem_lst.append([m] + p)
    return prem_lst

def findShortest(routes):
    temp = []
    for route in routes:
        temp.append(route.total_distance())

    return min(temp)

with open(filePath) as fp:
    scenarios_cnt = int(fp.readline())

    scenarios = []
    karel_init_coords = []
    for i in range(scenarios_cnt):
        world_sz = [int(i) for i in fp.readline().split()]
        karel_coords = [int(i) for i in fp.readline().split()]
        beepers_cnt = int(fp.readline())
        temp = []
        for j in range(beepers_cnt):
            temp_coord = [int(i) for i in fp.readline().split()]
            temp.append(temp_coord)
        scenarios.append(temp)
        karel_init_coords.append(karel_coords)

routes = []
for i in range(scenarios_cnt):
    temp = []
    for permutation in permutations(scenarios[i]):
        temp.append(Route(permutation, karel_init_coords[i]))
    routes.append(temp)

print(findShortest(routes[0]))