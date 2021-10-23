import csv

data = []

with open('bright_stars.csv',"r") as f:
    csv_reader = csv.reader(f)
    for r in csv_reader:
        data.append(r)
        
headers = data[0]
star_data = data[1:]

for data_point in star_data:
    data_point[2]=data_point[2].lower()

star_data.sort(key=lambda star_data:star_data[2])

with open('dwarf_starts.csv',"a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)