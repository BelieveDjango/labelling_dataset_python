import csv

# Specify the path to the input CSV file
input_file_path = "D:\DataSet\sessions.csv"

# Specify the path to the output CSV file
output_file_path = "D:\DataSet\sessions_out.csv"

# Data types for users to choose from
data_type_options = ["integer", "float", "string"]

# Prompt for column headers and corresponding data types
column_headers = []
data_types = []

while True:
    header = input("Enter the column header (or 'done' to finish): ")
    if header.lower() == "done":
        break
    column_headers.append(header)

    # Prompt for the data type
    while True:
        print("Available data types:")
        for i, data_type in enumerate(data_type_options, start=1):
            print(f"{i}. {data_type}")
        data_type_choice = input(f"Enter the data type for '{header}': ")
        if data_type_choice.isdigit() and 1 <= int(data_type_choice) <= len(data_type_options):
            data_type = data_type_options[int(data_type_choice) - 1]
            break
        else:
            print("Invalid input. Please select a valid data type.")

    data_types.append(data_type)

# Open the input CSV file and read its contents
with open(input_file_path, "r") as input_file:
    reader = csv.DictReader(input_file)

    # Create a new list of dictionaries to hold the modified rows
    modified_rows = []

    # Iterate over each row in the input CSV file
    for row in reader:
        modified_row = row.copy()
        for header, data_type in zip(column_headers, data_types):
            value = modified_row[header]
            if data_type == "integer":
                value = int(value)
            elif data_type == "float":
                value = float(value)
            elif data_type == "string":
                value = str(value)
            modified_row[header] = value

        # Check the conditions to label the traffic as "Malicious" Add as much column as possible below
        if (
            modified_row["column1"] == "***"
            and modified_row["column2"] == "***"
            and modified_row["column3] == "****"
            and int(modified_row["column4"]) > 10
        ):
            label = "Malicious"     #Set the name of the attack, eg. DoS, Scanning, Malware etc. 
        else:
            label = ""

        # Add the label to the modified row
        modified_row["Label"] = label

        # Append the modified row to the list
        modified_rows.append(modified_row)

# Write the modified rows to the output CSV file
with open(output_file_path, "w", newline="") as output_file:
    fieldnames = reader.fieldnames + ["Label"]  # Include the existing columns and the new "Label" column in the fieldnames
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(modified_rows)

print(f"Labeled traffic written to: {output_file_path}")
