import pandas as pd
import logging
import json
from functions import generate_unique_email, filter_and_sort_by_gender
from constraints import OUTPUT_CSV, OUTPUT_TSV, LOG_FILE

# Configure logging (Tracking events that happen when the program runs)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

# Load the student data
student_data = pd.read_excel('data/Test Files.xlsx')

# Generate unique emails for all students
existing_emails = set()
student_data['Email Address'] = student_data['Student Name'].apply(lambda name: generate_unique_email(name, existing_emails))

# Sort students: females first, then males
sorted_students = filter_and_sort_by_gender(student_data)

# Log the total number of students and by gender
logging.info(f"Total number of students: {len(sorted_students)}")
logging.info(f"Number of female students: {len(sorted_students[sorted_students['Gender'] == 'F'])}")
logging.info(f"Number of male students: {len(sorted_students[sorted_students['Gender'] == 'M'])}")

# Save the processed data in CSV and TSV formats
sorted_students.to_csv(OUTPUT_CSV, index=False)
sorted_students.to_csv(OUTPUT_TSV, sep='\t', index=False)

# Shuffle the DataFrame (this will only shuffle once as requested)
shuffled_students = sorted_students.sample(frac=1).reset_index(drop=True)

# Convert 'DoB' (Timestamp) to string format for JSON serialization
shuffled_students['DoB'] = shuffled_students['DoB'].apply(lambda x: x.strftime('%Y-%m-%d') if pd.notnull(x) else None)

# Save the shuffled DataFrame as a JSON file
json_output = 'data/shuffled_students.json'
shuffled_students.to_json(json_output, orient='records', indent=4)

# Save the shuffled data as a JSON Lines (JSONL) file
jsonl_output = 'data/output.jsonl'
with open(jsonl_output, 'w') as jsonl_file:
    for idx, row in shuffled_students.iterrows():
        jsonl_record = {
            "id": idx + 1,  # Generating a unique id for each record
            "student number": row['Student Number'],
            "additional details": {
                "dob": row['DoB'],  # This is now a string
                "gender": row['Gender'],
                "special character": any(c for c in row['Student Name'] if not c.isalnum()),  # Checking for special characters in name
                "name similar": row['Email Address'] in existing_emails  # Check for email similarity
            }
        }
        jsonl_file.write(json.dumps(jsonl_record) + '\n')

# Write the updated DataFrame (with emails) back to a new Excel file
output_excel = 'data/Processed_Student_Data.xlsx'
shuffled_students.to_excel(output_excel, index=False)

print("Shuffled data saved as JSON and JSONL files.")
