from unittest import TestCase

from hw2cs561s2018 import AtMostTwoConstraint


class TestAtMostTwoConstraint(TestCase):
    def test_at_most(self):
        # variables, domains, assignments
        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        at_most = AtMostTwoConstraint()
        self.assertEqual(0, at_most(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        at_most = AtMostTwoConstraint()
        self.assertEqual(0, at_most(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1}
        at_most = AtMostTwoConstraint()
        self.assertEqual(0, at_most(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 2, 'c': 3, 'e': 1}
        at_most = AtMostTwoConstraint()
        self.assertEqual(0, at_most(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 1, 'c': 3, 'd': 4, 'e': 1}
        at_most = AtMostTwoConstraint()
        self.assertEqual(1, at_most(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 1, 'c': 1, 'd': 4, 'e': 5}
        at_most = AtMostTwoConstraint()
        self.assertEqual(1, at_most(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 1, 'c': 1, 'd': 4}
        at_most = AtMostTwoConstraint()
        self.assertEqual(1, at_most(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
        at_most = AtMostTwoConstraint()
        self.assertEqual(3, at_most(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 1, 'c': 3, 'e': 1}
        at_most = AtMostTwoConstraint()
        self.assertEqual(1, at_most(variables, None, assignments))

        variables = ['a', 'b', 'c', 'd', 'e']
        assignments = {'a': 1, 'b': 1, 'c': 3, 'd': 4, 'e': 1}
        at_most = AtMostTwoConstraint()
        self.assertEqual(1, at_most(variables, None, assignments))
