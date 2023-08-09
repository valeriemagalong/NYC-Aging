import numpy as np
import pandas as pd


## Clean Senior Center Provider Data


scpd_raw = pd.read_csv('raw_csv/senior_center_provider_data_fy2020.csv')

# Make a copy of the raw dataframe
scpd = scpd_raw.copy()

# Drop columns you won't be using
scpd.drop(columns = ['Sponsor Name', 'Program Address', 'Program Address1', 'Postcode',
                    'Community Board', 'Council D istrict', 'Sunday', 'Monday', 'Tuesday',
                     'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Fiscal Year Amount',
                     'FY 20 Actual Meals', 'Meal Prep', 'Meals Prep for Others', 'Borough',
                     'Census Tract', 'BIN', 'BBL', 'NTA'], inplace = True)

# Rename columns to be more intuitive (based on data dictionary descriptions)
scpd.rename(columns = {
    'Provider Name': 'Senior Center Name',
    'Borough/City': 'Borough',
    '# of Full-time Staff': 'Total FTEs',
    '# of Part-time Staff': 'Total PTEs',
    'Average Daily Participants': 'Average Daily Clients',
    'Kosher Raw Food/ Disposable': 'Kosher Meal Budget',
    'Non-Kosher Raw Food/ Disposable': 'Non-Kosher Meal Budget',
    'Total Raw Food/ Disposable': 'Total Meal Budget',
    'Expenditures per Meal for Food and Disposable': 'Average Meal Expenditure Per Client',
    'Meal Prep1': 'Meal Prep Type',
    'Prep for Others1': 'Meal Prep For Other Centers',
    'Annual Expenditures for Information and Assistance, Education and Recreation, Health Promotion': 'Total AIB-SCE-HPP Expenditures',
    'Annual Expenditures Per Client for Information and Assistance, Education and Recreation, Health Promotion': 'Average AIB-SCE-HPP Expenditures Per Client',
    'Ultilization': 'Percent Utilization'
}, inplace = True)

# Rename columns to be more intuitive (based on data dictionary descriptions)
scpd.rename(columns = {
    'Provider Name': 'Senior Center Name',
    'Borough/City': 'Borough',
    '# of Full-time Staff': 'Total FTEs',
    '# of Part-time Staff': 'Total PTEs',
    'Average Daily Participants': 'Average Daily Clients',
    'Kosher Raw Food/ Disposable': 'Kosher Meal Budget',
    'Non-Kosher Raw Food/ Disposable': 'Non-Kosher Meal Budget',
    'Total Raw Food/ Disposable': 'Total Meal Budget',
    'Expenditures per Meal for Food and Disposable': 'Average Meal Expenditure Per Client',
    'Meal Prep1': 'Meal Prep Type',
    'Prep for Others1': 'Meal Prep For Other Centers',
    'Annual Expenditures for Information and Assistance, Education and Recreation, Health Promotion': 'Total AIB-SCE-HPP Expenditures',
    'Annual Expenditures Per Client for Information and Assistance, Education and Recreation, Health Promotion': 'Average AIB-SCE-HPP Expenditures Per Client',
    'Ultilization': 'Percent Utilization'
}, inplace = True)

# Drop redundant budget and reimbursement columns
scpd.drop(columns = ['FY 20 Budget', 'Personnel Budget', 'FY 20 Reimbursement'], inplace = True)

# Rename columns to be more intuitive (based on data dictionary descriptions)
scpd.rename(columns = {
    'Total FY20 Budget': 'Total Budget',
    'Total FY20 Personnel Budget': 'Total Personnel Budget',
    'Total FY20 Reimbursement': 'Total Expenses'
}, inplace = True)

# Fill NaNs in 'Latitude' and 'Longitude' with corresponding values in fill_dict
fill_cols = ['Latitude', 'Longitude']
fill_dict = {
    102: [40.596868706020445, -74.07555607642975],
    126: [40.82651347755042, -73.91661122662934],
    139: [40.85396935386981, -73.88190264660648],
    169: [40.67530765760249, -73.92446824134545],
    179: [40.602035938136076, -73.95715926297987],
    192: [40.696071010269755, -73.99506336199069],
    214: [40.830937975634, -73.93751073154422],
    228: [40.79462754058644, -73.93706847434424],
    231: [40.80412527380681, -73.95489674318942],
    260: [40.76252319677368, -73.93704370456038],
    273: [40.72522541418266, -73.76483607547621]
}
fill_df = pd.DataFrame(fill_dict.values(), index = fill_dict.keys(), columns = ['Latitude', 'Longitude'])

for col in fill_cols:
    scpd.loc[scpd[col].isna(), col] = scpd.loc[scpd[col].isna(), col].fillna(fill_df[col])
    
# Replace zeroes in 'Kosher Meal Budget', 'Non-Kosher Meal Budget', 'Total Meal Budget', 'Average Meal Expenditure Per Client', and 'Total AIB-SCE-HPP Expenditures' with NaN
fill_cols = ['Kosher Meal Budget', 'Non-Kosher Meal Budget', 'Total Meal Budget', 'Average Meal Expenditure Per Client', 'Total AIB-SCE-HPP Expenditures']

for col in fill_cols:
    scpd.loc[scpd[col] == 0, col] = scpd.loc[scpd[col].isna(), col].replace(0, np.nan)
    
# Fill NaNs in 'Total FTEs' and 'Months in HHS' columns with 0
for col in ['Total FTEs', 'Months in HHS']:
    scpd[col] = scpd[col].fillna(0)
    
