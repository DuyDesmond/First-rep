test_list = [1, 8, 2, 7, 2]

def average_of_list(input_list):
    sum = 0
    for i in range(len(input_list)):
        sum += input_list[i]
    average = sum / len(input_list)
    return average

print(average_of_list(test_list))


    
    