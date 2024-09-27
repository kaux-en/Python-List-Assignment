#Advanced Slicing Techniques

#Task 1:Given the list of temperatures
temps = [72,75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = slice(7,14)
print(temps[second_week])

#Task 2: Extract all the temperatures above 100
slice_temps = slice(23,30)
high_temps = temps[slice_temps]
print(high_temps)