def binary_search(lst, number_to_find):
    
    while True:
        middle = round(len(lst) / 2) 
        
        
        if len(lst) == 1 and middle != number_to_find:
            return False
        if lst[middle] == number_to_find:
            return True
            break
            
        elif lst[middle] > number_to_find:
            del lst[middle:]
            
        elif lst[middle] < number_to_find:
            del lst[:middle]
        
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
binary_search(lst, 7)
