#Я предлагаю быстрый поиск, так как он имеет средний случай как O(n log n) 


def quicksort(array):

    if len(array) <= 1:
        return array
        
    pivot = array[len(array) // 2]
    left = [i for i in array if i < pivot]
    middle = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]

    return quicksort(left) + middle + quicksort(right)

#Я считаю, что данная функция подходит, так как она достаточно быстра и надежна, а ее худший
# случай происходит только если опорным элементом выступает крайний элемент, что в данном случае
# мзбегается. Это хороший классический метод, время которого не сильно растет по мере увеличения данных в массиве,
# который надо отсортировать.