#binary_search_algorithm

from selection_sort_algorithm import selection_sort

def binary_search(list_of_numbers , number_to_search):

    #choice = print(int(input("\n\nwhat is the numberto be searhced")))
    length = len(list_of_numbers)
    start_index = 0
    end_index = length - 1

    while start_index <= end_index:
        center = start_index + (end_index - start_index) // 2
        center_val = list_of_numbers[center]

        if center_val == number_to_search:
            return center

        elif center_val < number_to_search:
          start_index = center + 1

        else:
           end_index = center - 1

    return None

#list = [2,3,4,5,6,7,8]
number_to_search = 23


print("in the sorted list : " + str(selection_sort([3,4,5,5,4,3,2,9,6,8,4,6,3,7,1,11,32,23,45,67,76,54,434,23,23,122,89])) + " the number "  + str(number_to_search) + " is at position :" + str(binary_search(selection_sort([3,4,5,5,4,3,2,9,6,8,4,6,3,7,1,11,32,23,45,67,76,54,434,23,23,122,89]), number_to_search)))
                


