numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even+=1
    else:
	    count_odd+=1
print("Кол-во четных чисел: ",count_even)
print("Кол-во нечетных чисел: ",count_odd)


