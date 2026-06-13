import csv

def get_data(path):
    final_list = []

    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")

        next(reader)

        for row in reader:
            final_list.append(row)

    return final_list