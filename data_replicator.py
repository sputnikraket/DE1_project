import pandas as pd
replicFactor = 11600 #makes it 4GB

input_csv_path = "Data_to_replicate.csv"

#csv to pandas
original_df = pd.read_csv(input_csv_path)

replicated_df = pd.concat([original_df] * replicFactor, ignore_index=True)

output_csv_path = "replicated_Data_4GB.csv"

# Write the replicated DataFrame to a new CSV file
replicated_df.to_csv(output_csv_path, index=False)

print(f"Rows replicated successfully. Output saved to: {output_csv_path}")