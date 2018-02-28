from collections import defaultdict
from unittest import TestCase

from hw2cs561s2018 import AllDifferentConstraint, AtMostTwoConstraint, Configuration, MinConflictSolver, solution_generator


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

    def test_dump_none(self):
        solutions = {'team1': 1, 'team2': 2, 'team3': 3}
        print(solution_generator(solutions, 4))
        self.assertEqual('Yes\nteam1\nteam2\nteam3\nNone', solution_generator(solutions, 4))

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
        print(solution_generator(solution, configuration.group))

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

    def test_case3(self):
        configuration = Configuration(
            '''8
4
Russia,Germany,Brazil,Portugal,Argentina,Belgium,Poland,France
Spain,Peru,Switzerland,England,Colombia,Mexico,Uruguay,Croatia
Denmark,Iceland,Costa Rica,Sweden,Tunisia,Egypt,Senegal,Iran
Serbia,Nigeria,Australia,Japan,Morocco,Panama,South Korea,Saudi Arabia
AFC:South Korea,Saudi Arabia,Iran,Japan,Australia
CAF:Tunisia,Egypt,Senegal,Morocco,Nigeria
CONCACAF:Mexico,Panama,Costa Rica
CONMEBOL:Brazil,Argentina,Uruguay,Colombia,Peru
UEFA:France,Germany,England,Russia,Portugal,Belgium,Poland,Switzerland,Croatia,Denmark,Iceland,Serbia,Spain,Sweden
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
        print(solution_generator(solution, configuration.group))

    def test_case2(self):
        configuration = Configuration(
            '''2
3
Russia,Brazil,Argentina
Germany,Italy,England
France,Mexico
AFC:None
CAF:None
CONCACAF:Mexico
CONMEBOL:Brazil,Argentina
UEFA:France,Germany,Italy,England,Russia
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
        print(solution_generator(solution, configuration.group))

    def test_huge(self):
        configuration = Configuration(
            '''27
25
AHL,WSS,SGB
ZCD,QMQ,AAQ,PLR,VDM
GOL,PXW,FIP
HRJ,YVF
JFV,SDQ
IQG,IHZ,LEN,PKP
QBF,XAO,LFS,GAH
WKL,LVD,JQE,NDT,QZK,REW,HJN
KLV,ROP,NXT,IEV,KRI,YRA,BUS,KCW
TBY,RPW,CPP
RMP,PGU
FSW,DGY,FRY,ADH,AOD
ZLX,GTE
ITJ,KDP,GPM,SFB,YIS
DXU,WBM,UVT,TAN,BSN,SMS,AIL
QNY,JQH,XCZ
PVW,BDD,FRE,VTB,CTZ,JJE,NIY,LKR,HHC
EUE,TNN,PSL
QZS,GGQ,ZUR,JXZ,RPJ
FIV,OFZ,RWF,WIB,BJS,UDP,DWE
HNH,GMA,ASE,ZTQ,LIS,XYE,JFP,WWR,XZJ
LPD,DVC,LYV,LXK
IND,YJW,GUO,SQI,ZLU,LZA
TIT,RGM,DED,BSK,KIP
AXU,FAG,EES,BEP,YWM,KJK,ZYO,TAD,PYO
AFC:EES,QNY,YJW,FSW,RPW,UVT,SQI,ZUR,VTB,TIT,BEP,LPD,SMS,LFS,ZLU,LEN,RPJ,LZA
CAF:IND,GOL,GPM,WBM,LIS,PXW,BSN,BJS,YWM,YRA,JQH,DVC,LYV,ADH,PLR,SGB,FIP,LXK
OFC:KLV,ZCD,ASE,KDP,QZS,RMP,TAN,JQE,NXT,WSS,IEV,JFP,DGY,BSK,KCW,CPP,HHC
CONCACAF:FIV,DXU,GMA,QMQ,EUE,OFZ,ZLX,ZTQ,AAQ,GUO,RWF,AHL,FRE,NDT,JJE,WWR,DED,SFB,VDM,YVF,GAH,PGU,AOD
CONMEBOL:AXU,PVW,IQG,HRJ,BDD,XAO,IHZ,XYE,QZK,KRI,KJK,BUS,NIY,FRY,REW,ZYO,LKR,TAD,HJN,GTE,YIS,PSL,DWE
UEFA:HNH,FAG,TBY,ITJ,QBF,WKL,LVD,ROP,WIB,GGQ,TNN,CTZ,UDP,JFV,RGM,JXZ,SDQ,PKP,AIL,XCZ,XZJ,KIP,PYO''')
        minConflictSolver = MinConflictSolver()
        for pot in configuration.pots.values():
            minConflictSolver.add_variable(pot, range(0, configuration.group))
            minConflictSolver.add_constraint(AllDifferentConstraint(), pot)
        for team_name, teams in configuration.teams.iteritems():
            if team_name == 'UEFA':
                minConflictSolver.add_constraint(AtMostTwoConstraint(), teams)
            else:
                minConflictSolver.add_constraint(AllDifferentConstraint(), teams)
        for _ in range(100):
            solution = minConflictSolver.get_solution()
            if solution is not None:
                break
            print("restart======")
        output = defaultdict(list)
        if solution is not None:
            for team_name, group in solution.iteritems():
                output[group].append(team_name)
        print(solution_generator(solution, configuration.group))
