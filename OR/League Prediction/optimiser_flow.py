""" LEAGUE PREDICTION """

"""

A 20 team league where each team faces another twice (like PL / La Liga etc).
Take different cases which are possible as a result of the league.

"""

import gurobipy as gp
from gurobipy import GRB
import pandas as pd

class Optimiser():
    def __init__(self, cases, case):
        self.teams = [t for t in range(1, 21)]
        self.status = {'w': 3, 'd': 1, 'l': 0}
        self.status_rev = {'w': 0, 'd': 1, 'l': 3}
        self.cases = cases
        self.case = case

    def run_math_model(self):
        self.model = gp.Model("League")
        self.variables()
        self.constraints()
        self.objective()
        self.run_params()
        self.model.optimize()
        # self.print_output()
        self.prepare_output()

    def variables(self):
        self.match_result = self.model.addVars(
            ((t1, t2, s) for t1 in self.teams for t2 in self.teams if t1 != t2 for s in self.status.keys()),
            vtype=GRB.BINARY,
            name=f"match_result")

        self.points = self.model.addVars(
            self.teams,
            vtype=GRB.INTEGER,
            lb=0,
            # ub=38*3,
            name=f"points"
        )

        self.deviations = self.model.addVars(
            ((t1, t2) for t1 in self.teams for t2 in self.teams if t1 < t2),
            vtype=GRB.INTEGER,
            lb=0,
            name=f"deviations")

    def constraints(self):

        for t in self.teams:
            self.model.addConstr(self.points[t] ==
                                 gp.quicksum(self.match_result[t, opp, s]*self.status[s]
                                             for opp in self.teams if t != opp for s in self.status.keys()) +
                                 gp.quicksum(self.match_result[opp, t, s] * self.status_rev[s]
                                             for opp in self.teams if t != opp for s in self.status.keys())
                                 ,
                                 name=f"points_for_{t}")

        for t in self.teams:
            for opp in self.teams:
                if t != opp:
                    self.model.addConstr(
                        self.match_result.sum(t, opp, "*")
                        == 1,
                        name=f"match_result_{t}_{opp}")

        for t in self.teams[:-1]:
            self.model.addConstr(
                self.points[t] >= self.points[t+1],
                name=f"hierarchy_{t}_{t+1}")

        for t1, t2 in self.deviations:
            self.model.addConstr(self.deviations[t1, t2] >= self.points[t1] - self.points[t2], name=f"dev_1_{t1}_{t2}")
            self.model.addConstr(self.deviations[t1, t2] >= self.points[t2] - self.points[t1], name=f"dev_2_{t1}_{t2}")

    def objective(self):
        self.diff_t1st_t2nd = self.points[1] - self.points[2]
        self.diff_t1st_t4th = self.points[1] - self.points[4]
        self.diff_t1st_t20th = self.points[1] - self.points[20]
        self.total_deviations = self.deviations.sum("*", "*")

        if self.case == "1":
            self.model.setObjectiveN(self.diff_t1st_t2nd, index=1, priority=5, weight=-1, name=f"max_diff_t1st_t2nd")
            self.model.setObjectiveN(self.total_deviations, index=2, priority=2, weight=-1, name=f"total_deviations")

        if self.case == "2":
            self.model.addConstr(self.points[1] - self.points[2] >= 1, "")
            self.model.setObjectiveN(self.diff_t1st_t2nd, index=1, priority=5, weight=1, name=f"min_diff_t1st_t2nd")
            self.model.setObjectiveN(self.points[1], index=2, priority=4, weight=-1, name=f"max_points_t1")

        if self.case == "3":
            for t in [1, 2, 3]:
                self.model.addConstr(self.points[t] - self.points[t+1] >= 1, "")
            self.model.setObjectiveN(self.diff_t1st_t4th, index=1, priority=5, weight=1, name=f"min_diff_t1st_t4th")
            self.model.setObjectiveN(self.points[1], index=2, priority=4, weight=-1, name=f"max_points_t1")

        if self.case == "4":
            for t in range(1, 20):
                self.model.addConstr(self.points[t] - self.points[t+1] >= 1, "")
            self.model.setObjectiveN(self.diff_t1st_t20th, index=1, priority=5, weight=1, name=f"min_diff_t1st_t20th")
            self.model.setObjectiveN(self.points[1], index=2, priority=4, weight=-1, name=f"max_points_t1")

    def run_params(self):
        self.model.setParam("TimeLimit", 60)
        self.model.setParam("MipGap", 0.00)

    def print_output(self):
        for t in self.teams:
            print(t, self.points[t].X)

    def prepare_output(self):
        self.points_table_columns = ["TEAM", "PLAYED", "WON", "DRAW", "LOST", "POINTS"]
        self.points_table_lst = []
        for t in self.teams:
            win, loss, draw = 0, 0, 0
            for opp in self.teams:
                if t != opp:
                    win += (1 if self.match_result[t, opp, "w"].X == 1 else 0)
                    win += (1 if self.match_result[opp, t, "l"].X == 1 else 0)
                    loss += (1 if self.match_result[t, opp, "l"].X == 1 else 0)
                    loss += (1 if self.match_result[opp, t, "w"].X == 1 else 0)
                    draw += (1 if self.match_result[t, opp, "d"].X == 1 else 0)
                    draw += (1 if self.match_result[opp, t, "d"].X == 1 else 0)

            self.points_table_lst.append([t, 38, win, draw, loss, round(self.points[t].X)])

        self.points_table_df = pd.DataFrame(self.points_table_lst, columns=self.points_table_columns)
        print(self.points_table_df)
        self.points_table_df.to_csv(f"outputs/points_table_{self.cases[self.case]}.csv", index=False)

def main():
    cases = {"1": "maximum_difference_between_1st_and_2nd",
             "2": "minimum_difference_between_1st_and_2nd_with_maximum_possible_points",
             "3": "minimum_difference_between_1st_and_4th_with_maximum_possible_points",
             "4": "minimum_difference_between_1st_and_20th_with_maximum_possible_points"}

    while True:
        print()
        for key in cases:
            print(f"case number - {key} : case - {cases[key]}")
        case = input(f"\nEnter case number from given values, 0 to terminate -\n\n")

        if case == "0":
            print("Interrupt request received")
            break

        elif case not in cases.keys():
            print("Enter a valid case number")
            continue

        else:
            optim = Optimiser(cases, case)
            optim.run_math_model()

main()