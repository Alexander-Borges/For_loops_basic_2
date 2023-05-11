#1
def countdown(n):
    countdown_list = []
    for i in range(n,-1,-1):
        countdown_list.append(i)
    return countdown_list

print(countdown(5))

#2
def print_and_return(numbers):
    print(numbers[0]) #print the first value in the list
    return numbers[1] #return the second value in the list

result = print_and_return([1,2])
print(result)

#3
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

#4
def values_greater_than_second(one):
    if len(one) < 2:
        return False
    
    second_value = one[1]
    new_list = [value for value in one if value > second_value]

    print(len(new_list))
    return(new_list)

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

#5
def length_and_value(size, value):
    return[value]* size

print(length_and_value(4,7))
print(length_and_value(6,2))