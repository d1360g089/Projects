import datetime
from datetime import date
import inflect
import sys

class Age_in_minutes:
    def __init__(self, birth_date):
        self.birth_date = birth_date
        self.today = datetime.date.today()


    def calculate_age_in_mins(self):
        age = (self.today - self.birth_date).days
        age_in_mins = age * 1440
        return age_in_mins


    def convert_to_words(self, number):
        words = inflect.engine()
        return words.number_to_words(number, andword="", group=0)
    
    
    def return_age_in_mins(self):
        age_in_mins = self.calculate_age_in_mins()
        age_in_words = self.convert_to_words(age_in_mins)
        print(f"{age_in_words} minutes")

    
def main():
    try:
        birth_input = input("Date of Birth(YYYY-MM-DD): ")
        birth_date = datetime.datetime.strptime(birth_input, "%Y-%m-%d").date()
        age_to_mins = Age_in_minutes(birth_date)
        age_to_mins.return_age_in_mins() 
        
    except ValueError:
        sys.exit("Invalid Format")

if __name__ == "__main__":
    main()
