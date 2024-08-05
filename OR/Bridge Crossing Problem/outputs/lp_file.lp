\ Model BridgeCrossing
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  time_round[1,left] + time_round[1,right] + time_round[2,left]
   + time_round[2,right] + time_round[3,left] + time_round[3,right]
   + time_round[4,left] + time_round[4,right] + time_round[5,left]
   + time_round[5,right]
Subject To
 R0: if_person_on_side[1,0,left] + if_person_on_side[2,0,left]
   + if_person_on_side[3,0,left] + if_person_on_side[4,0,left]
   + if_person_on_side[5,0,left] + if_person_on_side[6,0,left] = 6
 R1: if_person_on_side[1,5,right] + if_person_on_side[2,5,right]
   + if_person_on_side[3,5,right] + if_person_on_side[4,5,right]
   + if_person_on_side[5,5,right] + if_person_on_side[6,5,right] = 6
 R2: if_person_on_side[1,0,left] + if_person_on_side[1,0,right] = 1
 R3: if_person_on_side[1,1,left] + if_person_on_side[1,1,right] = 1
 R4: if_person_on_side[1,2,left] + if_person_on_side[1,2,right] = 1
 R5: if_person_on_side[1,3,left] + if_person_on_side[1,3,right] = 1
 R6: if_person_on_side[1,4,left] + if_person_on_side[1,4,right] = 1
 R7: if_person_on_side[1,5,left] + if_person_on_side[1,5,right] = 1
 R8: if_person_on_side[2,0,left] + if_person_on_side[2,0,right] = 1
 R9: if_person_on_side[2,1,left] + if_person_on_side[2,1,right] = 1
 R10: if_person_on_side[2,2,left] + if_person_on_side[2,2,right] = 1
 R11: if_person_on_side[2,3,left] + if_person_on_side[2,3,right] = 1
 R12: if_person_on_side[2,4,left] + if_person_on_side[2,4,right] = 1
 R13: if_person_on_side[2,5,left] + if_person_on_side[2,5,right] = 1
 R14: if_person_on_side[3,0,left] + if_person_on_side[3,0,right] = 1
 R15: if_person_on_side[3,1,left] + if_person_on_side[3,1,right] = 1
 R16: if_person_on_side[3,2,left] + if_person_on_side[3,2,right] = 1
 R17: if_person_on_side[3,3,left] + if_person_on_side[3,3,right] = 1
 R18: if_person_on_side[3,4,left] + if_person_on_side[3,4,right] = 1
 R19: if_person_on_side[3,5,left] + if_person_on_side[3,5,right] = 1
 R20: if_person_on_side[4,0,left] + if_person_on_side[4,0,right] = 1
 R21: if_person_on_side[4,1,left] + if_person_on_side[4,1,right] = 1
 R22: if_person_on_side[4,2,left] + if_person_on_side[4,2,right] = 1
 R23: if_person_on_side[4,3,left] + if_person_on_side[4,3,right] = 1
 R24: if_person_on_side[4,4,left] + if_person_on_side[4,4,right] = 1
 R25: if_person_on_side[4,5,left] + if_person_on_side[4,5,right] = 1
 R26: if_person_on_side[5,0,left] + if_person_on_side[5,0,right] = 1
 R27: if_person_on_side[5,1,left] + if_person_on_side[5,1,right] = 1
 R28: if_person_on_side[5,2,left] + if_person_on_side[5,2,right] = 1
 R29: if_person_on_side[5,3,left] + if_person_on_side[5,3,right] = 1
 R30: if_person_on_side[5,4,left] + if_person_on_side[5,4,right] = 1
 R31: if_person_on_side[5,5,left] + if_person_on_side[5,5,right] = 1
 R32: if_person_on_side[6,0,left] + if_person_on_side[6,0,right] = 1
 R33: if_person_on_side[6,1,left] + if_person_on_side[6,1,right] = 1
 R34: if_person_on_side[6,2,left] + if_person_on_side[6,2,right] = 1
 R35: if_person_on_side[6,3,left] + if_person_on_side[6,3,right] = 1
 R36: if_person_on_side[6,4,left] + if_person_on_side[6,4,right] = 1
 R37: if_person_on_side[6,5,left] + if_person_on_side[6,5,right] = 1
 R38: if_person_in_round[1,1,left] + if_person_in_round[2,1,left]
   + if_person_in_round[3,1,left] + if_person_in_round[4,1,left]
   + if_person_in_round[5,1,left] + if_person_in_round[6,1,left] <= 2
 R39: if_person_in_round[1,1,left] + if_person_in_round[2,1,left]
   + if_person_in_round[3,1,left] + if_person_in_round[4,1,left]
   + if_person_in_round[5,1,left] + if_person_in_round[6,1,left] >= 1
 R40: if_person_in_round[1,1,right] + if_person_in_round[2,1,right]
   + if_person_in_round[3,1,right] + if_person_in_round[4,1,right]
   + if_person_in_round[5,1,right] + if_person_in_round[6,1,right] <= 2
 R41: if_person_in_round[1,1,right] + if_person_in_round[2,1,right]
   + if_person_in_round[3,1,right] + if_person_in_round[4,1,right]
   + if_person_in_round[5,1,right] + if_person_in_round[6,1,right] >= 1
 R42: if_person_in_round[1,2,left] + if_person_in_round[2,2,left]
   + if_person_in_round[3,2,left] + if_person_in_round[4,2,left]
   + if_person_in_round[5,2,left] + if_person_in_round[6,2,left] <= 2
 R43: if_person_in_round[1,2,left] + if_person_in_round[2,2,left]
   + if_person_in_round[3,2,left] + if_person_in_round[4,2,left]
   + if_person_in_round[5,2,left] + if_person_in_round[6,2,left] >= 1
 R44: if_person_in_round[1,2,right] + if_person_in_round[2,2,right]
   + if_person_in_round[3,2,right] + if_person_in_round[4,2,right]
   + if_person_in_round[5,2,right] + if_person_in_round[6,2,right] <= 2
 R45: if_person_in_round[1,2,right] + if_person_in_round[2,2,right]
   + if_person_in_round[3,2,right] + if_person_in_round[4,2,right]
   + if_person_in_round[5,2,right] + if_person_in_round[6,2,right] >= 1
 R46: if_person_in_round[1,3,left] + if_person_in_round[2,3,left]
   + if_person_in_round[3,3,left] + if_person_in_round[4,3,left]
   + if_person_in_round[5,3,left] + if_person_in_round[6,3,left] <= 2
 R47: if_person_in_round[1,3,left] + if_person_in_round[2,3,left]
   + if_person_in_round[3,3,left] + if_person_in_round[4,3,left]
   + if_person_in_round[5,3,left] + if_person_in_round[6,3,left] >= 1
 R48: if_person_in_round[1,3,right] + if_person_in_round[2,3,right]
   + if_person_in_round[3,3,right] + if_person_in_round[4,3,right]
   + if_person_in_round[5,3,right] + if_person_in_round[6,3,right] <= 2
 R49: if_person_in_round[1,3,right] + if_person_in_round[2,3,right]
   + if_person_in_round[3,3,right] + if_person_in_round[4,3,right]
   + if_person_in_round[5,3,right] + if_person_in_round[6,3,right] >= 1
 R50: if_person_in_round[1,4,left] + if_person_in_round[2,4,left]
   + if_person_in_round[3,4,left] + if_person_in_round[4,4,left]
   + if_person_in_round[5,4,left] + if_person_in_round[6,4,left] <= 2
 R51: if_person_in_round[1,4,left] + if_person_in_round[2,4,left]
   + if_person_in_round[3,4,left] + if_person_in_round[4,4,left]
   + if_person_in_round[5,4,left] + if_person_in_round[6,4,left] >= 1
 R52: if_person_in_round[1,4,right] + if_person_in_round[2,4,right]
   + if_person_in_round[3,4,right] + if_person_in_round[4,4,right]
   + if_person_in_round[5,4,right] + if_person_in_round[6,4,right] <= 2
 R53: if_person_in_round[1,4,right] + if_person_in_round[2,4,right]
   + if_person_in_round[3,4,right] + if_person_in_round[4,4,right]
   + if_person_in_round[5,4,right] + if_person_in_round[6,4,right] >= 1
 R54: if_person_in_round[1,5,left] + if_person_in_round[2,5,left]
   + if_person_in_round[3,5,left] + if_person_in_round[4,5,left]
   + if_person_in_round[5,5,left] + if_person_in_round[6,5,left] <= 2
 R55: if_person_in_round[1,5,right] + if_person_in_round[2,5,right]
   + if_person_in_round[3,5,right] + if_person_in_round[4,5,right]
   + if_person_in_round[5,5,right] + if_person_in_round[6,5,right] <= 2
 R56: time_round[1,left] - if_person_in_round[1,1,left] >= 0
 R57: time_round[1,right] - if_person_in_round[1,1,right] >= 0
 R58: time_round[2,left] - if_person_in_round[1,2,left] >= 0
 R59: time_round[2,right] - if_person_in_round[1,2,right] >= 0
 R60: time_round[3,left] - if_person_in_round[1,3,left] >= 0
 R61: time_round[3,right] - if_person_in_round[1,3,right] >= 0
 R62: time_round[4,left] - if_person_in_round[1,4,left] >= 0
 R63: time_round[4,right] - if_person_in_round[1,4,right] >= 0
 R64: time_round[5,left] - if_person_in_round[1,5,left] >= 0
 R65: time_round[5,right] - if_person_in_round[1,5,right] >= 0
 R66: time_round[1,left] - 2 if_person_in_round[2,1,left] >= 0
 R67: time_round[1,right] - 2 if_person_in_round[2,1,right] >= 0
 R68: time_round[2,left] - 2 if_person_in_round[2,2,left] >= 0
 R69: time_round[2,right] - 2 if_person_in_round[2,2,right] >= 0
 R70: time_round[3,left] - 2 if_person_in_round[2,3,left] >= 0
 R71: time_round[3,right] - 2 if_person_in_round[2,3,right] >= 0
 R72: time_round[4,left] - 2 if_person_in_round[2,4,left] >= 0
 R73: time_round[4,right] - 2 if_person_in_round[2,4,right] >= 0
 R74: time_round[5,left] - 2 if_person_in_round[2,5,left] >= 0
 R75: time_round[5,right] - 2 if_person_in_round[2,5,right] >= 0
 R76: time_round[1,left] - 5 if_person_in_round[3,1,left] >= 0
 R77: time_round[1,right] - 5 if_person_in_round[3,1,right] >= 0
 R78: time_round[2,left] - 5 if_person_in_round[3,2,left] >= 0
 R79: time_round[2,right] - 5 if_person_in_round[3,2,right] >= 0
 R80: time_round[3,left] - 5 if_person_in_round[3,3,left] >= 0
 R81: time_round[3,right] - 5 if_person_in_round[3,3,right] >= 0
 R82: time_round[4,left] - 5 if_person_in_round[3,4,left] >= 0
 R83: time_round[4,right] - 5 if_person_in_round[3,4,right] >= 0
 R84: time_round[5,left] - 5 if_person_in_round[3,5,left] >= 0
 R85: time_round[5,right] - 5 if_person_in_round[3,5,right] >= 0
 R86: time_round[1,left] - 8 if_person_in_round[4,1,left] >= 0
 R87: time_round[1,right] - 8 if_person_in_round[4,1,right] >= 0
 R88: time_round[2,left] - 8 if_person_in_round[4,2,left] >= 0
 R89: time_round[2,right] - 8 if_person_in_round[4,2,right] >= 0
 R90: time_round[3,left] - 8 if_person_in_round[4,3,left] >= 0
 R91: time_round[3,right] - 8 if_person_in_round[4,3,right] >= 0
 R92: time_round[4,left] - 8 if_person_in_round[4,4,left] >= 0
 R93: time_round[4,right] - 8 if_person_in_round[4,4,right] >= 0
 R94: time_round[5,left] - 8 if_person_in_round[4,5,left] >= 0
 R95: time_round[5,right] - 8 if_person_in_round[4,5,right] >= 0
 R96: time_round[1,left] - 10 if_person_in_round[5,1,left] >= 0
 R97: time_round[1,right] - 10 if_person_in_round[5,1,right] >= 0
 R98: time_round[2,left] - 10 if_person_in_round[5,2,left] >= 0
 R99: time_round[2,right] - 10 if_person_in_round[5,2,right] >= 0
 R100: time_round[3,left] - 10 if_person_in_round[5,3,left] >= 0
 R101: time_round[3,right] - 10 if_person_in_round[5,3,right] >= 0
 R102: time_round[4,left] - 10 if_person_in_round[5,4,left] >= 0
 R103: time_round[4,right] - 10 if_person_in_round[5,4,right] >= 0
 R104: time_round[5,left] - 10 if_person_in_round[5,5,left] >= 0
 R105: time_round[5,right] - 10 if_person_in_round[5,5,right] >= 0
 R106: time_round[1,left] - 12 if_person_in_round[6,1,left] >= 0
 R107: time_round[1,right] - 12 if_person_in_round[6,1,right] >= 0
 R108: time_round[2,left] - 12 if_person_in_round[6,2,left] >= 0
 R109: time_round[2,right] - 12 if_person_in_round[6,2,right] >= 0
 R110: time_round[3,left] - 12 if_person_in_round[6,3,left] >= 0
 R111: time_round[3,right] - 12 if_person_in_round[6,3,right] >= 0
 R112: time_round[4,left] - 12 if_person_in_round[6,4,left] >= 0
 R113: time_round[4,right] - 12 if_person_in_round[6,4,right] >= 0
 R114: time_round[5,left] - 12 if_person_in_round[6,5,left] >= 0
 R115: time_round[5,right] - 12 if_person_in_round[6,5,right] >= 0
 R116: if_person_in_round[1,1,left] - if_person_in_round[1,1,right]
   - if_person_on_side[1,0,left] + if_person_on_side[1,1,left] = 0
 R117: if_person_in_round[1,1,left] - if_person_on_side[1,0,left] <= 0
 R118: - if_person_in_round[1,1,left] + if_person_in_round[1,1,right]
   - if_person_on_side[1,0,right] <= 0
 R119: if_person_in_round[1,2,left] - if_person_in_round[1,2,right]
   - if_person_on_side[1,1,left] + if_person_on_side[1,2,left] = 0
 R120: if_person_in_round[1,2,left] - if_person_on_side[1,1,left] <= 0
 R121: - if_person_in_round[1,2,left] + if_person_in_round[1,2,right]
   - if_person_on_side[1,1,right] <= 0
 R122: if_person_in_round[1,3,left] - if_person_in_round[1,3,right]
   - if_person_on_side[1,2,left] + if_person_on_side[1,3,left] = 0
 R123: if_person_in_round[1,3,left] - if_person_on_side[1,2,left] <= 0
 R124: - if_person_in_round[1,3,left] + if_person_in_round[1,3,right]
   - if_person_on_side[1,2,right] <= 0
 R125: if_person_in_round[1,4,left] - if_person_in_round[1,4,right]
   - if_person_on_side[1,3,left] + if_person_on_side[1,4,left] = 0
 R126: if_person_in_round[1,4,left] - if_person_on_side[1,3,left] <= 0
 R127: - if_person_in_round[1,4,left] + if_person_in_round[1,4,right]
   - if_person_on_side[1,3,right] <= 0
 R128: if_person_in_round[1,5,left] - if_person_in_round[1,5,right]
   - if_person_on_side[1,4,left] + if_person_on_side[1,5,left] = 0
 R129: if_person_in_round[1,5,left] - if_person_on_side[1,4,left] <= 0
 R130: - if_person_in_round[1,5,left] + if_person_in_round[1,5,right]
   - if_person_on_side[1,4,right] <= 0
 R131: if_person_in_round[2,1,left] - if_person_in_round[2,1,right]
   - if_person_on_side[2,0,left] + if_person_on_side[2,1,left] = 0
 R132: if_person_in_round[2,1,left] - if_person_on_side[2,0,left] <= 0
 R133: - if_person_in_round[2,1,left] + if_person_in_round[2,1,right]
   - if_person_on_side[2,0,right] <= 0
 R134: if_person_in_round[2,2,left] - if_person_in_round[2,2,right]
   - if_person_on_side[2,1,left] + if_person_on_side[2,2,left] = 0
 R135: if_person_in_round[2,2,left] - if_person_on_side[2,1,left] <= 0
 R136: - if_person_in_round[2,2,left] + if_person_in_round[2,2,right]
   - if_person_on_side[2,1,right] <= 0
 R137: if_person_in_round[2,3,left] - if_person_in_round[2,3,right]
   - if_person_on_side[2,2,left] + if_person_on_side[2,3,left] = 0
 R138: if_person_in_round[2,3,left] - if_person_on_side[2,2,left] <= 0
 R139: - if_person_in_round[2,3,left] + if_person_in_round[2,3,right]
   - if_person_on_side[2,2,right] <= 0
 R140: if_person_in_round[2,4,left] - if_person_in_round[2,4,right]
   - if_person_on_side[2,3,left] + if_person_on_side[2,4,left] = 0
 R141: if_person_in_round[2,4,left] - if_person_on_side[2,3,left] <= 0
 R142: - if_person_in_round[2,4,left] + if_person_in_round[2,4,right]
   - if_person_on_side[2,3,right] <= 0
 R143: if_person_in_round[2,5,left] - if_person_in_round[2,5,right]
   - if_person_on_side[2,4,left] + if_person_on_side[2,5,left] = 0
 R144: if_person_in_round[2,5,left] - if_person_on_side[2,4,left] <= 0
 R145: - if_person_in_round[2,5,left] + if_person_in_round[2,5,right]
   - if_person_on_side[2,4,right] <= 0
 R146: if_person_in_round[3,1,left] - if_person_in_round[3,1,right]
   - if_person_on_side[3,0,left] + if_person_on_side[3,1,left] = 0
 R147: if_person_in_round[3,1,left] - if_person_on_side[3,0,left] <= 0
 R148: - if_person_in_round[3,1,left] + if_person_in_round[3,1,right]
   - if_person_on_side[3,0,right] <= 0
 R149: if_person_in_round[3,2,left] - if_person_in_round[3,2,right]
   - if_person_on_side[3,1,left] + if_person_on_side[3,2,left] = 0
 R150: if_person_in_round[3,2,left] - if_person_on_side[3,1,left] <= 0
 R151: - if_person_in_round[3,2,left] + if_person_in_round[3,2,right]
   - if_person_on_side[3,1,right] <= 0
 R152: if_person_in_round[3,3,left] - if_person_in_round[3,3,right]
   - if_person_on_side[3,2,left] + if_person_on_side[3,3,left] = 0
 R153: if_person_in_round[3,3,left] - if_person_on_side[3,2,left] <= 0
 R154: - if_person_in_round[3,3,left] + if_person_in_round[3,3,right]
   - if_person_on_side[3,2,right] <= 0
 R155: if_person_in_round[3,4,left] - if_person_in_round[3,4,right]
   - if_person_on_side[3,3,left] + if_person_on_side[3,4,left] = 0
 R156: if_person_in_round[3,4,left] - if_person_on_side[3,3,left] <= 0
 R157: - if_person_in_round[3,4,left] + if_person_in_round[3,4,right]
   - if_person_on_side[3,3,right] <= 0
 R158: if_person_in_round[3,5,left] - if_person_in_round[3,5,right]
   - if_person_on_side[3,4,left] + if_person_on_side[3,5,left] = 0
 R159: if_person_in_round[3,5,left] - if_person_on_side[3,4,left] <= 0
 R160: - if_person_in_round[3,5,left] + if_person_in_round[3,5,right]
   - if_person_on_side[3,4,right] <= 0
 R161: if_person_in_round[4,1,left] - if_person_in_round[4,1,right]
   - if_person_on_side[4,0,left] + if_person_on_side[4,1,left] = 0
 R162: if_person_in_round[4,1,left] - if_person_on_side[4,0,left] <= 0
 R163: - if_person_in_round[4,1,left] + if_person_in_round[4,1,right]
   - if_person_on_side[4,0,right] <= 0
 R164: if_person_in_round[4,2,left] - if_person_in_round[4,2,right]
   - if_person_on_side[4,1,left] + if_person_on_side[4,2,left] = 0
 R165: if_person_in_round[4,2,left] - if_person_on_side[4,1,left] <= 0
 R166: - if_person_in_round[4,2,left] + if_person_in_round[4,2,right]
   - if_person_on_side[4,1,right] <= 0
 R167: if_person_in_round[4,3,left] - if_person_in_round[4,3,right]
   - if_person_on_side[4,2,left] + if_person_on_side[4,3,left] = 0
 R168: if_person_in_round[4,3,left] - if_person_on_side[4,2,left] <= 0
 R169: - if_person_in_round[4,3,left] + if_person_in_round[4,3,right]
   - if_person_on_side[4,2,right] <= 0
 R170: if_person_in_round[4,4,left] - if_person_in_round[4,4,right]
   - if_person_on_side[4,3,left] + if_person_on_side[4,4,left] = 0
 R171: if_person_in_round[4,4,left] - if_person_on_side[4,3,left] <= 0
 R172: - if_person_in_round[4,4,left] + if_person_in_round[4,4,right]
   - if_person_on_side[4,3,right] <= 0
 R173: if_person_in_round[4,5,left] - if_person_in_round[4,5,right]
   - if_person_on_side[4,4,left] + if_person_on_side[4,5,left] = 0
 R174: if_person_in_round[4,5,left] - if_person_on_side[4,4,left] <= 0
 R175: - if_person_in_round[4,5,left] + if_person_in_round[4,5,right]
   - if_person_on_side[4,4,right] <= 0
 R176: if_person_in_round[5,1,left] - if_person_in_round[5,1,right]
   - if_person_on_side[5,0,left] + if_person_on_side[5,1,left] = 0
 R177: if_person_in_round[5,1,left] - if_person_on_side[5,0,left] <= 0
 R178: - if_person_in_round[5,1,left] + if_person_in_round[5,1,right]
   - if_person_on_side[5,0,right] <= 0
 R179: if_person_in_round[5,2,left] - if_person_in_round[5,2,right]
   - if_person_on_side[5,1,left] + if_person_on_side[5,2,left] = 0
 R180: if_person_in_round[5,2,left] - if_person_on_side[5,1,left] <= 0
 R181: - if_person_in_round[5,2,left] + if_person_in_round[5,2,right]
   - if_person_on_side[5,1,right] <= 0
 R182: if_person_in_round[5,3,left] - if_person_in_round[5,3,right]
   - if_person_on_side[5,2,left] + if_person_on_side[5,3,left] = 0
 R183: if_person_in_round[5,3,left] - if_person_on_side[5,2,left] <= 0
 R184: - if_person_in_round[5,3,left] + if_person_in_round[5,3,right]
   - if_person_on_side[5,2,right] <= 0
 R185: if_person_in_round[5,4,left] - if_person_in_round[5,4,right]
   - if_person_on_side[5,3,left] + if_person_on_side[5,4,left] = 0
 R186: if_person_in_round[5,4,left] - if_person_on_side[5,3,left] <= 0
 R187: - if_person_in_round[5,4,left] + if_person_in_round[5,4,right]
   - if_person_on_side[5,3,right] <= 0
 R188: if_person_in_round[5,5,left] - if_person_in_round[5,5,right]
   - if_person_on_side[5,4,left] + if_person_on_side[5,5,left] = 0
 R189: if_person_in_round[5,5,left] - if_person_on_side[5,4,left] <= 0
 R190: - if_person_in_round[5,5,left] + if_person_in_round[5,5,right]
   - if_person_on_side[5,4,right] <= 0
 R191: if_person_in_round[6,1,left] - if_person_in_round[6,1,right]
   - if_person_on_side[6,0,left] + if_person_on_side[6,1,left] = 0
 R192: if_person_in_round[6,1,left] - if_person_on_side[6,0,left] <= 0
 R193: - if_person_in_round[6,1,left] + if_person_in_round[6,1,right]
   - if_person_on_side[6,0,right] <= 0
 R194: if_person_in_round[6,2,left] - if_person_in_round[6,2,right]
   - if_person_on_side[6,1,left] + if_person_on_side[6,2,left] = 0
 R195: if_person_in_round[6,2,left] - if_person_on_side[6,1,left] <= 0
 R196: - if_person_in_round[6,2,left] + if_person_in_round[6,2,right]
   - if_person_on_side[6,1,right] <= 0
 R197: if_person_in_round[6,3,left] - if_person_in_round[6,3,right]
   - if_person_on_side[6,2,left] + if_person_on_side[6,3,left] = 0
 R198: if_person_in_round[6,3,left] - if_person_on_side[6,2,left] <= 0
 R199: - if_person_in_round[6,3,left] + if_person_in_round[6,3,right]
   - if_person_on_side[6,2,right] <= 0
 R200: if_person_in_round[6,4,left] - if_person_in_round[6,4,right]
   - if_person_on_side[6,3,left] + if_person_on_side[6,4,left] = 0
 R201: if_person_in_round[6,4,left] - if_person_on_side[6,3,left] <= 0
 R202: - if_person_in_round[6,4,left] + if_person_in_round[6,4,right]
   - if_person_on_side[6,3,right] <= 0
 R203: if_person_in_round[6,5,left] - if_person_in_round[6,5,right]
   - if_person_on_side[6,4,left] + if_person_on_side[6,5,left] = 0
 R204: if_person_in_round[6,5,left] - if_person_on_side[6,4,left] <= 0
 R205: - if_person_in_round[6,5,left] + if_person_in_round[6,5,right]
   - if_person_on_side[6,4,right] <= 0
