import pandas as pd
import logging
from functions import generate_unique_email, filter_gender
from constraints import OUTPUT_CSV, OUTPUT_TSV, LOG_FILE

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

# Load the student data
student_data = pd.read_excel('data/Test Files.xlsx')

# Generate unique emails for all students
existing_emails = set()
student_data['Email Address'] = student_data['Student Name'].apply(lambda name: generate_unique_email(name, existing_emails))

# Filter male and female students
male_students = filter_gender(student_data, 'M')
female_students = filter_gender(student_data, 'F')

# Log the number of male and female students
logging.info(f"Number of male students: {len(male_students)}")

logging.info(f"Number of female students: {len(female_students)}")

# Save the processed data
student_data.to_csv(OUTPUT_CSV, index=False)
student_data.to_csv(OUTPUT_TSV, sep='\t', index=False)

# Additional code for shuffling and saving as JSON, JSONL...
