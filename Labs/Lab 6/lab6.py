# -----------------------------------------+
# Ari Osmun                                | 
# CSCI 127, Lab 6                          |
# Last Updated: (10/4/2022)                |
# Name:                                    |
# -----------------------------------------|
# Get states in a population range         |
# -----------------------------------------+


def get_list_from_file(census_data):
    
    census_file = open(census_data, "r")
    states = []
    for one_line in census_file:
        values = one_line.split()
        #print("State: " + values[0] + "\n\tPopulation: " +  values[1] + '\n')
        states.append([values[0],values[1]])
    return states

def get_listing_in_range(lower, upper, state_list):
    
    listing = ""
    count = 0
    
    for i in range(51):
        index = 50 - i
        name = state_list[index][0]
        population = state_list[index][1]
        if (lower < float(population) / 1000000 < upper):
            count += 1
            population = float(population)
            population /= 1000000
            listing += name.ljust(20) + "\t | " + str(round(population,2)) + " million \n"
            
    print(count, " States have a population between ", lower, " and ", upper, " million:")
    return listing
    
def main():
    # TODO: complete the get_list_from_file() function
    states = get_list_from_file("census2020.txt")
    print("\n ***first state in list:", states[0][0], '*** \n') # should be California
    print("The least populous U.S. state: Wyoming with just over 0.5 million")
    print("The most populous U.S. state: California with almost 40 million")
    print("Enter two numbers between 0.5 and 40 to list states in that range.")
    lo = float(input("Enter lower bound: "))
    hi = float(input("Enter upper bound: "))
    
    # TODO: complete the function called get_listing_in_range(); make it a pure function
    # The return value should be a string.
    # Each state and population in that range should appear on its own line,
    # ordered by population from lowest to highest.
    
    listing = get_listing_in_range(lo, hi, states)
    print(listing)
    print("\n ***first state in list:", states[0][0], '*** \n') # should be California

main()
