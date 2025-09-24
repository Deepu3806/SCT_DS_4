import pandas as pd

file_path = 'Accident_dataset.xlsx'
data = pd.read_excel(file_path)

# The data is in one combined column, split it by comma
data_split = data[data.columns[0]].str.split(',', expand=True)

# Now assign proper column names manually
data_split.columns = ['Accident_ID', 'Date_Time', 'Road_Condition', 'Weather', 'Time_of_Day', 'Latitude', 'Longitude', 'Contributing_Factor']

# Check the fixed data
print(data_split.head())
print(data_split.info())
