import pandas as pd
from hospital_data import transform_hospital_data

hospital_data = transform_hospital_data('data/Hospital_General_Information.csv')

print(list(hospital_data.columns))

print(hospital_data.dtypes)