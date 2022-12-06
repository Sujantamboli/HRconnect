from my_utils.csv import HandleCSV


if __name__ == "__main__":
    filename = "employee.csv"

    f = HandleCSV()
    lst = f.read_string_to_dict()
    # print(lst)

    dict1 = {}
    for foo in lst:
        if int(foo["SALARY"]) > 9000:
            full_name = foo["FIRST_NAME"] + " " + foo["LAST_NAME"]
            email = foo["EMAIL"]
            phone_number = foo["PHONE_NUMBER"]
            dict1.update({"name": full_name})
            dict1.update({"email": email})
            dict1.update({"phone_number": phone_number})
            print(dict1)



