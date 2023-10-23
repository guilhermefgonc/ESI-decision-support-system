import csv

CROPS_LIST = []
CITIES_LIST = []

# reading crops data
with open('data.csv', 'r') as file1:
    reader1 = csv.DictReader(file1)
    
    for line in reader1:
        crop = line['Crops']
        CROPS_LIST.append(crop)

CROPS_LIST = '\n'.join(CROPS_LIST)

with open('cities.csv', 'r') as file2:
    reader2 = csv.DictReader(file2)
    
    for line in reader2:
        city = line['City']
        CITIES_LIST.append(city)

CITIES_LIST = '\n'.join(CITIES_LIST)