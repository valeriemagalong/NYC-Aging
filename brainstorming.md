# NYC Aging Python Project
## Analyzing NYC OpenData from the Department for the Aging

### About the NYC Department for the Aging
From [NYC.gov](https://www.nyc.gov/site/dfta/about/commissioners-message.page):
> ...the NYC Department for the Aging is deeply committed to helping older adults age in their homes and creating a community-care approach that reflects a model age-inclusive city.
> 
> We accomplish these goals by **partnering with hundreds of community-based organizations to provide services** through older adult centers, naturally occurring retirement communities, case-management and home-care agencies, home-delivered meal programs, mental health and friendly visiting programs, and much more in each borough.

From the data dictionary for `reported_expenditures.csv`:
> The NYC Department for the Aging (NYC Aging) provides a wide array of services to assist older adults in New York City.  To accomplish this, the department **contracts out to organizations (mainly non-profit) to provide services** throughout the five boroughs.

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

### What observations have come out of exploratory data analysis?
1. Brooklyn has the most senior centers (97) partnered with NYC Aging, followed by Manhattan (73).
2. Staten Island and Manhattan have the highest median number of employees (12 and 10 respectively) per senior center.  Brooklyn & Bronx have the lowest (8 respectively).
3. 83% of Staten Island's senior centers & 64% of Manhattan's have both PTEs and FTEs.  Brooklyn & Bronx have the lowest percentage of their senior centers with both employee types (44% and 41% respectively).
4. Staten Island and Queens have the highest median number of FTEs (8 respectively) per senior center.  Manhattan has the lowest (6).
5. Staten Island and Manhattan have the highest median number of PTEs (5 and 2 respectively).  The median number of PTEs in the other boroughs is 0.
6. Staten Island and Manhattan have the highest median number of daily clients per senior center (85 respectively).  Brooklyn & Bronx have the lowest (72 and 62 respectively).
7. There is a positive correlation between Total Employees and Average Daily Clients for Manhattan (r = 0.58) and Bronx (r = 0.56). Brooklyn has the weakest correlation (r = 0.20).
8. Staten Island & Brooklyn have the lowest median Client to Staff Ratio (5:1 and 7:1 respectively).  The other boroughs have a 8:1 client to staff ratio.
9. There is a positive correlation between client to staff ratio and average daily clients for all boroughs except the Bronx (r = 0.27).
10. Queens and Staten Island have the highest median annual expenses per senior center (510k and 490k respectively).  Brooklyn and Bronx have the lowest (446k and 384k).
11. Staten Island and Brooklyn have the highest median percent budget allocated for meals (48% and 46% respectively).  Bronx has the lowest (38%).
12. Staten Island and Queens have the highest median meal expenditure per client ($9.82 and $9.65 respectively.)  Bronx has the lowest ($8.27).

**Take-Homes**
* Manhattan has the most employees, most daily clients, highest % of senior centers with both FTEs & PTEs 
* Brooklyn has the most senior centers, lowest client-to-staff ratio, second lowest daily clients, weakest correlation between employees and daily clients, second lowest annual expenses, highest % budget allocated for meals
* Bronx has the lowest daily clients, weakest correlation between client-to-staff ratio and daily clients, lowest annual expenses, lowest % budget allocated for meals, lowest meal expenditure per client
* Queens has the highest annual expenses, highest meal expenditure per client