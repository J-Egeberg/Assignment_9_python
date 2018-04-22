from common_functions import get_csv_reader

def run(f):
    data = get_csv_reader(f)
    total = 0
    for row in data:
        harro=int(row[2])
        total += harro       
    print("Number of Incidents between 1985-1999 is", total)