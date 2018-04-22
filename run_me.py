import question1
import question2
import question3
import question4
import question5
from file_handler import download_csv_sheet


def run():
    csv_sheet_name = 'data.csv'
    url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv'
    download_csv_sheet(csv_sheet_name, url)
    with open(csv_sheet_name, encoding='utf-8') as f:
        print_question_separator('1. How many incidents happened between 1985-1999?')
        question1.run(f)

        print_question_separator('2. How many death-incidents happened between 1985-1999?')
        question2.run(f)

        print_question_separator('3. How many incidents happened between 2000-2014?')
        question3.run(f)

        print_question_separator('4. How many death-incidents happened between 2000-2014?')
        question4.run(f)

        print_question_separator('5. Has the amount of incidents increased, comparing the later statistics to the earlier ones?')
        question5.run(f)

def print_question_separator(question_number):
    print('\nQuestion ' + str(question_number), end='\n' + 100 * '-' + '\n')


run()
# It is really bugging me that you have to define function before you call it, so I wrapped everything in run()
# Thanks to that I can order functions as they are called, so you can read code from top to bottom
