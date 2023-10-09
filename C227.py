import json
import csv

data_from_csv = []

with open('data_set.txt', 'r') as f:
     data_from_txt = json.loads(f.read())

field_names = ['throttle', 'steer', 'brake', 'hand_brake']
csvfilestore = open('project-227.csv', 'w', newline = '')
writer = csv.DictWriter(csvfilestore, fieldnames = field_names)
writer.writeheader()
writer.writerows(data_from_txt)

with open('C227.csv', 'r') as file:
	reader = csv.reader(file)

	for row in reader:
		data_from_csv.append(row)

print(data_from_csv)