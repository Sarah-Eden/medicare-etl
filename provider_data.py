import pandas as pd
import numpy as np
from utils import load_data, standardize_zipcode

DEMOGRAPHICS_COLUMNS = ['Rndrng_NPI', 'Rndrng_Prvdr_Last_Org_Name',
                        'Rndrng_Prvdr_First_Name', 'Rndrng_Prvdr_MI',
                        'Rndrng_Prvdr_Crdntls', 'Rndrng_Prvdr_Ent_Cd',
                        'Rndrng_Prvdr_St1', 'Rndrng_Prvdr_St2',
                        'Rndrng_Prvdr_City', 'Rndrng_Prvdr_State_Abrvtn',
                        'Rndrng_Prvdr_State_FIPS', 'Rndrng_Prvdr_Zip5', 
                        'Rndrng_Prvdr_RUCA', 'Rndrng_Prvdr_RUCA_Desc', 
                        'Rndrng_Prvdr_Cntry', 'Rndrng_Prvdr_Type']

SERVICES_COLUMNS = ['Rndrng_NPI', 'HCPCS_Cd', 'HCPCS_Desc',
                    'HCPCS_Drug_Ind', 'Place_Of_Srvc', 'Tot_Benes',
                    'Tot_Bene_Day_Srvcs', 'Rndrng_Prvdr_Mdcr_Prtcptg_Ind',
                    'Avg_Sbmtd_Chrg', 'Avg_Mdcr_Alowd_Amt',
                    'Avg_Mdcr_Pymt_Amt', 'Avg_Mdcr_Stdzd_Amt', 'Tot_Srvcs']

def create_demographics_table(df):
    demographics_df = df[DEMOGRAPHICS_COLUMNS].copy()

    demographics_df['Rndrng_Prvdr_Zip5'] = standardize_zipcode(demographics_df['Rndrng_Prvdr_Zip5'])

    has_fips = demographics_df['Rndrng_Prvdr_State_FIPS'].notna()
    demographics_df.loc[has_fips, 'Rndrng_Prvdr_State_FIPS'] = demographics_df.loc[has_fips, 'Rndrng_Prvdr_State_FIPS'].astype(str).str.zfill(2)

    demographics_df.columns = [col.upper() for col in demographics_df.columns]

    demographics_df.drop_duplicates(inplace=True)

    if demographics_df.shape[0] != df['Rndrng_NPI'].nunique():
        raise ValueError(f'Inconsistencies within zipcode or FIPS data. Please verify output.')
    
    return demographics_df
 

def create_services_table(df):
    services_df = df[SERVICES_COLUMNS].copy()

    services_df.columns = [col.upper() for col in services_df.columns]

    return services_df 


def transform_provider_data(file_path):

    provider_df = load_data(file_path)

    demographics_df = create_demographics_table(provider_df)
    services_df = create_services_table(provider_df)

    return demographics_df, services_df

