numbers_1_to_100 = range(1, 101)

for number in numbers_1_to_100:
    number_is_multiple_of_5 = number % 5 == 0
    number_is_multiple_of_7 = number % 7 ==0

    if number_is_multiple_of_5 and number_is_multiple_of_7:
        print("ChickenMonkey")
    elif number_is_multiple_of_7:
        print("Monkey")
    elif number_is_multiple_of_5:
        print("Chicken")
    else:
        print(number)
