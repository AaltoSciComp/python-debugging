# This script will cause a divide by zero error


def sum(numbers):
    result = 0
    for n in numbers:
        result += n
    return result


def calc_average(numbers):
    enum = sum(numbers)
    denom = len(numbers)
    return enum / denom


def conditional_averages(numbers):
    '''
    Calculate the averages with a diminishing subset of the numbers.
    I.e. exclude the numbers one by one, starting from the first number.
    
    Return the conditional averages of the subsets. (Length equals len(numbers))
    '''

    copy = list(numbers)
    averages = []

    for i in range(len(numbers)):
        average = calc_average(copy)
        averages.append(average)
        # The original skips the first number completely.
        # It should be removed after calculating the average.
        copy = copy[1:]

    return averages


numbers = [1, 2, 3, 4]

averages = conditional_averages(numbers)

print(averages)

