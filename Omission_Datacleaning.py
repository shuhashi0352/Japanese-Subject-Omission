import pandas as pd

# Load the data
data = pd.read_csv("Tweets.csv")

# Define columns to check (excluding 'tokens')
columns_to_check = [col for col in data.columns if col != 'tokens']

# Drop rows where all specified columns are empty
filtered_data = data.dropna(how='all', subset=columns_to_check)

# Save the cleaned data to a new CSV file
filtered_data.to_csv("cleaned_output.csv", index=False)
print("Rows with empty values (except 'tokens') removed. Saved as 'cleaned_output.csv'.")
