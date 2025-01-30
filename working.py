import re 

def main():

    hours_input = input("Hours: ").upper()
    print(convert(hours_input))

def convert(hours):
    pattern = r"(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    if working_time := re.search(r"^" + pattern + " TO " + pattern + "$", hours):
        start_time = working_time.group(0).split(" TO ")[0].strip()
        end_time = working_time.group(0).split(" TO ")[1].strip()

        
        
        start_military = convert_to_military(start_time)
        end_military = convert_to_military(end_time)
        return f"{start_military} to {end_military}"
    else:
        raise ValueError

def convert_to_military(time):
    time_part = time[:2]
    am_pm = time[2:]

    parts = time_part.split(":")
    hour = int(parts[0])
    minutes = int(parts[1])
    mins = None


    if am_pm.upper() == "AM":
        if hour == 12:
            hour = 0
        else:
            hour = 12
    else:
        if hour > 12:
            hour += 12
    if mins == None:
        minutes = 00


    return f"{int(hour):02}:{int(minutes):02}"
            



if __name__ == "__main__":
    main()
