from pyresparser import ResumeParser
import os

def data(file_path):
    file_path = os.listdir("assets/resumes")[0]
    file_name = os.path.join("assets/resumes",file_path)
    data = ResumeParser(resume=file_name).get_extracted_data()
    return data
