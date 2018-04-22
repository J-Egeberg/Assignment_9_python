from common_functions import get_csv_reader

def run(f):
    data = get_csv_reader(f)
    total = 0
    for row in data:
        harro=int(row[5])
        total += harro       
    print("Number of Incidents between 2000-2014 is", total)