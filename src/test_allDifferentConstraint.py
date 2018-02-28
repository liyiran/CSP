from unittest import TestCase

from hw2cs561s2018 import AllDifferentConstraint


class TestAllDifferentConstraint(TestCase):
    def test_all_diff(self):
        # variables, domains, assignments
        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        all_diff = AllDifferentConstraint()
        self.assertEqual(0, all_diff(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        all_diff = AllDifferentConstraint()
        self.assertEqual(0, all_diff(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1}
        all_diff = AllDifferentConstraint()
        self.assertEqual(1, all_diff(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 2, 'c': 3, 'e': 1}
        all_diff = AllDifferentConstraint()
        self.assertEqual(1, all_diff(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 1, 'c': 3, 'd': 4, 'e': 1}
        all_diff = AllDifferentConstraint()
        self.assertEqual(2, all_diff(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 1, 'c': 2, 'd': 2, 'e': 1}
        all_diff = AllDifferentConstraint()
        self.assertEqual(3, all_diff(variables, None, assignments))
