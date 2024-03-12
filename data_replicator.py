import pandas as pd
replicFactor = 25
# Replace 'input_csv_path' with the path to your input CSV file
input_csv_path = "replicated_Data_x100.csv"

# Read the CSV file into a Pandas DataFrame
original_df = pd.read_csv(input_csv_path)

# Replicate each row 100 times
replicated_df = pd.concat([original_df] * replicFactor, ignore_index=True)

# Replace 'output_csv_path' with the desired path for the output CSV file
output_csv_path = f"replicated_Data_x{str(replicFactor*100)}.csv"

# Write the replicated DataFrame to a new CSV file
replicated_df.to_csv(output_csv_path, index=False)

print(f"Rows replicated successfully. Output saved to: {output_csv_path}")