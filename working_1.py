import re 

def main():

    hours_input = input("Hours: ").upper().strip()
    print(convert(hours_input))

def convert(hours):
    pattern = r"(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    if working_time := re.search(r"^" + pattern + " TO " + pattern + "$", hours):
        start_time = convert_to_military(working_time.group(1), working_time.group(2), working_time.group(3))
        end_time = convert_to_military(working_time.group(4), working_time.group(5), working_time.group(6))

        return f"{start_time} to {end_time}"
    else:
        raise ValueError

def convert_to_military(hr, mins, am_pm):
    if hr == "12":
        if am_pm == "AM":
            hour = "00"

        else:
            hour = "12"
    else:
        if am_pm == "AM":
            hour = f"{int(hr):02}"
        elif am_pm == "PM":
            hour = f"{int(hr)+12}"
    
    if mins == None:
        minutes = "00"
    else:
        minutes = f"{int(mins):02}"
    return f"{hour}:{minutes}"

if __name__ == "__main__":
    main()
