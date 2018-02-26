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
