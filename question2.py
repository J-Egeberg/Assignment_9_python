from common_functions import get_csv_reader

def run(f):
    data = get_csv_reader(f)
    total = 0
    for row in data:
        harro=int(row[3])
        total += harro       
    print("Number of Fatal Accidents between 1985-1999 is", total)