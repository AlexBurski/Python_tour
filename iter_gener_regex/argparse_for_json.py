import json
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name", metavar="file_name", type=str)
args = parser.parse_args()
file_name = args.file_name


def json_to_csv(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        for word in data.keys():
            if type(data[word]) == list:
                name = word
                header = list(data[word][0].keys())
        with open('csv_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            for val in data[name]:
                csv_writer.writerow(val.values())


if __name__ == "__main__":
    json_to_csv(file_name)
