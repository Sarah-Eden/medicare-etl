import pandas as pd
import numpy as np
from utils import load_data


"""Imports data from a specified CSV file and returns a cleaned DataFrame for upload into Snowflake."""
def transform_hospital_data(file_path):

    hospital_df = load_data(file_path)


    measure = ['MORT', 'Safety', 'READM', 'Pt Exp', 'TE']
    suffix = ['Group', 'Facility', 'Better', 'No Different', 'Worse']
    col_dict = {}

    for m in measure:
        for idx, s in enumerate(suffix):
            match idx:
                case 0:
                    col_dict[f'{m} {s} Measure Count'] = f'{m}_{s}_Count'
                case 1:
                    col_dict[f'Count of {s} {m} Measures'] = f'{m}_{s}_Count'
                    if m == 'Pt Exp' or m == 'TE':
                        break
                case _:
                    col_dict[f'Count of {m} Measures {s}'] = f'{m}_{s}_Count'


    hospital_df.rename(columns=col_dict, inplace=True)
    
    hospital_df.columns = [col.upper().replace(' ', '_').replace('/', '_') for col in hospital_df.columns]

    hospital_df['ZIP_CODE'] = hospital_df['ZIP_CODE'].astype(str).str.zfill(5)

    hospital_df.replace('Not Available', np.nan, inplace=True)

    num_col = [c for c in hospital_df.columns if "_COUNT" in c]
    num_col.append('HOSPITAL_OVERALL_RATING')

    hospital_df[num_col]=hospital_df[num_col].apply(pd.to_numeric)

    return hospital_df
