numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
list_1 = numbers[:4]
list_2 = numbers[5:]
skip_five = list_1 + list_2
sum =  sum(skip_five)
count = len(numbers)
average = round(sum/count,2)
numbers[4] = average
print("Измененный список:", numbers)
