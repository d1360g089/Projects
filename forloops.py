


import matplotlib.pyplot as plt

# Function to calculate average cost per calendar
def average_cost_per_calendar(N, T, U):
    total_cost = T + N * U
    average_cost = total_cost / N
    return average_cost

# Parameters
total_photo_charge = 710  # one-time charge for using photos
unit_printing_cost = 4.50  # unit cost of printing each calendar

# Range of number of calendars printed
num_calendars_range = range(1, 1001)  # considering up to 1000 calendars

# Calculate average cost for each number of calendars
average_costs = [average_cost_per_calendar(N, total_photo_charge, unit_printing_cost) for N in num_calendars_range]

# Plot
plt.plot(num_calendars_range, average_costs, label='Average Cost per Calendar')
plt.axhline(y=6, color='r', linestyle='--', label='$6 per Calendar')  # Horizontal line at $6 per calendar
plt.xlabel('Number of Calendars Printed')
plt.ylabel('Average Cost per Calendar ($)')
plt.title('Average Cost per Calendar vs. Number of Calendars Printed')
plt.legend()
plt.grid(True)
plt.show()







