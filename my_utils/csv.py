import csv


class HandleCSV:
    filename = "employee.csv"

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            return foo.readlines()

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()

    @classmethod
    def read_string_to_dict(cls):
        lst = []
        with open(cls.filename, mode='r') as f:
            data = csv.DictReader(f)
            for row in data:
                lst.append(dict(row))
        return lst




