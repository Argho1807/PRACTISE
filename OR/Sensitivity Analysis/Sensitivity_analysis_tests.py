### SENSITIVITY ANALYSIS - TESTS ###
# Shadow prices
# Reduced costs
print('\nSENSITIVITY ANALYSIS - TESTS\n')

import math
import numpy as np
import pandas as pd

from ortools.linear_solver import pywraplp

################################################################################### PRIMAL PROBLEM ###################################################################################

"""
Max Z = 550*x1 + 600*x2 + 350*x3 + 400*x4 + 200*x5
such that,
12*x1 + 20*x2 + 25*x4 + 15*x5 <= 288 - grinding
10*x1 + 8*x2 + 16*x3 <= 192 - drilling
20*x1 + 20*x2 + 20*x3 + 20*x4 + 20*x5 <= 384 - manpowering
"""

num_products = 5
num_processes = 3
I = [f'Product {i+1}' for i in range(num_products)]
P = ['Grinding', 'Drilling', 'Manpowering']

Profits = [550, 600, 350, 400, 200]

Durations = [[12, 20, 0, 25, 15],
             [10, 8, 16, 0, 0],
             [20, 20, 20, 20, 20]]

Capacity = [288, 192, 384]

solver_primal = pywraplp.Solver.CreateSolver('SCIP')

x = {}
for i in range(num_products):
    x[i] = solver_primal.NumVar(0, math.inf, 'x[i]')

for p in range(num_processes):
    solver_primal.Add(solver_primal.Sum([Durations[p][i]*x[i] for i in range(num_products)]) <= Capacity[p])

z = [] 
for i in range(num_products):
    z.append(Profits[i]*x[i])

solver_primal.Maximize(solver_primal.Sum(z))
status = solver_primal.Solve()

if status == pywraplp.Solver.OPTIMAL:

    Z = round(solver_primal.Objective().Value(),2)
    print('Profit =',Z,'POUNDS\n')    
    
    X = [x[i].solution_value() for i in range(num_products)]
    print(pd.DataFrame(X, index = I, columns = ['Quantity']),'\n')

else:
    print('The problem does not have an optimal solution.')

################################################################################### DUAL PROBLEM ###################################################################################

"""
Min W = 288*y1 + 192*y2 + 384*y3
such that,
12*y1 + 10*y2 + 20*y3 >= 550 - product 1
20*y1 + 8*y2 + 20*y3 >= 600 - product 2
16*y2 + 20*y3 >= 350 - product 3
25*y1 + 20*y3 >= 400 - product 4
15*y1 + 20*y3 >= 200 - product 5
"""

solver_dual = pywraplp.Solver.CreateSolver('SCIP')

y = {}
for p in range(num_processes):
    y[p] = solver_dual.NumVar(0, math.inf, 'y[p]')


for i in range(num_products):
    solver_dual.Add(solver_dual.Sum([Durations[p][i]*y[p] for p in range(num_processes)]) >= Profits[i])

w = []
for p in range(num_processes):
    w.append(Capacity[p]*y[p])

solver_dual.Minimize(solver_dual.Sum(w))
status = solver_dual.Solve()

if status == pywraplp.Solver.OPTIMAL:

    W = round(solver_dual.Objective().Value(),2)
    #print('Profit =',W,'POUNDS\n')    
    
    Y = [y[p].solution_value() for p in range(num_processes)]
    #print(pd.DataFrame(Y, index = P, columns = ['Value']),'\n')

else:
    print('The problem does not have an optimal solution.')

Slacks = []
for p in range(num_processes):
    Slacks.append(Capacity[p] - sum(X[i]*Durations[p][i] for i in range(num_products)))

Shadow_prices = Y

Reduced_costs = []
for i in range(num_products):
    R = sum(Y[p]*Durations[p][i] for p in range(num_processes)) - Profits[i]
    Reduced_costs.append(round(R,2))
    if Reduced_costs[i] == -0.00:
        Reduced_costs[i] = round(Reduced_costs[i])
        
# CHECKING SENSITIVITY ANALYSIS - TESTS

# SHADOW PRICES - increase grinding duration capacity by 1 hour

Capacity[0] += 1

solver = pywraplp.Solver.CreateSolver('SCIP')

x = {}
for i in range(num_products):
    x[i] = solver.NumVar(0, math.inf, 'x[i]')

for p in range(num_processes):
    solver.Add(solver.Sum([Durations[p][i]*x[i] for i in range(num_products)]) <= Capacity[p])

z_s = [] 
for i in range(num_products):
    z_s.append(Profits[i]*x[i])

solver.Maximize(solver.Sum(z_s))
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print(f'\nReduced costs test - produce 1 unit of {I[2]}\n')
    Z_s = round(solver.Objective().Value(),2)
    print('Profit =',Z_s,'POUNDS\n')    
    
    X = [x[i].solution_value() for i in range(num_products)]
    print(pd.DataFrame(X, index = I, columns = ['Quantity']),'\n')

    # check if shadow price condition is verified
    if round(Z_s - Z,2) == round(Shadow_prices[0],2):
        print(f'Shadow price condition verified - objective increases by {round(Shadow_prices[0],2)} pounds on increasing duration capacity of {P[0]} by 1 hour\n')
    else:
        print('Shadow price condition not verified\n')

else:
    print('The problem does not have an optimal solution.')

# REDUCED COSTS - force product 3 to 1 unit

solver_primal.Add(x[2] == 1)  # forcing 1 unit of product 3 to be produced (previously none were produced)

z_r = []
for i in range(num_products):
    z_r.append(Profits[i]*x[i])

solver_primal.Maximize(solver_primal.Sum(z_r))
status = solver_primal.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print(f'\nReduced costs test - produce 1 unit of {I[2]}\n')
    Z_r = round(solver_primal.Objective().Value(),2)
    print('Profit =',Z_r,'POUNDS\n')

    X = [x[i].solution_value() for i in range(num_products)]
    print(pd.DataFrame(X, index = I, columns = ['Quantity']),'\n')

    # check if reduced cost condition is verified
    if Z - Z_r == Reduced_costs[2]:
        print(f'Reduced cost condition verified - objective decreases by {Reduced_costs[2]} pounds on producing one unit of {I[2]}\n')
    else:
        print('Reduced cost condition not verified\n')

else:
    print('The problem does not have an optimal solution.')