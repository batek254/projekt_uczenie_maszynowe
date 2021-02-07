import pandas as pd
import numpy as np
from scipy import stats

def choose_columns(data, columns:list):
    '''This function just choose columns from data set
    '''
    data_processed = data[columns]

    return data_processed

def treat_nan(data, columns:list, change_from:list, change_to:list):
    '''Function for selected columns using pd.DataFrame.replace change values (from) 
    to the new one (to)
    '''
    for c, f, t in zip(columns, change_from, change_to):
        data[c].replace(f, t)
    
    return data

if __name__ == '__main__':
    data = pd.read_csv('data/raw/full_data.csv')

    columns = ['id', 'status_group', 'amount_tsh', 'gps_height', 'longitude', 'latitude', 
    'basin', 'region', 'ward', 'population', 'public_meeting', 'scheme_management', 'permit', 'construction_year', 
    'extraction_type', 'management', 'payment', 'payment_type', 'water_quality', 'quantity', 'quantity_group', 
    'source', 'waterpoint_type']

    data_processed = choose_columns(data, columns)

    columns = ['longitude', 'latitude', 'population', 'construction_year', 'scheme_management', 'management', 'payment',
    'payment_type', 'water_quality', 'quantity', 'quantity_group', 'source']
    change_from = [0, -2.000000e-08, 0, 0, 'None']+['unknown']*7
    change_to = [np.nan]*12

    data_processed = treat_nan(data_processed, columns, change_from, change_to)

    data_processed.to_csv('data/processed/data_processed_nans.csv')