# Title-case columns with strings
for col in ['Senior Center Name', 'Site Type', 'Borough', 'Meal Prep Type']:
    scpd[col] = scpd[col].str.title()
    
# Fill NaNs in 'Meal Prep Type' with 'Not Applicable'
scpd.loc[scpd['Meal Prep Type'].isna(), 'Meal Prep Type'] = scpd.loc[scpd['Meal Prep Type'].isna(), 'Meal Prep Type'].fillna('Not Applicable')

# Fill NaNs in 'Meal Prep For Other Centers' with 'No'
scpd.loc[scpd['Meal Prep For Other Centers'].isna(), 'Meal Prep For Other Centers'] = scpd.loc[scpd['Meal Prep For Other Centers'].isna(), 'Meal Prep For Other Centers'].fillna('No')

# Change data type of 'Total FTEs' and 'Months in HHS' to integer
for col in ['Total FTEs', 'Months in HHS']:
    scpd[col] = scpd[col].astype(int)
    
# Add five derived columns to scpd dataframe
scpd['Total Employees'] = scpd['Total FTEs'] + scpd['Total PTEs']
scpd['Client to Staff Ratio'] = scpd['Average Daily Clients'] / scpd['Total Employees']
scpd['PTE Status'] = scpd['Total PTEs'].apply(lambda num: 'Has No PTEs' if num == 0 else 'Has PTEs')
scpd['% Budget Allocated for Personnel'] = scpd['Total Personnel Budget'] / scpd['Total Budget']
scpd['% Budget Allocated for Meals'] = scpd['Total Meal Budget'] / scpd['Total Budget']
scpd['% Budget Used for AIB, SCE, & HPP Services'] = scpd['Total AIB-SCE-HPP Expenditures'] / scpd['Total Budget']



## Clean Senior Center Client Data


sccd_raw = pd.read_csv('raw_csv/senior_center_client_data_fy2020.csv')

# Make a copy of the raw dataframe
sccd = sccd_raw.copy()

# Merge columns from senior center provider dataset (i.e. left join sccd with scpd)
merge_cols = ['Senior Center Name', 'Site Type', 'Borough', 'Meal Prep Type', 'Meal Prep For Other Centers', 'Total Employees', 'Client to Staff Ratio', 'PTE Status']
sccd = sccd.merge(scpd[merge_cols], how = 'left', left_on = 'dftaid', right_on = scpd['DFTA ID'])

# Rename columns to be more intuitive (based on data dictionary descriptions)
sccd.rename(columns = {
    'dftaid': 'DFTA ID',
    'service_date': 'Service Date',
    'total_daily': 'Total Daily Services',
    'breakfast_units': 'Total Breakfasts Served',
    'lunch_units': 'Total Lunches Served',
    'dinner_units': 'Total Dinners Served',
    'tot_meals': 'Total Meals Served',
    'aib_tot': 'Total AIB Services',
    'sce_tot': 'Total SCE Services',
    'hpp_tot': 'Total HPP Services',
    'tot_serv_pp': 'Total Clients Served',
    'Senior Center Name_x': 'Senior Center Name',
    'Site Type_x': 'Site Type', 
    'Borough_x': 'Borough', 
    'Meal Prep Type_x': 'Meal Prep Type',
    'Meal Prep For Other Centers_x': 'Meal Prep For Other Centers', 
    'Total Employees_x': 'Total Employees',
    'Client to Staff Ratio_x': 'Client to Staff Ratio', 
    'PTE Status_x': 'PTE Status', 
    'Senior Center Name_y': 'Senior Center Name',
    'Site Type_y': 'Site Type', 
    'Borough_y': 'Borough', 
    'Meal Prep Type_y': 'Meal Prep Type',
    'Meal Prep For Other Centers_y': 'Meal Prep For Other Centers', 
    'Total Employees_y': 'Total Employees',
    'Client to Staff Ratio_y': 'Client to Staff Ratio', 
    'PTE Status_y': 'PTE Status'
}, inplace = True)

# Drop the redundant provider_name column, since there is a merged Senior Center Name column now
sccd.drop(columns = 'provider_name', inplace = True)

# Drop the rows that have NaNs in Senior Center Name (i.e. didn't have a match in scpd dataframe)
sccd.drop(index = sccd[sccd['Senior Center Name'].isna()].index, inplace = True)

# Cast the values in 'Service Date' to datetimes
sccd['Service Date'] = pd.to_datetime(sccd['Service Date'], format = '%m/%d/%Y')

# Derive a column called 'Service Month' from the 'Service Date' column
sccd['Service Month'] = sccd['Service Date'].dt.strftime('%B %Y')

# Derive a column called 'Service Month as Num' from the 'Service Date' column
sccd['Service Month as Num'] = sccd['Service Date'].dt.month

# Derive a column called 'Fiscal Quarter' from the 'Service Month' column
def get_fiscal_quarter(month):
    if month in ['July 2019', 'August 2019', 'September 2019']:
        return 'Q1'
    elif month in ['October 2019', 'November 2019', 'December 2019']:
        return 'Q2'
    elif month in ['January 2020', 'February 2020', 'March 2020']:
        return 'Q3'
    elif month in ['April 2020', 'May 2020', 'June 2020']:
        return 'Q4'
    
sccd['Fiscal Quarter'] = sccd['Service Month'].apply(get_fiscal_quarter)

