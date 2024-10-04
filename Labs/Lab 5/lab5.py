
def main():
    #GEt input string, turn it into array
    user_nums = input("Enter some integers: ")
    num_list = user_nums.split(" ")
    #Turn list objects into integers
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    #Get Bounds
    user_lo = int(input("Lower bound: "))
    user_hi = int(input("Upper bound: "))
    #Get new array from bounds
    make_int_list(num_list, user_lo, user_hi)
    print("Lower bound: ", user_lo)
    print("Upper bound: ", user_hi)
    print("Original List: ", num_list)
    print("Filtered List: ", make_int_list(num_list, user_lo, user_hi))
    print("Shrunken Array: ", str(shrink_array(num_list, user_lo, user_hi)))
    

def make_int_list(num_list, user_lo, user_hi):
    filtered = []
    for i in range(len(num_list)):
        if(num_list[i] >= user_lo) and (num_list[i] <= user_hi):
            filtered.append(num_list[i])
    return filtered 

def shrink_array(num_list, user_lo, user_hi):
    temp = []
    count = user_lo
    while (count <= user_hi and count != len(num_list)):
        temp.append(num_list[count])
        count += 1
    return temp


main()