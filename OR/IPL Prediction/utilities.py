from libraries import *
import constants as const

def date_time_formatting(date_str, time_str):

    time_only = time_str[:-7]
    time_am_pm = 12 if time_str[5:7] == 'pm' else 0

    new_time_only = str(int(time_only[0]) + time_am_pm) + time_only[1:]

    date_obj = datetimeobj.strptime(date_str, '%b, %a %d').replace(year=datetimeobj.now().year)
    time_obj = datetimeobj.strptime(new_time_only, '%H:%M').time()

    datetime_combined = datetimeobj.combine(date_obj.date(), time_obj)

    return datetime_combined

def write_processed_output_for_input_data(points_table_df, match_schedule_df):
    points_table_df.to_csv(
        "outputs/points_table_processed_" + str(datetime.date.today()) + datetime.datetime.now().strftime(
            "_%H_%M_%S") + ".csv", index=False)

    match_schedule_df.to_csv(
        "outputs/match_schedule_processed_" + str(datetime.date.today()) + datetime.datetime.now().strftime(
            "_%H_%M_%S") + ".csv", index=False)

def print_final_outputs(possibilities_qualifying_count, qualifier1_count, eliminator_count, match_schedule_df):

    print()
    print(f'playoffs - \n{possibilities_qualifying_count}\n')
    print(f'qualifier 1 -\n{qualifier1_count}\n')
    print(f'eliminator - \n{eliminator_count}\n')

    total_possibilities = math.pow(3, len(match_schedule_df))

    probability_of_qualification_to_playoffs = {team: possibilities_qualifying_count[team]*100/total_possibilities for team in const.Teams}
    probability_of_qualification_to_qualifier1 = {team: qualifier1_count[team]*100/total_possibilities for team in const.Teams}
    probability_of_qualification_to_eliminator = {team: eliminator_count[team]*100/total_possibilities for team in const.Teams}

    print('\nchance of qualifying to playoffs -')
    for team in const.Teams:
        print(f'{team} - {probability_of_qualification_to_playoffs[team]} %')

    print('\nchance of qualifying to qualifier 1 -')
    for team in const.Teams:
        print(f'{team} - {probability_of_qualification_to_qualifier1[team]} %')

    print('\nchance of qualifying to eliminator -')
    for team in const.Teams:
        print(f'{team} - {probability_of_qualification_to_eliminator[team]} %')

    output_list = [list(probability_of_qualification_to_playoffs.values()),
                   list(probability_of_qualification_to_qualifier1.values()),
                   list(probability_of_qualification_to_eliminator.values())]

    output_df = pd.DataFrame(output_list,
                             index = ['PLAYOFFS', 'QUALIFIER 1', 'ELIMINATOR'],
                             columns = list(probability_of_qualification_to_playoffs))

    output_df.to_csv(
        f"outputs/output_matches_left_{len(match_schedule_df)}_" + str(datetime.date.today()) + datetime.datetime.now().strftime(
            "_%H_%M_%S") + ".csv")