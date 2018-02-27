import random


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
        for _ in range(max_step):
            conflicted = False
            var_list = self.domains.keys()
            for var in var_list:
                # find conflict
                for constraint, variables in self.vconstraints[var]:
                    # find all related constraints and all variables that related to this constraint
                    if not constraint(variables, self.domains, assignment):
                        # a conflict for this variable assignment, resolve it
                        break
                else:
                    continue  # move to the next variable
                # resolve conflict
                min_count = len(self.vconstraints[var])  # at most len(self.vconstraints[var]) conflicts
                values = []  # least conflict assignment condidates
                for value in self.domains[var]:
                    # all possible assignments
                    assignment[var] = value  # assignment the value 
                    counter = 0
                    for constraint, variables in self.vconstraints[var]:
                        if not constraint(variables, self.domains, assignment):
                            counter += 1  # one conflict
                    if counter == min_count:
                        values.append(value)
                    elif counter < min_count:
                        # less conflicts
                        min_count = counter
                        values = [value]
                assignment[var] = random.choice(values)  # randomly choose a value
                conflicted = True
            if not conflicted:
                return assignment
        return None


class AllDifferentConstraint(object):
    def __call__(self, variables, domains, assignments):
        found = []
        for var in variables:
            value = assignments.get(var)
            if value is not None:
                if value in found:
                    return False
                found.append(value)
        return True


class AtMostTwoConstraint:
    def __call__(self, variables, domains, assignments):
        map = {}
        for var in variables:
            value = assignments.get(var, None)
            if value is not None:
                if not value in map:
                    map[value] = 1
                elif map[value] == 1:
                    map[value] = 2
                else:
                    return False
        return True