Bounds
 time_round[1,left] <= 12
 time_round[1,right] <= 12
 time_round[2,left] <= 12
 time_round[2,right] <= 12
 time_round[3,left] <= 12
 time_round[3,right] <= 12
 time_round[4,left] <= 12
 time_round[4,right] <= 12
 time_round[5,left] <= 12
 time_round[5,right] <= 12
Binaries
 if_person_in_round[1,1,left] if_person_in_round[1,1,right]
 if_person_in_round[1,2,left] if_person_in_round[1,2,right]
 if_person_in_round[1,3,left] if_person_in_round[1,3,right]
 if_person_in_round[1,4,left] if_person_in_round[1,4,right]
 if_person_in_round[1,5,left] if_person_in_round[1,5,right]
 if_person_in_round[2,1,left] if_person_in_round[2,1,right]
 if_person_in_round[2,2,left] if_person_in_round[2,2,right]
 if_person_in_round[2,3,left] if_person_in_round[2,3,right]
 if_person_in_round[2,4,left] if_person_in_round[2,4,right]
 if_person_in_round[2,5,left] if_person_in_round[2,5,right]
 if_person_in_round[3,1,left] if_person_in_round[3,1,right]
 if_person_in_round[3,2,left] if_person_in_round[3,2,right]
 if_person_in_round[3,3,left] if_person_in_round[3,3,right]
 if_person_in_round[3,4,left] if_person_in_round[3,4,right]
 if_person_in_round[3,5,left] if_person_in_round[3,5,right]
 if_person_in_round[4,1,left] if_person_in_round[4,1,right]
 if_person_in_round[4,2,left] if_person_in_round[4,2,right]
 if_person_in_round[4,3,left] if_person_in_round[4,3,right]
 if_person_in_round[4,4,left] if_person_in_round[4,4,right]
 if_person_in_round[4,5,left] if_person_in_round[4,5,right]
 if_person_in_round[5,1,left] if_person_in_round[5,1,right]
 if_person_in_round[5,2,left] if_person_in_round[5,2,right]
 if_person_in_round[5,3,left] if_person_in_round[5,3,right]
 if_person_in_round[5,4,left] if_person_in_round[5,4,right]
 if_person_in_round[5,5,left] if_person_in_round[5,5,right]
 if_person_in_round[6,1,left] if_person_in_round[6,1,right]
 if_person_in_round[6,2,left] if_person_in_round[6,2,right]
 if_person_in_round[6,3,left] if_person_in_round[6,3,right]
 if_person_in_round[6,4,left] if_person_in_round[6,4,right]
 if_person_in_round[6,5,left] if_person_in_round[6,5,right]
 if_person_on_side[1,0,left] if_person_on_side[1,0,right]
 if_person_on_side[1,1,left] if_person_on_side[1,1,right]
 if_person_on_side[1,2,left] if_person_on_side[1,2,right]
 if_person_on_side[1,3,left] if_person_on_side[1,3,right]
 if_person_on_side[1,4,left] if_person_on_side[1,4,right]
 if_person_on_side[1,5,left] if_person_on_side[1,5,right]
 if_person_on_side[2,0,left] if_person_on_side[2,0,right]
 if_person_on_side[2,1,left] if_person_on_side[2,1,right]
 if_person_on_side[2,2,left] if_person_on_side[2,2,right]
 if_person_on_side[2,3,left] if_person_on_side[2,3,right]
 if_person_on_side[2,4,left] if_person_on_side[2,4,right]
 if_person_on_side[2,5,left] if_person_on_side[2,5,right]
 if_person_on_side[3,0,left] if_person_on_side[3,0,right]
 if_person_on_side[3,1,left] if_person_on_side[3,1,right]
 if_person_on_side[3,2,left] if_person_on_side[3,2,right]
 if_person_on_side[3,3,left] if_person_on_side[3,3,right]
 if_person_on_side[3,4,left] if_person_on_side[3,4,right]
 if_person_on_side[3,5,left] if_person_on_side[3,5,right]
 if_person_on_side[4,0,left] if_person_on_side[4,0,right]
 if_person_on_side[4,1,left] if_person_on_side[4,1,right]
 if_person_on_side[4,2,left] if_person_on_side[4,2,right]
 if_person_on_side[4,3,left] if_person_on_side[4,3,right]
 if_person_on_side[4,4,left] if_person_on_side[4,4,right]
 if_person_on_side[4,5,left] if_person_on_side[4,5,right]
 if_person_on_side[5,0,left] if_person_on_side[5,0,right]
 if_person_on_side[5,1,left] if_person_on_side[5,1,right]
 if_person_on_side[5,2,left] if_person_on_side[5,2,right]
 if_person_on_side[5,3,left] if_person_on_side[5,3,right]
 if_person_on_side[5,4,left] if_person_on_side[5,4,right]
 if_person_on_side[5,5,left] if_person_on_side[5,5,right]
 if_person_on_side[6,0,left] if_person_on_side[6,0,right]
 if_person_on_side[6,1,left] if_person_on_side[6,1,right]
 if_person_on_side[6,2,left] if_person_on_side[6,2,right]
 if_person_on_side[6,3,left] if_person_on_side[6,3,right]
 if_person_on_side[6,4,left] if_person_on_side[6,4,right]
 if_person_on_side[6,5,left] if_person_on_side[6,5,right]
Generals
 time_round[1,left] time_round[1,right] time_round[2,left]
 time_round[2,right] time_round[3,left] time_round[3,right]
 time_round[4,left] time_round[4,right] time_round[5,left]
 time_round[5,right]
End
