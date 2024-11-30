import pandas as pd
import json


filepath = "C:/Users/iyash/Downloads/prompt_data.xlsx"

excel_data = pd.read_excel(filepath)

cleaned_data = excel_data.dropna(how='all')
required_fields = ["Course Name(Doctorate/PhD)", "University/Institute (Doctorate/PhD)", "Duration (Doctorate/PhD)", "Specialization (Doctorate/PhD)", "Course Type (Doctorate/PhD)","Grade (Doctorate/PhD)", "Course Name (Masters/Post-Graduation)", "University/Institute (Masters/Post-Graduation)","Duration (Masters/Post-Graduation)","Specialization (Masters/Post-Graduation)","Course Type (Masters/Post-Graduation)","Grade (Masters/Post-Graduation)", "Course Name(Graduation/Diploma)", "University/Institute (Graduation/Diploma)", "Duration (Graduation/Diploma)", "Specialization (Graduation/Diploma)", "Course Type (Graduation/Diploma)", "Grade (Graduation/Diploma)", "Board (12th)", "Passing Out Year (12th)", "School medium (12th)", "Marks (12th)", "English marks (12th)", "Maths marks (12th)", "Board (10th)", "Passing Out Year (10th)", "School medium (10th)", "Marks (10th)", "Summary", "Work Experience", "Skills", "Personal Projects", "Certificates"," Interests"]
for field in required_fields:
    if field not in cleaned_data.columns:
        cleaned_data[field] = None
json_data = cleaned_data.to_dict(orient = 'records')
output_file_path = "C:/Users/iyash/Downloads/output.json"

with open(output_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
print(f"JSON data saved as {output_file_path}")

