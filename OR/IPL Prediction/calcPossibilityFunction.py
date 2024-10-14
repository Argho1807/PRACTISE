import copy

from libraries import *
import constants as const

def create_possibilities(points_table_df, match_schedule_df):

    global RESULTS, TEAMS_QUALIFYING, possibilities_qualifying_count, qualifier1_count, eliminator_count
    RESULTS = []
    TEAMS_QUALIFYING = []
    possibilities_qualifying_count = {team: 0 for team in const.Teams}
    qualifier1_count = {team: 0 for team in const.Teams}
    eliminator_count = {team: 0 for team in const.Teams}

    MATCH_NUM = 0

    match_won(MATCH_NUM, points_table_df, match_schedule_df)
    match_loss(MATCH_NUM, points_table_df, match_schedule_df)
    match_no_result(MATCH_NUM, points_table_df, match_schedule_df)

    return possibilities_qualifying_count, qualifier1_count, eliminator_count

def match_won(PREV_MATCH_NUM, points_table_df, match_schedule_df):

    prev_match_teams = [match_schedule_df.loc[PREV_MATCH_NUM, 'TEAM 1'], match_schedule_df.loc[PREV_MATCH_NUM, 'TEAM 2']]

    updated_points_table_df = copy.deepcopy(points_table_df)

    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[0], 'PLAYED'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[1], 'PLAYED'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[0], 'POINTS'] += 2
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[0], 'WON'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[1], 'LOSS'] += 1

    NEXT_MATCH_NUM = PREV_MATCH_NUM + 1
    if NEXT_MATCH_NUM >= len(match_schedule_df):
        find_qualifying_teams(updated_points_table_df)
        return

    match_won(NEXT_MATCH_NUM, updated_points_table_df, match_schedule_df)
    match_loss(NEXT_MATCH_NUM, updated_points_table_df, match_schedule_df)
    match_no_result(NEXT_MATCH_NUM, updated_points_table_df, match_schedule_df)

def match_loss(PREV_MATCH_NUM, points_table_df, match_schedule_df):

    prev_match_teams = [match_schedule_df.loc[PREV_MATCH_NUM, 'TEAM 1'], match_schedule_df.loc[PREV_MATCH_NUM, 'TEAM 2']]

    updated_points_table_df = copy.deepcopy(points_table_df)

    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[0], 'PLAYED'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[1], 'PLAYED'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[1], 'POINTS'] += 2
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[0], 'LOSS'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[1], 'WON'] += 1

    NEXT_MATCH_NUM = PREV_MATCH_NUM + 1
    if NEXT_MATCH_NUM >= len(match_schedule_df):
        find_qualifying_teams(updated_points_table_df)
        return

    match_won(NEXT_MATCH_NUM, updated_points_table_df, match_schedule_df)
    match_loss(NEXT_MATCH_NUM, updated_points_table_df, match_schedule_df)
    match_no_result(NEXT_MATCH_NUM, updated_points_table_df, match_schedule_df)

def match_no_result(PREV_MATCH_NUM, points_table_df, match_schedule_df):

    prev_match_teams = [match_schedule_df.loc[PREV_MATCH_NUM, 'TEAM 1'], match_schedule_df.loc[PREV_MATCH_NUM, 'TEAM 2']]

    updated_points_table_df = copy.deepcopy(points_table_df)

    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[0], 'PLAYED'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[1], 'PLAYED'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[0], 'POINTS'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[1], 'POINTS'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[0], 'NO RESULT'] += 1
    updated_points_table_df.loc[updated_points_table_df['TEAM'] == prev_match_teams[1], 'NO RESULT'] += 1

    NEXT_MATCH_NUM = PREV_MATCH_NUM + 1
    if NEXT_MATCH_NUM >= len(match_schedule_df):
        find_qualifying_teams(updated_points_table_df)
        return

    match_won(NEXT_MATCH_NUM, updated_points_table_df, match_schedule_df)
    match_loss(NEXT_MATCH_NUM, updated_points_table_df, match_schedule_df)
    match_no_result(NEXT_MATCH_NUM, updated_points_table_df, match_schedule_df)

