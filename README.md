# Student Data Processor

This Python project processes student data from an Excel file, generates unique email addresses for each student, sorts students by gender (with females listed first), and saves the results in multiple formats including CSV, TSV, Excel, JSON, and JSON Lines (JSONL). Additionally, the script logs key statistics about the processed data.

## Features
- **Generate Unique Emails**: Each student is assigned a unique email address based on their name.
- **Sort by Gender**: Students are sorted so that all female students appear first, followed by male students.
- **Save Data in Multiple Formats**: Processed data is saved in CSV, TSV, Excel, JSON, and JSONL formats.
- **Shuffle Data**: The student data is shuffled before saving in JSON and JSONL formats.
- **Log Processing Information**: Key information, such as the total number of students and gender breakdown, is logged for auditing purposes.


## Requirements
- Python 3.7 or later
- Required Python packages:
  - pandas
  - openpyxl

You can install the required dependencies by running:
```bash
pip install pandas openpyxl
```

##to run
```
python main.py
```

