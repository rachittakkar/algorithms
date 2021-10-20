#selection_sort_algorithm

def selection_sort(list_of_numbers):
    length = len(list_of_numbers) - 1

    for i in range(0,length):
        min_value = i
 
        for j in range(i+1 , len(list_of_numbers)):

            if list_of_numbers[j] < list_of_numbers[min_value]:
                
                min_value = j

            if min_value != i:

                list_of_numbers[i], list_of_numbers[min_value] = list_of_numbers[min_value] , list_of_numbers[i]

    return list_of_numbers

#print(selection_sort([3,4,5,5,4,3,2,9,6,8,4,6,3,7,1]))              