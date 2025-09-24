import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Step 1: Load dataset and split combined column
file_path = 'Accident_dataset.xlsx'
data = pd.read_excel(file_path)

# The data is combined in one column, split by commas
data_split = data[data.columns[0]].str.split(',', expand=True)

# Rename columns properly
data_split.columns = ['Accident_ID', 'Date_Time', 'Road_Condition', 'Weather', 'Time_of_Day',
                      'Latitude', 'Longitude', 'Contributing_Factor']

# Step 2: Data Cleaning and Preprocessing
# Drop rows with missing values if any
data_cleaned = data_split.dropna()

# Encode categorical columns
label_encoders = {}
categorical_cols = ['Road_Condition', 'Weather', 'Time_of_Day', 'Contributing_Factor']

for col in categorical_cols:
    le = LabelEncoder()
    data_cleaned[col] = le.fit_transform(data_cleaned[col])
    label_encoders[col] = le

# Convert Date_Time to datetime
data_cleaned['Date_Time'] = pd.to_datetime(data_cleaned['Date_Time'])

# Step 3: Exploratory Data Analysis (EDA)

# Basic statistics
print("Data Summary:")
print(data_cleaned.describe(include='all'))

# Plot accidents by Time_of_Day
plt.figure(figsize=(8,5))
sns.countplot(x='Time_of_Day', data=data_cleaned)
plt.title('Accidents by Time of Day')
plt.show()

# Plot accidents by Road_Condition
plt.figure(figsize=(8,5))
sns.countplot(x='Road_Condition', data=data_cleaned)
plt.title('Accidents by Road Condition')
plt.show()

# Plot accidents by Weather
plt.figure(figsize=(8,5))
sns.countplot(x='Weather', data=data_cleaned)
plt.title('Accidents by Weather')
plt.show()

# Plot accidents by Contributing Factors
plt.figure(figsize=(10,6))
sns.countplot(y='Contributing_Factor', data=data_cleaned,
              order=data_cleaned['Contributing_Factor'].value_counts().index)
plt.title('Accidents by Contributing Factors')
plt.show()
