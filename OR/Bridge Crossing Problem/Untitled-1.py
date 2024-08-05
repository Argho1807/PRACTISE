import math
import numpy as np
import pandas as pd
import time

from ortools.linear_solver import pywraplp

num_people = 4 # 1, 2, 3, 4
P = [f'P{p+1}' for p in range(num_people)]        

times = [1, 2, 5, 10]

for num_rounds in range(10):
    print('num_rounds -',num_rounds)
    ROUND = [f'round {r+1}' for r in range(num_rounds)] 
    ROUNDEX = [f'round {r+1}' for r in range(num_rounds+1)] 
    
    solver = pywraplp.Solver.CreateSolver('SCIP')

    ### DECISION VARIABLES ### 

    TL = {} # time for round r
    TR = {} # time for round r
    DL = {} # 1 if person p is in round r 
    DR = {} # 1 if person p is in round r 
    L = {} # 1 if person p is in left before round r - 0 to n
    R = {} # 1 if person p is in right before round r - 0 to n

    for r in range(num_rounds):
        TL[r] = solver.IntVar(0, max(times), 'T[r]')
        TR[r] = solver.IntVar(0, max(times), 'T[r]')
        for p in range(num_people):
            DL[r,p] = solver.IntVar(0, 1, 'D[r,p]')
            DR[r,p] = solver.IntVar(0, 1, 'D[r,p]')
    
    for r in range(num_rounds+1):
        for p in range(num_people):
            L[r,p] = solver.IntVar(0, 1, 'L[r,p]')
            R[r,p] = solver.IntVar(0, 1, 'R[r,p]')

    ### CONSTRAINTS ###

    for p in range(num_people):
        solver.Add(L[0,p] == 1)
        solver.Add(R[0,p] == 0)
        solver.Add(L[num_rounds,p] == 0)
        solver.Add(R[num_rounds,p] == 1)
    
    for r in range(num_rounds):
        for p in range(num_people):
            solver.Add(TL[r] >= DL[r,p]*times[p])
            solver.Add(TR[r] >= DR[r,p]*times[p])
   
    for r in range(num_rounds+1):
        for p in range(num_people):
            solver.Add(L[r,p] + R[r,p] == 1) # either one side
    
    for r in range(1,num_rounds,2):
        for p in range(num_people):
            solver.Add(DL[r,p] == 0) # either one side
    
    for r in range(0,num_rounds,2):
        for p in range(num_people):
            solver.Add(DR[r,p] == 0) # either one side
    
    for r in range(0,num_rounds,2): # max two people at a time
        solver.Add(solver.Sum(DL[r,p] for p in range(num_people)) <= 2)
        solver.Add(solver.Sum(DL[r,p] for p in range(num_people)) >= 1)    
    
    for r in range(1,num_rounds,2): # max two people at a time
        solver.Add(solver.Sum(DR[r,p] for p in range(num_people)) <= 2)
        solver.Add(solver.Sum(DR[r,p] for p in range(num_people)) >= 1)    

    for r in range(0,num_rounds,2):
        for p in range(num_people):
            solver.Add(L[r+1,p] == L[r,p] - DL[r,p])
            solver.Add(DL[r,p] <= L[r,p])
    
    for r in range(1,num_rounds,2):
        for p in range(num_people):
            solver.Add(R[r+1,p] == R[r,p] - DR[r,p])
            solver.Add(DR[r,p] <= R[r,p])

    ### OBJECTIVE ###
    objective_function = []
    for r in range(num_rounds):
        objective_function.append(TL[r])
        objective_function.append(TR[r])

    ### SOLVER ###
    solver.Minimize(solver.Sum(objective_function))
    status = solver.Solve()
    print('OPTIMAL =',status == pywraplp.Solver.OPTIMAL)

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
    
        L_val = [[round(L[r,p].solution_value(), 1) for r in range(num_rounds+1)] for p in range(num_people)]
        R_val = [[round(R[r,p].solution_value(), 1) for r in range(num_rounds+1)] for p in range(num_people)]
        XL_val = [[round(DL[r,p].solution_value(), 1) for r in range(num_rounds)] for p in range(num_people)]
        XR_val = [[round(DR[r,p].solution_value(), 1) for r in range(num_rounds)] for p in range(num_people)]
        TL_val = [round(TL[r].solution_value(), 1) for r in range(num_rounds)]
        TR_val = [round(TR[r].solution_value(), 1) for r in range(num_rounds)]

        L_df = pd.DataFrame(L_val, index = P, columns = ROUNDEX)
        R_df = pd.DataFrame(R_val, index = P, columns = ROUNDEX)
        XL_df = pd.DataFrame(XL_val, index = P, columns = ROUND)
        TL_df = pd.DataFrame(TL_val, index = ROUND, columns = ['TIMES'])
        XR_df = pd.DataFrame(XR_val, index = P, columns = ROUND)
        TR_df = pd.DataFrame(TR_val, index = ROUND, columns = ['TIMES'])
        # Z_df = pd.DataFrame(Z_val, index = P, columns = ROUND)
        
        print('\nL\n',L_df)
        print('\nR\n',R_df)
        print('\nDL\n',XL_df)
        print('\nDR\n',XR_df)
        print('\nTL\n',TL_df)
        print('\nTR\n',TR_df)
    
        break

    else:
        print('The problem does not have an optimal solution.')