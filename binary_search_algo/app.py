def binary_search(my_list, element):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == element:
            return mid
        if guess > element:
            high = mid - 1
        else:
            low = mid + 1
    return None


l = [1, 3, 5, 7, 9]

print(binary_search(l, 3))  # => 1
