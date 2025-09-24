# 🚦 Traffic Accident Data Analysis

## 📋 Overview
This project analyzes traffic accident data to identify patterns related to road conditions, weather, and time of day. The goal is to understand contributing factors and visualize accident hotspots using geographical coordinates. This analysis aims to provide insights that can help improve road safety and accident prevention strategies.

## 📊 Dataset
The dataset contains records of traffic accidents with the following key features:
- 🆔 Accident_ID: Unique identifier for each accident
- 🕒 Date_Time: Timestamp of the accident
- 🛣️ Road_Condition: Condition of the road at the time of the accident
- ☁️ Weather: Weather conditions during the accident
- 🌅 Time_of_Day: Time category such as Morning, Afternoon, Evening, Night
- 📍 Latitude & Longitude: Geographical location of the accident
- 🚧 Contributing_Factor: Primary factor contributing to the accident (e.g., poor visibility, speeding)

## 🧹 Data Cleaning and Preprocessing
- Data was initially loaded from an Excel file with combined columns.
- Columns were split, renamed, and rows with missing values were dropped.
- 🔤 Categorical variables were encoded for analysis.
- 📅 Date_Time was converted to proper datetime format for temporal analysis.

## 📈 Analysis and Visualization
- Distribution of accidents by Time of Day, Road Condition, and Weather.
- 📍 Identification and visualization of accident hotspots using Latitude and Longitude.
- ⚠️ Most common contributing factors to accidents were identified and visualized.
- Visualizations include bar charts for categorical distributions and scatter plots for geographical hotspots.

## 🛠️ Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn
- scikit-learn

## ▶️ How to Run
1. Clone the repository
2. Install the required packages:  
   `pip install pandas matplotlib seaborn scikit-learn`
3. Run the analysis script (e.g., `traffic_accident_analysis.py`)
4. View the generated plots and analysis output

## 👤 Author
Deepika P
Intern at SkillCraft Technology

---
