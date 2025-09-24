import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Step 1 & 2: Load and clean/preprocess data
file_path = 'Accident_dataset.xlsx'
data = pd.read_excel(file_path)

# Split combined column into proper columns
data_split = data[data.columns[0]].str.split(',', expand=True)
data_split.columns = ['Accident_ID', 'Date_Time', 'Road_Condition', 'Weather', 'Time_of_Day',
                      'Latitude', 'Longitude', 'Contributing_Factor']

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

# Step 3: EDA (Optional - can omit if only Step 4 needed)
print("Data Summary:")
print(data_cleaned.describe(include='all'))

# Step 4: Identify Hotspots and Contributing Factors

# Group accidents by Latitude and Longitude for hotspots
location_counts = data_cleaned.groupby(['Latitude', 'Longitude']).size().reset_index(name='Accident_Count')
location_counts['Latitude'] = pd.to_numeric(location_counts['Latitude'])
location_counts['Longitude'] = pd.to_numeric(location_counts['Longitude'])

plt.figure(figsize=(10,6))
sns.scatterplot(x='Longitude', y='Latitude', size='Accident_Count', sizes=(20, 200),
                alpha=0.6, data=location_counts)
plt.title('Accident Hotspots by Location')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Accident Count', loc='upper right')
plt.show()

# Decode contributing factors back to labels for plotting
if 'Contributing_Factor' in label_encoders:
    le_factor = label_encoders['Contributing_Factor']
    factor_labels = le_factor.inverse_transform(data_cleaned['Contributing_Factor'])
else:
    factor_labels = data_cleaned['Contributing_Factor']

data_cleaned['Contributing_Factor_Label'] = factor_labels

plt.figure(figsize=(10,6))
sns.countplot(y='Contributing_Factor_Label', data=data_cleaned,
              order=data_cleaned['Contributing_Factor_Label'].value_counts().index)
plt.title('Top Contributing Factors to Accidents')
plt.show()
