import pandas as pd
import os

# Set your local path to the training CSV files and label file
csv_dir = 'cases'  # or your own local path
label_file = 'labels.xlsx'

# Load the labels Excel file
labels_df = pd.read_excel(label_file, skiprows=1)  # Skip the merged header row

# Clean up the label DataFrame
labels_df = labels_df.rename(columns={
    'Case#': 'case_id',
    'Spacecraft#': 'spacecraft',
    'Condition': 'condition',
    'Solenoid valves': 'SV1',
    'Unnamed: 4': 'SV2',
    'Unnamed: 5': 'SV3',
    'Unnamed: 6': 'SV4',
    'Bubble': 'BP1',
    'Unnamed: 8': 'BP2',
    'Unnamed: 9': 'BP3',
    'Unnamed: 10': 'BP4',
    'Unnamed: 11': 'BP5',
    'Unnamed: 12': 'BP6',
    'Unnamed: 13': 'BP7',
    'Unnamed: 14': 'BV1'
})

# Drop rows with no case ID
labels_df = labels_df.dropna(subset=['case_id'])

# Convert case_id to integer and format file name
labels_df['case_id'] = labels_df['case_id'].astype(int)
labels_df['filename'] = labels_df['case_id'].apply(lambda x: f"Case{x:03d}.csv")

# Load all CSVs and store in a dictionary
data_dict = {}
for i, row in labels_df.iterrows():
    filepath = os.path.join(csv_dir, row['filename'])
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        data_dict[row['filename']] = {
            'data': df,
            'label': row
        }
