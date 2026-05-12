import pandas as pd
import numpy as np
from utils import load_data, standardize_zipcode


"""Imports data from a specified CSV file and returns a cleaned DataFrame for upload into Snowflake."""
def transform_hospital_data(file_path):

    hospital_df = load_data(file_path)

    hospital_df.columns = [col.upper().replace(' ', '_').replace('/', '_') for col in hospital_df.columns]

    hospital_df['ZIP_CODE'] = standardize_zipcode(hospital_df['ZIP_CODE'])

    hospital_df.replace('Not Available', np.nan, inplace=True)

    num_col = [c for c in hospital_df.columns if "_COUNT" in c]
    num_col.append('HOSPITAL_OVERALL_RATING')

    hospital_df[num_col]=hospital_df[num_col].apply(pd.to_numeric)

    return hospital_df
