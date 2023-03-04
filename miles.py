#Employee A: 15.62 miles
Employee_A_Distance = 15.62
Employee_A_times = input()
Employee_A_total_distance = float(Employee_A_times) * float(Employee_A_Distance) 
#Employee_A_total_distance_rounded = round(Employee_A_total_distance, 2)
#print(Employee_A_total_distance)

#Employee B: 41.85 miles
Employee_B_Distance = 41.85
Employee_B_times = input()
Employee_B_total_distance = float(Employee_B_times) * float(Employee_B_Distance)
#Employee_B_total_distance_rounded = round(Employee_B_total_distance, 2)
#print(Employee_B_total_distance)

#Employee C: 32.67 miles
Employee_C_Distance = 32.67

Employee_C_times = input()
Employee_C_total_distance = float(Employee_C_times) * float(Employee_C_Distance)
#Employee_C_total_distance_rounded = round(Employee_C_total_distance, 2)
#print(Employee_C_total_distance)

total_miles_traveled = float(Employee_A_total_distance) + float(Employee_B_total_distance) + float(Employee_C_total_distance)
#total_miles_traveled = "Distance: " + str(float(Employee_A_total_distance) + float(Employee_B_total_distance) + float(Employee_C_total_distance)) + " miles"
total_miles_traveled_rounded = round(float(total_miles_traveled), 2)
total_miles_traveled_rounded_2d = "{:.2f}".format(total_miles_traveled_rounded)
output = "Distance: " + str(total_miles_traveled_rounded) + " miles"
print(output)
