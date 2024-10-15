import constants
from libraries import *
import utilities

def read_input_files():
    input_path = r"\inputs"
    current_directory = os.getcwd()
    try:
        IPL_2024_data = current_directory + input_path + r"\IPL_TABLE_LIVE.xlsx"
        points_table_df = pd.read_excel(IPL_2024_data, sheet_name="Sheet2")
        match_schedule_df = pd.read_excel(IPL_2024_data, sheet_name="Sheet3")
        return points_table_df, match_schedule_df
    except:
        print("no such file / sheet name exists")
        return None, None

def process_input_df(points_table_df, match_schedule_df):
    points_table_columns = ["POSITION", "GROUP", "TEAM", "PLAYED", "WON", "LOSS", "NO RESULT", "POINTS", "NRR"]
    match_schedule_columns = ['STADIUM', 'DATE', 'TIME', 'TEAM 1', 'TEAM 2', 'MATCH NUM']

    try:
        points_table_df.columns = points_table_columns
        match_schedule_df.columns = match_schedule_columns
    except:
        print("column length mismatch")
        return None, None

    points_table_df = points_table_df.astype(
        {"POSITION": int, "PLAYED": int, "WON": int, "LOSS": int, "NO RESULT": int, "POINTS": int})
    points_table_df["NRR"] = points_table_df["NRR"].astype(float)

    try:
        points_table_df['TEAM'] = points_table_df['TEAM'].map(constants.Team_name_map)
        match_schedule_df['TEAM 1'] = match_schedule_df['TEAM 1'].map(constants.Team_name_map)
        match_schedule_df['TEAM 2'] = match_schedule_df['TEAM 2'].map(constants.Team_name_map)

        match_schedule_df['DATE'] = match_schedule_df.apply(
            lambda row: utilities.date_time_formatting(row['DATE'], row['TIME']), axis=1)

    except:
        print("possible error in input")
        return None, None

    # utilities.write_processed_output_for_input_data(points_table_df, match_schedule_df)

    return points_table_df, match_schedule_df