import pytest 
import seasons
from datetime import datetime
from seasons import Age_in_minutes


        
def test_calculate_age_in_mins():
    birth_date = datetime.strptime("2000-01-01", "%Y-%m-%d").date()
    age_in_mins_distance = Age_in_minutes(birth_date)
    calculated_mins = age_in_mins_distance.calculate_age_in_mins()
    today = datetime.today().date()
    expected_days = (today - birth_date).days
    expected_minutes = expected_days * 1440
    assert calculated_mins == expected_minutes
    
def test_convert_to_words():
    age_in_minutes_instance = Age_in_minutes(datetime.today().date())
    number = 123456
    words = age_in_minutes_instance.convert_to_words(number)
    assert words == "one hundred twenty-three thousand, four hundred fifty-six"








if __name__ == "__main__":
    pytest.main()

