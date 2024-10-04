census_file = open("census2020.txt", "r")

print(type(census_file))
total = 0
for one_line in census_file:
    values = one_line.split()
    total += int(values[1])
    print("State: " + values[0] + "\n\tPopulation: " +  values[1] + '\n')
print("total population: ", total)
census_file.close()  
