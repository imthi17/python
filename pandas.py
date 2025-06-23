import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('your_dataset.csv')  # Replace with your file path

# Display basic info
print(df.info())

# Handling missing values
# Fill missing numeric values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill missing categorical values with mode
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Encode categorical variables using Label Encoding
label_encoder = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = label_encoder.fit_transform(df[col])

# Feature scaling (Standardization)
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Rename columns (optional)
df.rename(columns=lambda x: x.strip().lower().replace(' ', '_'), inplace=True)

# Drop irrelevant columns (example: 'id' column)
if 'id' in df.columns:
    df.drop('id', axis=1, inplace=True)

# Final dataset preview
print(df.head())
