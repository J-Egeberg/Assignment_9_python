from common_functions import get_csv_reader

def run(f):
    ninety = 402
    twothousand = 231
    difference = ninety-twothousand
    print("Number of incidents from 1885-1999 was", ninety)
    print("Number of incidents from 2000-2014 was", twothousand)
    print("This means that there was a decrease of incidents by", difference)