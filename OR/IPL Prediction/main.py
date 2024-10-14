from libraries import *
import constants as const
from readingInput import read_input_files, process_input_df
import utilities
from calcPossibilityFunction import create_possibilities

def optimizer_flow():

    points_table_df, match_schedule_df = read_input_files()
    if points_table_df is None or match_schedule_df is None:
        print("error in reading input")
        return

    points_table_df, match_schedule_df = process_input_df(points_table_df, match_schedule_df)
    if points_table_df is None or match_schedule_df is None:
        print("error in processing input")
        return

    possibilities_qualifying_count, qualifier1_count, eliminator_count = create_possibilities(points_table_df, match_schedule_df)

    utilities.print_final_outputs(possibilities_qualifying_count, qualifier1_count, eliminator_count, match_schedule_df)

if __name__ == '__main__':
    optimizer_flow()