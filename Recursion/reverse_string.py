import array



def array_reverse(some_array):
    if len(some_array) == 0:
        answer = some_array
    else:
        answer = array_reverse(some_array[1:]) + some_array[:1]
    return answer


def list_reverse(some_list):
    if some_list == []:
        answer = []
    else:
        answer = list_reverse(some_list[1:]) + [some_list[0]]
    return answer



def string_reverse(some_string):
    print("Start", some_string)
    if some_string == "":   #Base case
        answer = "" 
    else:                   #General case
        answer = string_reverse(some_string[1:]) + some_string[0]
    print("end", answer)
    return answer

def towerOfHanoi(disks, start, middle, finish):
    
    if disks > 0:
        towerOfHanoi(disks-1, start, finish, middle) 
        print("Move disk", disks, "from", start, "to", finish)
        towerOfHanoi(disks-1, middle, start, finish)
    

#print(string_reverse("mississippi"))
print(list_reverse([1, 2, 3, 4, 5, 6]))
election_years = array.array('i', [2004, 2008, 2012, 2016, 2022])

#print(array_reverse(election_years))

#print(towerOfHanoi(8, 'a', 'b', 'c'))