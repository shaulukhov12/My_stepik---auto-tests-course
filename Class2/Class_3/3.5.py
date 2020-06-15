import csv
from collections import Counter

with open('Crimes.csv') as file:
    reader = csv.reader(file)
    data = list(reader)[1:]
    crimes = list(zip(*data))[5]
    crime_counts = Counter(crimes)
    print(crime_counts.most_common(1))