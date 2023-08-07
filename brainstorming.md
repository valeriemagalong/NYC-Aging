# NYC Aging Python Project
## Analyzing NYC OpenData from the Department for the Aging

### About the .csv files
* *all_contracted_providers.csv*
  * 379 rows, 8 columns
  * `['Contract Type', 'Provider ID', 'Program Name', 'Sponsor Name',
       'Program Address', 'Program Borough', 'Program Zipcode',
       'Program Phone']`
* *bottom_line_budget.csv*
  * 419 rows, 10 columns
  * `['ProviderType', 'DFTA ID', 'ContractYear', 'SponsorName', 'ProgramName',
       'DFTA Funded', 'BudgetPeriod', 'TotalBudgetAmount',
       'ServicesBudgetAmount', 'Equipment+OneTimePaymentAmount']`
* *budgeted_services.csv*
  * 3444 rows, 8 columns
  * `['ProviderType', 'DFTA ID', 'ContractYear', 'SponsorName', 'ProgramName',
       'ServiceID', 'ServiceName', 'BudgetedUnits']`
* *contracted_providers_expanded.csv*
  * 474 rows, 34 columns
  * `['ProviderType', 'DFTA ID', 'ProgramName', 'SponsorName',
       'ProgramAddress', 'ProgramCity', 'ProgramState', 'Postcode', 'Borough',
       'ProgramPhone', 'DFTA Funded', 'MonHourOpen', 'MonHourClose',
       'TueHourOpen', 'TueHourClose', 'WedHourOpen', 'WedHourClose',
       'ThuHourOpen', 'ThuHourClose', 'FriHourOpen', 'FriHourClose',
       'SatHourOpen', 'SatHourClose', 'SunHourOpen', 'SunHourClose',
       'Latitude', 'Longitude', 'Community Board', 'Council District',
       'Census Tract', 'BIN', 'BBL', 'NTA', 'Location 1']`
* *reported_expenditures.csv*
  * 72700 rows, 9 columns
  * `['ProviderType', 'DFTA ID', 'ContractYear', 'SponsorName', 'ProgramName',
       'LineItem', 'LineItemName', 'ReportedMonth', 'ReportedAmount']`
* *reported_service_units.csv*
  * 47500 rows, 9 columns
  * `['ProviderType', 'DFTA ID', 'ContractYear', 'SponsorName', 'ProgramName',
       'ServiceID', 'ServiceName', 'ReportedMonth', 'ReportedUnits']`
* *senior_center_client_data_fy2020.csv*
  * 69200 rows, 12 columns
  * `['dftaid', 'provider_name', 'service_date', 'total_daily',
       'breakfast_units', 'lunch_units', 'dinner_units', 'tot_meals',
       'aib_tot', 'sce_tot', 'hpp_tot', 'tot_serv_pp']`
* *senior_center_provider_data_fy2020.csv*
  * 294 rows, 49 columns
  * `['DFTA ID', 'Provider Name', 'Sponsor Name', 'Site Type',
       'Program Address', 'Program Address1', 'Borough/City', 'Postcode',
       'Contract From Date', 'Contract To Date', 'Community Board',
       'Council D istrict', 'Sunday', 'Monday', 'Tuesday', 'Wednesday',
       'Thursday', 'Friday', 'Saturday', 'FY 20 Budget', 'FY 20 Reimbursement',
       '# of Full-time Staff', '# of Part-time Staff', 'Personnel Budget',
       'Fiscal Year Amount', 'Months in HHS', 'Total FY20 Budget',
       'Total FY20 Personnel Budget', 'Total FY20 Reimbursement',
       'Average Daily Participants', 'FY 20 Actual Meals',
       'Kosher Raw Food/ Disposable', 'Non-Kosher Raw Food/ Disposable',
       'Total Raw Food/ Disposable',
       'Expenditures per Meal for Food and Disposable', 'Meal Prep',
       'Meal Prep1', 'Meals Prep for Others', 'Prep for Others1',
       'Annual Expenditures for Information and Assistance, Education and Recreation, Health Promotion',
       'Annual Expenditures Per Client for Information and Assistance, Education and Recreation, Health Promotion',
       'Ultilization', 'Borough', 'Latitude', 'Longitude', 'Census Tract',
       'BIN', 'BBL', 'NTA']`
* *social_adult_day_care_services.csv*
  * 15 rows, 34 columns
  * `['ProviderType', 'DFTA ID', 'ProgramName', 'SponsorName',
       'ProgramAddress', 'ProgramCity', 'ProgramState', 'Postcode', 'Borough',
       'ProgramPhone', 'DFTA Funded', 'MonHourOpen', 'MonHourClose',
       'TueHourOpen', 'TueHourClose', 'WedHourOpen', 'WedHourClose',
       'ThuHourOpen', 'ThuHourClose', 'FriHourOpen', 'FriHourClose',
       'SatHourOpen', 'SatHourClose', 'SunHourOpen', 'SunHourClose',
       'Latitude', 'Longitude', 'Community Board', 'Council District',
       'Census Tract', 'BIN', 'BBL', 'NTA', 'Location 1']`