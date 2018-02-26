from unittest import TestCase

from main import Configuration


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
