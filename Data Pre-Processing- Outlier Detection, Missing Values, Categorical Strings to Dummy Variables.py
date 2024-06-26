# The length of the data
print(f"The Length of the data: {data.shape}")

# Missing values
for column in data.columns:
    if data[column].isna().sum() != 0:
        missing = data[column].isna().sum()
        portion = (missing / data.shape[0]) * 100
        print(f"'{column}': number of missing values '{missing}' ==> '{portion:.3f}%'")

data.emp_title.nunique()
data.drop('emp_title', axis=1, inplace=True)
for year in data.emp_length.unique():
    print(f"{year} years in this position:")
    print(f"{data[data.emp_length == year].loan_status.value_counts(normalize=True)}")
    print('==========================================')      

# Too many job-titles in emp-title column, the column will be removed with missing values instead. 

data.drop('emp_length', axis=1, inplace=True)
data.title.value_counts().head()
data.purpose.value_counts().head()
data.drop('title', axis=1, inplace=True)
data.mort_acc.value_counts()
data.mort_acc.isna().sum()
data.corr()['mort_acc'].drop('mort_acc').sort_values().hvplot.barh()

#The total_acc feature correlates with the mort_acc which means the categorical variables of interest have been converted. 
#Let's try this fillna() approach. 
#We will group the dataframe by the total_acc and calculate the mean value for the mort_acc per total_acc entry.

total_acc_avg = data.groupby(by='total_acc').mean().mort_acc

def fill_mort_acc(total_acc, mort_acc):
    if np.isnan(mort_acc):
        return total_acc_avg[total_acc].round()
    else:
        return mort_acc

data['mort_acc'] = data.apply(lambda x: fill_mort_acc(x['total_acc'], x['mort_acc']), axis=1)
for column in data.columns:
    if data[column].isna().sum() != 0:
        missing = data[column].isna().sum()
        portion = (missing / data.shape[0]) * 100
        print(f"'{column}': number of missing values '{missing}' ==> '{portion:.3f}%'")

data.dropna(inplace=True)
data.shape

#Categorical Variables and Dummy Variables

print(f"Data shape: {data.shape}")

# Remove duplicate Features
data = data.T.drop_duplicates()
data = data.T

# Remove Duplicate Rows
data.drop_duplicates(inplace=True)
print(f"Data shape: {data.shape}")

print([column for column in data.columns if data[column].dtype == object])

data.term.unique()

term_values = {' 36 months': 36, ' 60 months': 60}
data['term'] = data.term.map(term_values)
data.term.unique()
data.drop('grade', axis=1, inplace=True)

dummies = ['sub_grade', 'verification_status', 'purpose', 'initial_list_status', 
           'application_type', 'home_ownership']

data = pd.get_dummies(data, columns=dummies, drop_first=True)
data.address.head()
data['zip_code'] = data.address.apply(lambda x: x[-5:])
data.zip_code.value_counts()
data = pd.get_dummies(data, columns=['zip_code'], drop_first=True)
data.drop('address', axis=1, inplace=True)
data.drop('issue_d', axis=1, inplace=True)
data['earliest_cr_line'] = data.earliest_cr_line.dt.year
data.earliest_cr_line.nunique()
data.earliest_cr_line.value_counts()

