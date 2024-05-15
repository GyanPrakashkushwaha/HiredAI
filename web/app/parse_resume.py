from pyresparser import ResumeParser
import os

def data(file_name_os):
    file_name = os.path.join("assets/resumes",file_name_os.name)
    data = ResumeParser(resume=file_name).get_extracted_data()
    return data
