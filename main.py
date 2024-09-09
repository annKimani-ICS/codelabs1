import pandas as pd
import logging
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

# Print success message for verification
print(f"Data processing complete. Files saved as '{OUTPUT_CSV}' and '{OUTPUT_TSV}'")

# Additional code for shuffling and saving as JSON, JSONL...