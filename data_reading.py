import csv

CROPS_LIST = []
CITIES_LIST = []
COORDINATES_LIST = []
TIME_LIST = []

# reading crops data
with open('data\\crops.csv', 'r') as file1:
    reader1 = csv.DictReader(file1)
    
    for line in reader1:
        crop = line['Crops']
        CROPS_LIST.append(crop)

# reading cities data
with open('data\\cities.csv', 'r') as file2:
    reader2 = csv.DictReader(file2)
    
    for line in reader2:
        city = line['City']
        CITIES_LIST.append(city)

# reading cities coordinates
with open('data\\cities.csv', 'r') as file3:
    reader3 = csv.DictReader(file3)
    
    for line in reader3:
        latitude = line['Latitude']
        longitude = line['Longitude']
        COORDINATES_LIST.append((latitude, longitude))

# reading time
with open('data\\crops.csv', 'r') as file4:
    reader4 = csv.DictReader(file4)
    
    for line in reader4:
        time = line['Time']
        TIME_LIST.append(time)