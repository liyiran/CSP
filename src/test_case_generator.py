import random
from collections import defaultdict
from random import randint
from unittest import TestCase

from hw2cs561s2018 import AllDifferentConstraint, Configuration, MinConflictSolver


class case_generator(TestCase):
    def test_case_generator(self):
        # print(self.generate_groups())
        for i in range(187, 500):
            config = self.generate_groups()
            with open('auto_gen_config/input' + str(i) + '.txt', 'w') as file:
                file.write(config.__str__())
                print("done: " + str(i))

    def generate_groups(self):
        pot_solver = MinConflictSolver()
        division_solver = MinConflictSolver()
        self.group_num = 100  # 10 groups
        self.group_max_size = 6  # 6 teams in one group
        self.pot = 300
        group = defaultdict(list)
        pot = defaultdict(list)
        division = defaultdict(list)
        last_index = 0
        all_teams = []
        for i in range(self.group_num):
            two_UEFA = bool(random.getrandbits(1))
            if two_UEFA:
                real_group_size = randint(0, self.group_max_size + 1)
            else:
                real_group_size = randint(0, self.group_max_size)
            group_range = range(last_index, last_index + real_group_size)
            group[i] = [str(k) for k in group_range]
            all_teams.extend(group[i])
            last_index += real_group_size
        # we have group_num groups
        # print(group)

        for i in group:  # each group member should in different pots
            pot_solver.add_variable(group[i], range(0, self.pot))
            pot_solver.add_constraint(AllDifferentConstraint(), group[i])

            if len(group[i]) <= 6:
                division_solver.add_variable(group[i], ['AFC', 'CAF', 'CONCACAF', 'CONMEBOL', 'OFC', 'UEFA'])
                division_solver.add_constraint(AllDifferentConstraint(), group[i])
            else:
                division_solver.add_variable([group[i][0]], ['UEFA'])  # fix the first element to UEFA
                division_solver.add_variable(group[i][1:], ['AFC', 'CAF', 'CONCACAF', 'CONMEBOL', 'OFC', 'UEFA'])
                division_solver.add_constraint(AllDifferentConstraint(), group[i][1:])
        pot_solver.add_constraint(UseAllPot(), all_teams)
        for _ in range(10):
            pot_solution = pot_solver.get_solution(max_step=10)
            if not pot_solution is None:
                break
            print('======restart=========')
        # print(pot_solution)
        for _ in range(10):
            division_solution = division_solver.get_solution(max_step=10)
            if not division_solution is None:
                break
            print('======restart=========')
        # print(division_solution)
        for team, pot_number in pot_solution.iteritems():
            pot[pot_number].append(team)
        for team, division_number in division_solution.iteritems():
            division[division_number].append(team)
        config = Configuration(None)
        config.group = self.group_num
        config.pot = self.pot
        config.pots = pot
        config.teams = division
        return config


class UseAllPot:
    def __call__(self, variables, domains, assignments):
        map = set()
        for var in variables:
            value = assignments.get(var, None)
            if value is not None:
                map.add(value)
        return 300 - len(map)
