from collections import defaultdict
from unittest import TestCase

from main import AllDifferentConstraint, AtMostTwoConstraint, Configuration, MinConflictSolver


class TestConfiguration(TestCase):
    def test_configure(self):
        configuration = Configuration(
            '''3
4
Russia,Brazil,Argentina
Germany,Italy,England
France,Iran,Mexico
USA,Japan,Australia
AFC:Iran,Japan,Australia
CAF:None
OFC:None
CONCACAF:USA,Mexico
CONMEBOL:Brazil,Argentina
UEFA:France,Germany,Italy,England,Russia''')
        self.assertEqual(configuration.group, 3)
        self.assertEqual(configuration.pot, 4)
        self.assertListEqual(configuration.pots[0], ['Russia', 'Brazil', 'Argentina'])
        self.assertListEqual(configuration.pots[1], ['Germany', 'Italy', 'England'])
        self.assertListEqual(configuration.pots[2], ['France', 'Iran', 'Mexico'])
        self.assertListEqual(configuration.pots[3], ['USA', 'Japan', 'Australia'])
        self.assertListEqual(list(configuration.teams.values())[3], ['Iran', 'Japan', 'Australia'])
        self.assertListEqual(list(configuration.teams.values())[1], ['USA', 'Mexico'])
        self.assertListEqual(list(configuration.teams.values())[0], ['Brazil', 'Argentina'])
        self.assertListEqual(list(configuration.teams.values())[2], ['France', 'Germany', 'Italy', 'England', 'Russia'])

    def test_small(self):
        configuration = Configuration(
            '''3
4
Russia,Brazil,Argentina
Germany,Italy,England
France,Iran,Mexico
USA,Japan,Australia
AFC:Iran,Japan,Australia
CAF:None
OFC:None
CONCACAF:USA,Mexico
CONMEBOL:Brazil,Argentina
UEFA:France,Germany,Italy,England,Russia''')
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
        output = defaultdict(list)
        if solution is not None:
            for team_name, group in solution.iteritems():
                output[group].append(team_name)
        print(output)

    def test_big_no_result(self):
        configuration = Configuration(
            '''8
5
Russia,Germany,Brazil,Portugal,Argentina,Belgium,Poland,France
Spain,Peru,Switzerland,England,Colombia,Mexico,Uruguay,Croatia
Denmark,Iceland,Costa Rica,Sweden,Tunisia,Egypt,Senegal,Iran
Australia,Japan,Morocco,Panama,South Korea,Saudi Arabia,USA,Bolivia
Chile,Paraguay,Serbia,Nigeria,Italy,Netherlands,Czech Republic,China
AFC:South Korea,Saudi Arabia,Iran,Japan,Australia,China
CAF:Tunisia,Egypt,Senegal,Morocco,Nigeria
CONCACAF:Mexico,Panama,Costa Rica,USA
CONMEBOL:Brazil,Argentina,Uruguay,Colombia,Peru,Bolivia,Chile,Paraguay
UEFA:France,Germany,England,Russia,Portugal,Belgium,Poland,Switzerland,Croatia,Denmark,Iceland,Serbia,Spain,Sweden,Italy,Netherlands,Czech Republic
OFC:None''')
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
        output = defaultdict(list)
        if solution is not None:
            for team_name, group in solution.iteritems():
                output[group].append(team_name)
        self.assertEqual(0, len(output))

    def test_big_has_result(self):
        configuration = Configuration(
            '''8
5
Russia,Germany,Brazil,Portugal,Argentina,Belgium,Poland,France
Spain,Peru,Switzerland,England,Colombia,Mexico,Uruguay
Denmark,Iceland,Costa Rica,Sweden,Tunisia,Egypt,Senegal,Iran
Australia,Japan,Morocco,Panama,South Korea,Saudi Arabia,USA
Chile,Paraguay,Serbia,Nigeria,Italy,Netherlands,Czech Republic
AFC:South Korea,Saudi Arabia,Japan,Australia,Iran
CAF:Tunisia,Egypt,Senegal,Morocco,Nigeria
CONCACAF:Mexico,Panama,Costa Rica,USA
CONMEBOL:Brazil,Argentina,Uruguay,Colombia,Peru,Chile,Paraguay
UEFA:France,Germany,England,Russia,Portugal,Belgium,Poland,Switzerland,Denmark,Iceland,Serbia,Spain,Sweden,Italy,Netherlands,Czech Republic
OFC:None''')
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
        output = defaultdict(list)
        if solution is not None:
            for team_name, group in solution.iteritems():
                output[group].append(team_name)
        print(output)
