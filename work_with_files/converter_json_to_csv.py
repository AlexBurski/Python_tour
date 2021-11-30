import json
import csv


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


json_to_csv('json_data.json')


"""
JSON

{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers":  "Radiation resistance"
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers":  "Million tonne punch"
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers":  "Immortality"
    }
  ]
}


to 


name,age,secretIdentity,powers
Molecule Man,29,Dan Jukes,Radiation resistance
Madame Uppercut,39,Jane Wilson,Million tonne punch
Eternal Flame,1000000,Unknown,Immortality

"""