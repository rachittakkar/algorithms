#quick_sort_algorithm

def quick_sort(list_of_numbers):
    length = len(list_of_numbers)
    
    if length <= 1:
        return list_of_numbers
    else:
        center = list_of_numbers.pop()

    larger_values = []
    smaller_values = []

    for values in list_of_numbers:

        if values > center:
            larger_values.append(values)
        else:
            smaller_values.append(values)

    return quick_sort(smaller_values) + [center] + quick_sort(larger_values)                

print(quick_sort([3,4,5,5,4,3,2,9,6,8,4,6,3,7,1]))
