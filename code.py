def remove_duplicates(num_arr:list, num_dup: int)->list:
    seen_numbers=set()
    n_of_duplicate = 0
    i = 0

    while n_of_duplicate < num_dup and i < len(num_arr):
        if num_arr[i] in seen_numbers:
            n_of_duplicate+=1
            num_arr.pop(i)
        else:
            seen_numbers.add(num_arr[i])
            i+=1
    return sorted(num_arr, reverse=True)

if __name__=="__main__":
    arr=[1,1,2,2,3,4,5,5,100,4]
    print (remove_duplicates(arr,4))





