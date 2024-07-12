# importing the required modules
import glob
import pandas as pd
import os

# specifying the path to csv files
path = 'C:\\Users\\YQ417FW\\Downloads\\Sindhudurga\\test'

# csv files in the path
file_list = glob.glob(os.path.join(path, "*.csv"))


# list of excel files we want to merge.
# pd.read_excel(file_path) reads the excel
# data into pandas dataframe.
li = []
print(li)

for file in file_list:
	df = pd.read_csv(file, index_col=None, header=0, encoding = "utf-8")
	print(file)
	li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv('combinedSindh.csv', index = True)

print('Done')