""" BOAT PROBLEM """

""" 

PROBLEM STATEMENT -
N people on a side of bridge and all need to cross the bridge
Each person takes a time to cross the bridge
Maximum two people can cross at a time with a lamp
Only people having that lamp can cross the bridge and there is just one lamp
When two people cross, time taken would be time for the slower person
Minimise the time taken for all people to cross the bridge

"""

import gurobipy as gp
from gurobipy import GRB

class Optimizer():
    def __init__(self):

        self.readInput()

        while True:
            self.model = gp.Model('BridgeCrossing')
            self.variables()
            self.constraints()
            self.objectiveFunction()
            self.setRunParams()
            if self.model.STATUS not in [GRB.INFEASIBLE, GRB.UNBOUNDED, GRB.INF_OR_UNBD]:
                print(f"Found solution for {self.numRounds} rounds!\n")
                break
            print(f"Didn't find any solution for {self.numRounds} rounds\n")
            self.numRounds += 1
            self.rounds = [round for round in range(1, self.numRounds+1)]

        self.printOutputs()

    def readInput(self):
        # self.crossingTimes = {1: 1, 2: 2, 3: 5, 4: 10}
        self.crossingTimes = {1: 1, 2: 2, 3: 5, 4: 8, 5: 10, 6: 12}
        self.numPeople = len(self.crossingTimes)
        self.people = [p+1 for p in range(self.numPeople)]
        self.bridgeSides = ['left', 'right']
        self.numRounds = 1
        self.rounds = [round for round in range(1, self.numRounds + 1)]

    def variables(self):

        self.timeRound = self.model.addVars(
            self.rounds
            , self.bridgeSides
            , lb=0
            , ub=max(self.crossingTimes.values())
            , vtype=GRB.INTEGER
            , name=f"time_round")

        self.ifPersonInRound = self.model.addVars(
            self.people
            , self.rounds
            , self.bridgeSides
            , vtype=GRB.BINARY
            , name=f"if_person_in_round")

        self.ifPersonOnSide = self.model.addVars(
            self.people
            , [0]+self.rounds
            , self.bridgeSides
            , vtype=GRB.BINARY
            , name=f"if_person_on_side")

    def constraints(self):
        """ CONSTRAINTS """
        """ All people are on left initially and on right after last round """
        self.model.addConstr(self.ifPersonOnSide.sum('*', 0, 'left') == self.numPeople, f"")
        self.model.addConstr(self.ifPersonOnSide.sum('*', self.rounds[-1], 'right') == self.numPeople, f"")

        """ A person can only be on one direction at a time """
        for person in self.people:
            for round in [0]+self.rounds:
                self.model.addConstr(self.ifPersonOnSide.sum(person, round, '*') == 1, f"")

        """ Maximum two people can cross at a time and minimum one person (because it is a minimisation problem) """
        for round, side in self.timeRound:
            self.model.addConstr(self.ifPersonInRound.sum('*', round, side) <= 2, f"")
            if round != self.rounds[-1]:
                self.model.addConstr(self.ifPersonInRound.sum('*', round, side) >= 1, f"")

        """ Time taken for round """
        for person, round, side in self.ifPersonInRound:
            self.model.addConstr(self.timeRound[round, side]
                                 >= self.ifPersonInRound[person, round, side]*self.crossingTimes[person]
                                 , f"")

        """ Side of person after each round """
        for person in self.people:
            for round in self.rounds:
                self.model.addConstr(self.ifPersonOnSide[person, round, 'left']
                                     == self.ifPersonOnSide[person, round-1, 'left']
                                     - self.ifPersonInRound[person, round, 'left']
                                     + self.ifPersonInRound[person, round, 'right']
                                     , f"")

                self.model.addConstr(self.ifPersonInRound[person, round, 'left'] <=
                                     self.ifPersonOnSide[person, round-1, 'left']
                                     , f"")

                self.model.addConstr(self.ifPersonInRound[person, round, 'right']
                                     <= self.ifPersonOnSide[person, round-1, 'right']
                                     + self.ifPersonInRound[person, round, 'left']
                                     , f"")

    def objectiveFunction(self):
        self.totalTime = self.timeRound.sum('*', '*')

    def setRunParams(self):

        self.model.setObjective(self.totalTime, GRB.MINIMIZE)
        self.model.setParam('TimeLimit', 30)
        # self.model.setParam('NoRelHeurTime', 200)
        self.model.setParam('MIPGap', 0)
        self.model.write('outputs/lp_file.lp')
        self.model.optimize()

    def printOutputs(self):
        print("Optimal Solution") if self.model.STATUS == GRB.OPTIMAL else print("Feasible Solution")
        print(f"Objective - {self.model.objVal} minutes")
        for v in self.model.getVars():
            if v.X > 0.5:
                print(f'{v.VarName} - {v.X}')

        print("\nSOLUTION -\n")
        for round in [0]+self.rounds:

            if round != 0:
                left_to_right_str = \
                    " ".join([f"{person} ({self.crossingTimes[person]}) "
                              for person in self.people if self.ifPersonInRound[person, round, 'left'].X > 0.1])
                print(f"Left to Right - {left_to_right_str} - {self.timeRound[round,'left'].X} minutes")

                if round != self.rounds[-1]:
                    right_to_left_str = \
                        " ".join([f"{person} ({self.crossingTimes[person]}) "
                              for person in self.people if self.ifPersonInRound[person, round, 'right'].X > 0.1])
                    print(f"Right to Left - {right_to_left_str} - {self.timeRound[round, 'right'].X} minutes")

            sol_str = \
                " ".join([f"{person} " for person in self.people if self.ifPersonOnSide[person, round, 'left'].X > 0.1]) \
                + "__________________________________" \
                + " ".join([f" {person}" for person in self.people if self.ifPersonOnSide[person, round, 'right'].X > 0.1])
            print(f"After Round {round} - {sol_str}")

Optimizer()