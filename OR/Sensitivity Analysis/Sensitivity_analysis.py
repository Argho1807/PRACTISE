""" SENSITIVITY ANALYSIS """

"""

SLACKS
SHADOW PRICES
REDUCED COSTS

"""

import math
import pandas as pd
import copy
from ortools.linear_solver import pywraplp

class Optimizer():

    def __init__(self):
        self.num_products = 5
        self.num_processes = 3
        self.Products = [f'Product {prod + 1}' for prod in range(self.num_products)]
        self.Processes = ['Grinding', 'Drilling', 'Man Powering']

        self.Profits = [550, 600, 350, 400, 200]

        self.Durations = [[12, 20, 0, 25, 15],
                          [10, 8, 16, 0, 0],
                          [20, 20, 20, 20, 20]]

        self.Capacity = [288, 192, 384]

    def solve(self):
        self.solvePrimalProblem()
        self.solveDualProblem()
        self.sensitivityAnalysis()
    
    def solvePrimalProblem(self):
        print("\nPRIMAL PROBLEM")
        
        """
        PRIMAL PROBLEM
        Max Z = 550*x1 + 600*x2 + 350*x3 + 400*x4 + 200*x5
        such that,
        12*x1 + 20*x2 + 25*x4 + 15*x5 <= 288 - grinding
        10*x1 + 8*x2 + 16*x3 <= 192 - drilling
        20*x1 + 20*x2 + 20*x3 + 20*x4 + 20*x5 <= 384 - man powering
        """

        solver_primal = pywraplp.Solver.CreateSolver('SCIP')
        x = {i: solver_primal.NumVar(0, math.inf, f'x_{i}') for i in range(self.num_products)}

        for p in range(self.num_processes):
            solver_primal.Add(solver_primal.Sum([self.Durations[p][i] * x[i] for i in range(self.num_products)]) <= self.Capacity[p])

        z = [self.Profits[i] * x[i] for i in range(self.num_products)]
        solver_primal.Maximize(solver_primal.Sum(z))
        status = solver_primal.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            self.Z = round(solver_primal.Objective().Value(), 2)
            print('Profit =', self.Z, 'POUNDS\n')
            self.X = [round(x[i].solution_value(), 2) for i in range(self.num_products)]
            print(pd.DataFrame(self.X, index=self.Products, columns=['Quantity']))
        else:
            print('The problem does not have an optimal solution.')

    def solveDualProblem(self):
        print("\nDUAL PROBLEM")
        
        """ 
        DUAL PROBLEM 
        Min W = 288*y1 + 192*y2 + 384*y3
        such that,
        12*y1 + 10*y2 + 20*y3 >= 550 - product 1
        20*y1 + 8*y2 + 20*y3 >= 600 - product 2
        16*y2 + 20*y3 >= 350 - product 3
        25*y1 + 20*y3 >= 400 - product 4
        15*y1 + 20*y3 >= 200 - product 5
        """

        self.solver_dual = pywraplp.Solver.CreateSolver('SCIP')
        y = {p: self.solver_dual.NumVar(0, math.inf, f'y_{p}') for p in range(self.num_processes)}

        for i in range(self.num_products):
            self.solver_dual.Add(
                self.solver_dual.Sum([self.Durations[p][i] * y[p] for p in range(self.num_processes)]) >= self.Profits[i])

        w = [self.Capacity[p] * y[p] for p in range(self.num_processes)]
        self.solver_dual.Minimize(self.solver_dual.Sum(w))
        status = self.solver_dual.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            self.W = round(self.solver_dual.Objective().Value(), 2)
            print('Profit =', self.W, 'POUNDS\n')
            self.Y = [round(y[p].solution_value(), 2) for p in range(self.num_processes)]
            print(pd.DataFrame(self.Y, index=self.Processes, columns=['Value']))
        else:
            print('The problem does not have an optimal solution.')
    
    def sensitivityAnalysis(self):
        print('\nSENSITIVITY ANALYSIS')
        self.calcSlacks()
        self.calcShadowPrices()
        print('\n', pd.DataFrame([self.Slacks, self.Shadow_prices], index=['Slack', 'Shadow Price'], columns=self.Processes))
        self.calcReducedCosts()
        self.testShadowPrices()
        self.testReducedCosts()
    
    def calcSlacks(self):
        print('\nSLACKS -\n')
        # SLACK = (RHS - LHS) for each constraint of primal problem
        self.Slacks = [round(
            self.Capacity[process] - sum(self.X[i] * self.Durations[process][i] for i in range(self.num_products)), 2)
                  for process in range(self.num_processes)]

        for process in range(len(self.Slacks)):
            if self.Slacks[process] != 0:
                print(f'{self.Processes[process]} has {round(self.Slacks[process],2)} hours unutilised')

    def calcShadowPrices(self):
        print('\nSHADOW PRICES -\n')
        # SHADOW PRICE - Increase in objective by unit increase in RHS of primal problem (for maximisation problem)
        # decision variable values of dual problem are the shadow prices of primal problem
        self.Shadow_prices = copy.deepcopy(self.Y)

        for process in range(self.num_processes):
            if self.Shadow_prices[process] != 0:
                print(f'Increasing {self.Processes[process]} time by 1 hour increases profit by {round(self.Shadow_prices[process],2)} pounds')

    def calcReducedCosts(self):
        print('\nREDUCED COSTS -\n')
        # REDUCED COST is zero for variables already in basis
        # for variables not in basis -
        # increasing a variable by one unit will reduce objective by REDUCED COST of that variable (for maximisation problem)
        # surplus of constraints of dual problem are the reduced costs
        self.Reduced_costs = [
            round(sum(self.Y[p] * self.Durations[p][i] for p in range(self.num_processes)) - self.Profits[i], 2)
            for i in range(self.num_products)]

        for i in range(self.num_products):
            if self.Reduced_costs[i] == -0.00:
                self.Reduced_costs[i] = round(self.Reduced_costs[i])
            if self.Reduced_costs[i] != 0:
                print(f'{self.Products[i]} is not produced as it has a reduced cost of {self.Reduced_costs[i]} pounds - producing one unit of {self.Products[i]} will decrease profit by {self.Reduced_costs[i]} pounds')

        print('\n', pd.DataFrame(self.Reduced_costs, index=self.Products, columns=['Reduced Cost']))
    
    def testShadowPrices(self):
        print("\nSHADOW PRICES TEST - increase grinding duration capacity by 1 hour")

        self.capacity_temp = copy.deepcopy(self.Capacity)
        self.capacity_temp[0] += 1
        solver_shadow_price = pywraplp.Solver.CreateSolver('SCIP')
        x = {i: solver_shadow_price.NumVar(0, math.inf, f'x_{i}') for i in range(self.num_products)}

        for p in range(self.num_processes):
            solver_shadow_price.Add(solver_shadow_price.Sum([self.Durations[p][i] * x[i] for i in range(self.num_products)]) <= self.capacity_temp[p])

        z_shadow_price_test = [self.Profits[i] * x[i] for i in range(self.num_products)]
        solver_shadow_price.Maximize(solver_shadow_price.Sum(z_shadow_price_test))
        status = solver_shadow_price.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            self.Z_shadow_price_test = round(solver_shadow_price.Objective().Value(), 2)
            print('Profit =', self.Z_shadow_price_test, 'POUNDS\n')
            X = [x[i].solution_value() for i in range(self.num_products)]
            print(pd.DataFrame(X, index=self.Products, columns=['Quantity']), '\n')

            # check if shadow price condition is verified
            if round(self.Z_shadow_price_test - self.Z, 2) == round(self.Shadow_prices[0], 2):
                print(f'Shadow price condition verified -')
                print(f'Objective increases by {round(self.Shadow_prices[0], 2)} pounds on increasing {self.Processes[0]} duration capacity by 1 hour')
            else:
                print('Shadow price condition not verified')

        else:
            print('The problem does not have an optimal solution.')
    
    def testReducedCosts(self):
        print("\nREDUCED COSTS TEST - force product 3 to 1 unit")
        
        solver_reduced_cost = pywraplp.Solver.CreateSolver('SCIP')
        x = {i: solver_reduced_cost.NumVar(0, math.inf, f'x_{i}') for i in range(self.num_products)}

        for p in range(self.num_processes):
            solver_reduced_cost.Add(solver_reduced_cost.Sum([self.Durations[p][i] * x[i] for i in range(self.num_products)]) <=self.Capacity[p])

        solver_reduced_cost.Add(x[2] == 1)
        # forcing 1 unit of product 3 to be produced (previously none were produced)

        z_reduced_cost_test = [self.Profits[i] * x[i] for i in range(self.num_products)]
        solver_reduced_cost.Maximize(solver_reduced_cost.Sum(z_reduced_cost_test))
        status = solver_reduced_cost.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            Z_reduced_cost_test = round(solver_reduced_cost.Objective().Value(), 2)
            print('Profit =', Z_reduced_cost_test, 'POUNDS\n')
            X = [x[i].solution_value() for i in range(self.num_products)]
            print(pd.DataFrame(X, index=self.Products, columns=['Quantity']), '\n')

            # check if reduced cost condition is verified
            if self.Z - Z_reduced_cost_test == self.Reduced_costs[2]:
                print(f'Reduced cost condition verified -')
                print(f'Objective decreases by {self.Reduced_costs[2]} pounds on producing one unit of {self.Products[2]}')
            else:
                print('Reduced cost condition not verified')

        else:
            print('The problem does not have an optimal solution.')

optim = Optimizer()
optim.solve()