import random
import sys
from collections import defaultdict


class Configuration:
    def __init__(self, conf):
        configs = conf.splitlines()
        self.group = int(configs[0])
        self.pot = int(configs[1])
        self.pots = {}
        self.teams = {}
        for pot_num in range(self.pot):
            pot_division = configs[pot_num + 2].split(',')
            self.pots[pot_num] = pot_division  # devisions Russia,Brazil,Argentina
        for team in range(6):
            team_name = configs[2 + self.pot + team].split(':')[0]
            team_string = configs[2 + self.pot + team].split(':')[1]
            one_team = team_string.split(',')
            if not one_team[0] == 'None':
                self.teams[team_name] = one_team


class MinConflictSolver:
    def __init__(self):
        self.constraints = []
        self.domains = {}
        self.vconstraints = {}

    def add_variable(self, variables, domain):
        """
        :param variables: list like [a,b,c] 
        :param domain: list like [1,2,3]
        :return: 
        """
        for var in variables:
            self.domains[var] = domain

    def add_constraint(self, constraint, variables):
        """
        :param constraint: constraint like AllDifferent 
        :param variables: list like [a,b,c]
        :return: 
        """
        # for var in variables:
        self.constraints.append((constraint, variables))

    def get_solution(self, max_step=1000):
        # recording the constraint and all related variables for this variable
        for variables in self.domains:
            self.vconstraints[variables] = []
        for constraint, variables in self.constraints:
            for variable in variables:
                self.vconstraints[variable].append((constraint, variables))
        assignment = {}
        for var in self.domains:
            # random initialize variable
            assignment[var] = random.choice(self.domains[var])
        # print(assignment)
        for _ in range(max_step):
            conflicted = False
            var_list = self.domains.keys()
            for var in var_list:
                # find conflict
                for constraint, variables in self.vconstraints[var]:
                    # find all related constraints and all variables that related to this constraint
                    if 0 != constraint(variables, self.domains, assignment):
                        # a conflict for this variable assignment, resolve it
                        break
                else:
                    continue  # move to the next variable
                # resolve conflict
                min_count = sys.maxint  # at most len(self.vconstraints[var]) conflicts
                # print(min_count)
                values = []  # least conflict assignment condidates
                for value in self.domains[var]:
                    # all possible assignments
                    assignment[var] = value  # assignment the value 
                    counter = 0
                    for constraint, variables in self.vconstraints[var]:
                        violated = constraint(variables, self.domains, assignment)
                        if violated != 0:
                            counter += violated  # one conflict
                    if counter == min_count:
                        values.append(value)
                    elif counter < min_count:
                        # less conflicts
                        min_count = counter
                        values = [value]
                    # print(min_count)
                assignment[var] = random.choice(values)  # randomly choose a value
                # print(assignment, min_count)
                conflicted = True
            if not conflicted:
                return assignment
        return None


class AllDifferentConstraint(object):
    def __call__(self, variables, domains, assignments):
        found = {}
        for var in variables:
            value = assignments.get(var)
            if value is not None:
                if value in found:
                    found[value] += 1
                else:
                    found[value] = 0
        return sum(found.values())


class AtMostTwoConstraint:
    def __call__(self, variables, domains, assignments):
        map = {}
        for var in variables:
            value = assignments.get(var, None)
            if value is not None:
                if not value in map:
                    map[value] = -1
                else:
                    map[value] += 1
        return sum(x for x in map.values() if x > 0)


def solution_generator(solution, group_num):
    if solution is None:
        return 'No'
    else:
        result = "Yes\n"
        output = defaultdict(list)
        for team_name, group in solution.iteritems():
            output[group].append(team_name)
        for group in output:
            result += ",".join(output[group]) + '\n'
        remaining_group = group_num - len(output)
        for _ in range(remaining_group):
            result += "None\n"
        return result.rstrip()


def main():
    with open("input3.txt") as f:
        file_lines = f.read()
        configuration = Configuration(file_lines)
    minConflictSolver = MinConflictSolver()
    for pot in configuration.pots.values():
        minConflictSolver.add_variable(pot, range(0, configuration.group))
        minConflictSolver.add_constraint(AllDifferentConstraint(), pot)
    for team_name, teams in configuration.teams.iteritems():
        if team_name == 'UEFA':
            minConflictSolver.add_constraint(AtMostTwoConstraint(), teams)
        else:
            minConflictSolver.add_constraint(AllDifferentConstraint(), teams)
    solution = minConflictSolver.get_solution()
    with open("output3.txt", 'w') as the_file:
        the_file.write(solution_generator(solution, configuration.group))


if __name__ == "__main__":
    main()
