#bubble_sort_algorithm

def bubble_sort(list_of_numbers):
    length = len(list_of_numbers) - 1
    is_sorted = False

    while is_sorted != True:
        is_sorted = True

        for i in range(0,length):
            
            if list_of_numbers[i] > list_of_numbers[i+1]:
               list_of_numbers[i] , list_of_numbers[i+1] = list_of_numbers[i+1] , list_of_numbers[i]
               is_sorted = False

    return list_of_numbers

print(bubble_sort([3,4,5,5,4,3,2,9,6,8,4,6,3,7,1]))           