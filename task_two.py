from my_utils.csv import HandleCSV
from datetime import datetime

if __name__ == "__main__":
    filename = "employee.csv"

    bar = HandleCSV()
    lst = bar.read_string_to_dict()
    # print(f"{lst}/n")

    dict1 = {}
    for foo in lst:
        if 30 < int(foo["DEPARTMENT_ID"]) < 110 and int(foo["SALARY"]) > 4200:
            full_name = foo["FIRST_NAME"] + " " + foo["LAST_NAME"]
            date_hire = foo["HIRE_DATE"]
            detail = datetime.strptime(date_hire, "%d-%b-%y")
            date = detail.date()
            date = str(date)
            # print(date)
            dict1[date] = [full_name]
    print(dict1)
