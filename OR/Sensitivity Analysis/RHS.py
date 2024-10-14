### SENSITIVITY ANALYSIS ###
# Shadow prices
# Reduced costs
print('\nSENSITIVITY ANALYSIS\n')

import math
import numpy as np
import pandas as pd

from ortools.linear_solver import pywraplp

################################################################################### PRIMAL PROBLEM ###################################################################################

print('PRIMAL PROBLEM -\n')

"""
Max Z = 550*x1 + 600*x2 + 350*x3 + 400*x4 + 200*x5
such that,
12*x1 + 20*x2 + 25*x4 + 15*x5 <= 288 - grinding
10*x1 + 8*x2 + 16*x3 <= 192 - drilling
20*x1 + 20*x2 + 20*x3 + 20*x4 + 20*x5 <= 384 - manpowering
"""

############################################### SETS AND INDICES ###############################################

num_products = 5
num_processes = 3

I = [f'Product {i+1}' for i in range(num_products)]
P = ['Grinding', 'Drilling', 'Manpowering']

############################################### PARAMETERS ###############################################

Profits = [550, 600, 350, 400, 200]

Durations = [[12, 20, 0, 25, 15],
             [10, 8, 16, 0, 0],
             [20, 20, 20, 20, 20]]

Capacity = [288, 192, 384]

############################################### FORMULATION ###############################################

solver_primal = pywraplp.Solver.CreateSolver('SCIP')

############################################### DECISION VARIABLES ############################################### 

x = {}
for i in range(num_products):
    x[i] = solver_primal.NumVar(0, math.inf, 'x[i]')

############################################### CONSTRAINTS ###############################################

for p in range(num_processes):
    solver_primal.Add(solver_primal.Sum([Durations[p][i]*x[i] for i in range(num_products)]) <= Capacity[p])

############################################### OBJECTIVE ###############################################

z = [] 

for i in range(num_products):
    z.append(Profits[i]*x[i])

############################################### SOLVER ###############################################

solver_primal.Maximize(solver_primal.Sum(z))
status = solver_primal.Solve()

############################################### OUTPUT ###############################################

if status == pywraplp.Solver.OPTIMAL:

    Z = round(solver_primal.Objective().Value(),2)
    print('Profit =',Z,'POUNDS\n')    
    
    X = [round(x[i].solution_value(),2) for i in range(num_products)]
    print(pd.DataFrame(X, index = I, columns = ['Quantity']),'\n')

else:
    print('The problem does not have an optimal solution.')

################################################################################### DUAL PROBLEM ###################################################################################

print('DUAL PROBLEM -\n')

"""
Min W = 288*y1 + 192*y2 + 384*y3
such that,
12*y1 + 10*y2 + 20*y3 >= 550 - product 1
20*y1 + 8*y2 + 20*y3 >= 600 - product 2
16*y2 + 20*y3 >= 350 - product 3
25*y1 + 20*y3 >= 400 - product 4
15*y1 + 20*y3 >= 200 - product 5
"""

############################################### FORMULATION ###############################################

solver_dual = pywraplp.Solver.CreateSolver('SCIP')

############################################### DECISION VARIABLES ############################################### 

y = {}
for p in range(num_processes):
    y[p] = solver_dual.NumVar(0, math.inf, 'y[p]')

############################################### CONSTRAINTS ###############################################

for i in range(num_products):
    solver_dual.Add(solver_dual.Sum([Durations[p][i]*y[p] for p in range(num_processes)]) >= Profits[i])

############################################### OBJECTIVE ###############################################

w = []

for p in range(num_processes):
    w.append(Capacity[p]*y[p])

############################################### SOLVER ###############################################

solver_dual.Minimize(solver_dual.Sum(w))
status = solver_dual.Solve()

############################################### OUTPUT ###############################################

if status == pywraplp.Solver.OPTIMAL:

    W = round(solver_dual.Objective().Value(),2)
    print('Profit =',W,'POUNDS\n')    
    
    Y = [round(y[p].solution_value(),2) for p in range(num_processes)]
    print(pd.DataFrame(Y, index = P, columns = ['Value']),'\n')

else:
    print('The problem does not have an optimal solution.')


print('Sensitivity Analysis -')    

print('\nSlacks -')
Slacks = []
for p in range(num_processes):
    S = Capacity[p] - sum(X[i]*Durations[p][i] for i in range(num_products))
    Slacks.append(round(S,2))
    if round(Slacks[p]) != 0:
        print(f'{P[p]} has {round(Slacks[p],2)} hours unutilised')

print('\nShadow Prices -')
Shadow_prices = Y
for p in range(num_processes):
    if Shadow_prices[p] != 0:
        print(f'Increasing {P[p]} time by 1 hour increases profit by {round(Shadow_prices[p],2)} pounds')

print('\n',pd.DataFrame([Slacks, Shadow_prices], index = ['Slacks', 'Shadow Price'], columns = P),'\n')

print('\nReduced Costs -')
Reduced_costs = []
for i in range(num_products):
    R = sum(Y[p]*Durations[p][i] for p in range(num_processes)) - Profits[i]
    Reduced_costs.append(round(R,2))
    if Reduced_costs[i] == -0.00:
        Reduced_costs[i] = round(Reduced_costs[i])
        
    if Reduced_costs[i] != 0:
        print(f'{I[i]} is not produced as it has a reduced cost of {Reduced_costs[i]} pounds - producing one unit of {I[i]} will decrease profit by {Reduced_costs[i]} pounds')
    
print('\n',pd.DataFrame(Reduced_costs, index = I, columns = ['Reduced Cost']),'\n')