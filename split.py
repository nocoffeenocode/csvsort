## Import pandas
import pandas as pd
import os
 
 
"""
df = pd.read_csv(split_source_file, header=0, delimiter=",")
DtypeWarning: Columns (2) have mixed types. Specify dtype option on import or set low_memory=False.
 
"""
## Provide the File Name
#split_source_file = 'z_flights_info.csv'
#split_source_file = 'MJPSKY_PORTAL_USER_LIST.csv'
#split_source_file = 'SavingsAccountData.csv'
#split_source_file = '20220714_UP_Beneficiary_Mapping_v4.csv'
#split_source_file = 'UP_Test_v2.csv'
#split_source_file = 'Chattisgarh_Land_Data_Uploaded_Accepted.csv'

split_source_file ='combinedSindh.csv'
## Create a Pandas data frame
df = pd.read_csv(split_source_file, header=0, delimiter=",")
print(df.head())
## Extract only the columns of the DataFrame
columns = df.columns.values.tolist()
 
## Convert Columns into upper case (pandas way of doing it)
columns_list = list(pd.Series(columns).str.upper())
 
## Ask user to provide a column to split
column_choosen = input(f"Which column to choose to split file? type in: {columns} ?:")
 
## Loop in until user provides a right column name
while True:
    ## Check if the column typed in by user is actually in the column list
    if column_choosen.upper() in (columns_list):
        ## Find the index value of the column
        indx_val = columns_list.index(column_choosen.upper())
 
        ## Take the column to split from the actual column names of data frame
        column_to_split = columns[indx_val]
 
        ## Indicate how many sub files this programming is going to create
        proceed = input(
            f"This code splits the CSV into {df.nunique()[column_to_split]} parts? want to proceed? yes / no: ")
        if proceed.upper() == 'YES':
            ## Find unique values from the column
            unique_values = df[column_to_split].unique()
 
            ## Loop through all unique values
            for label in unique_values:
                ## Create another sub data frame using the value for the value of the column each time
                df_label = df[df[column_to_split] == label]
                ## Define target File name
                split_target_file = f"{split_source_file.replace('*.csv', '')}_{label}.csv"
 
                ## Write to the file using pandas to_csv
                df_label.to_csv(split_target_file, index=False, header=True, mode='a')
            break
    else:
        column_choosen = input(f"Which column to choose to split file? type in: {columns} ?")