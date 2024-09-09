import re
import pandas as pd

# Function to generate email addresses based on student names
def generate_email(name):
    cleaned_name = re.sub(r"[^\w\s]", '', name)
    names = cleaned_name.split()

    if len(names) == 1:
        email = f"{names[0].lower()}@gmail.com"
    elif len(names) == 2:
        first_initial = names[0][0].lower()
        last_name = names[1].lower()
        email = f"{first_initial}{last_name}@gmail.com"
    else:
        first_initial = names[0][0].lower()
        last_name = names[-1].lower()
        email = f"{first_initial}{last_name}@gmail.com"

    return email

# Function to generate unique email addresses
def generate_unique_email(name, existing_emails):
    base_email = generate_email(name)
    unique_email = base_email
    counter = 1
    while unique_email in existing_emails:
        unique_email = f"{base_email.split('@')[0]}{counter}@gmail.com"
        counter += 1
    existing_emails.add(unique_email)
    return unique_email

# Function to sort by gender: females first, then males
def filter_and_sort_by_gender(data):
    females = data[data['Gender'] == 'F']
    males = data[data['Gender'] == 'M']
    # Concatenate females first, then males
    return pd.concat([females, males], ignore_index=True)
