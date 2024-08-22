import os
import re

# Define the source and destination directories
source_directory = '09-08'
#source_dir_name = os.path.basename(source_directory) 
destination_directory = os.path.join('6 to 12 cleaned mmlb data', source_directory)

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Function to split the values into groups of 900 and create new INSERT statements
def split_insert_values(content, max_values=900):
    # Use regex to find the INSERT statements
    pattern = re.compile(r"INSERT INTO [^\(]*\(([^)]+)\) VALUES \(([^;]+)\);", re.IGNORECASE)
    matches = pattern.finditer(content)
    new_content = ""
    for match in matches:
        columns = match.group(1)
        values_str = match.group(2)
        # Split the values by '), ('
        all_values = re.split(r"\), \(", values_str)
        # Group the values into chunks of 900
        for i in range(0, len(all_values), max_values):
            values_chunk = all_values[i:i + max_values]
            # Join the chunk of values and format them into a new INSERT statement
            new_values_str = '),\n('.join(values_chunk)
            if i > 0:
                new_values_str = '(' + new_values_str
            if i + max_values < len(all_values):
                new_values_str = new_values_str + '),'
            new_insert_statement = f"INSERT INTO dbt_data ({columns}) VALUES\n({new_values_str});\n"
            new_content += new_insert_statement

    # Replace '(( with '(' and '),); with ');'
    new_content = new_content.replace('((', '(')
    new_content = new_content.replace('),);', ');')
    return new_content

# Loop through each file in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('.sql'):
        # Read the content of the SQL file
        with open(os.path.join(source_directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Split the INSERT values and create new INSERT statements
        new_content = split_insert_values(content)
        
        # Write the new content to a file in the destination directory
        with open(os.path.join(destination_directory, filename), 'w', encoding='utf-8') as new_file:
            new_file.write(new_content)

print("SQL files have been processed and saved to the new folder.")
