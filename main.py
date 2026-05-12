import pandas as pd
from hospital_data import transform_hospital_data
from provider_data import transform_provider_data

hospital_data = transform_hospital_data('data/Hospital_General_Information.csv')

print(list(hospital_data.columns))

print(hospital_data.dtypes)

demographics_data, services_data = transform_provider_data('data/MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv')

print(list(demographics_data.dtypes))
print(list(services_data.dtypes))