def find_qualifying_teams(points_table_df):

    points_table_df_sorted = points_table_df.sort_values(by=['POINTS', 'NRR'], ascending=[False, False])
    points_table_df_sorted['POSITION'] = range(1, len(points_table_df_sorted) + 1)
    points_table_df_sorted.reset_index(drop=True, inplace=True)

    temp_playoffs = {team: 0 for team in const.Teams}
    temp_qualifier1 = {team: 0 for team in const.Teams}
    temp_eliminator = {team: 0 for team in const.Teams}

    start_pos = 0
    while True:
        if start_pos >= 4:
            break
        next_pos = start_pos + 1
        while True:
            if points_table_df_sorted.loc[start_pos, 'POINTS'] != points_table_df_sorted.loc[next_pos, 'POINTS']:
                break
            next_pos += 1

        ratio_temp = max(0, next_pos - 4)

        for pos in range(start_pos, next_pos):
            temp_playoffs[points_table_df_sorted.loc[pos, 'TEAM']] = 1 - (ratio_temp/(next_pos-start_pos))
            possibilities_qualifying_count[points_table_df_sorted.loc[pos, 'TEAM']] += 1 - (ratio_temp/(next_pos-start_pos))

        start_pos = copy.deepcopy(next_pos)

    start_pos_q1 = 0
    while True:
        if start_pos_q1 >= 4:
            break
        next_pos_q1 = start_pos_q1 + 1
        while True:
            if points_table_df_sorted.loc[start_pos_q1, 'POINTS'] != points_table_df_sorted.loc[next_pos_q1, 'POINTS']:
                break
            next_pos_q1 += 1

        APPLY_QUALIFIER_CHANGE = True
        APPLY_ELIMINATOR_CHANGE = True
        LB_QUALIFIER = 0
        UB_QUALIFIER = 2
        LB_ELIMINATOR = 2
        UB_ELIMINATOR = 4

        if start_pos_q1 < 2 and next_pos_q1 <= 2:
            ratio_temp_q1 = 1
            LB_QUALIFIER = start_pos_q1
            UB_QUALIFIER = next_pos_q1
            APPLY_ELIMINATOR_CHANGE = False
        elif start_pos_q1 < 2 and next_pos_q1 <= 4:
            ratio_temp_q1 = (2-start_pos_q1)/(next_pos_q1-start_pos_q1)
            ratio_temp_e = (next_pos_q1-2)/(next_pos_q1-start_pos_q1)
            LB_QUALIFIER = start_pos_q1
            UB_QUALIFIER = next_pos_q1
            LB_ELIMINATOR = start_pos_q1
            UB_ELIMINATOR = next_pos_q1
        elif start_pos_q1 < 2 and next_pos_q1 > 4:
            ratio_temp_q1 = (2-start_pos_q1)/(next_pos_q1-start_pos_q1)
            ratio_temp_e = 2/(next_pos_q1-start_pos_q1)
            LB_QUALIFIER = start_pos_q1
            UB_QUALIFIER = next_pos_q1
            LB_ELIMINATOR = start_pos_q1
            UB_ELIMINATOR = next_pos_q1
        elif start_pos_q1 < 4 and next_pos_q1 <= 4:
            ratio_temp_e = 1
            LB_ELIMINATOR = start_pos_q1
            UB_ELIMINATOR = next_pos_q1
            APPLY_QUALIFIER_CHANGE = False
        elif start_pos_q1 < 4 and next_pos_q1 > 4:
            ratio_temp_e = (4-start_pos_q1)/(next_pos_q1-start_pos_q1)
            LB_ELIMINATOR = start_pos_q1
            UB_ELIMINATOR = next_pos_q1
            APPLY_QUALIFIER_CHANGE = False

        if APPLY_QUALIFIER_CHANGE:
            for pos in range(LB_QUALIFIER, UB_QUALIFIER):
                temp_qualifier1[points_table_df_sorted.loc[pos, 'TEAM']] = ratio_temp_q1
                qualifier1_count[points_table_df_sorted.loc[pos, 'TEAM']] += ratio_temp_q1

        if APPLY_ELIMINATOR_CHANGE:
            for pos in range(LB_ELIMINATOR, UB_ELIMINATOR):
                temp_eliminator[points_table_df_sorted.loc[pos, 'TEAM']] = ratio_temp_e
                eliminator_count[points_table_df_sorted.loc[pos, 'TEAM']] += ratio_temp_e

        start_pos_q1 = copy.deepcopy(next_pos_q1)

    # for position in range(4):
        # if position <= 1:
        #     qualifier1_count[points_table_df_sorted.loc[position, 'TEAM']] += 1
        # if position > 1:
        #     eliminator_count[points_table_df_sorted.loc[position, 'TEAM']] += 1

    # print(possibilities_qualifying_count)
    # print(qualifier1_count)
    # print(eliminator_count)
    #
    # print('\n')
    print(temp_playoffs)
    print(temp_qualifier1)
    print(temp_eliminator)

    return