numbers_to_strings = {
    'one':   1,
    'two':   2,
    'three': 3,
    'four':  4,
    'five':  5,
    'six':   6,
    'seven': 7,
    'eight': 8,
    'nine':  9
}


def calculate_line_sum(string: str):
    if len(string) == 0:
        return 0

    # a dictionary containing the indexes of found numbers and the int values of the numbers
    found_numbers = {}

    # get all of the numbers in the string
    for i, ch in enumerate(string):
        if ch.isdigit():
            found_numbers[i] = int(ch)

    # get all of the words in the string
    for str_number in numbers_to_strings.keys():
        if str_number in string:
            # find all indexes of str_number in string
            index = 0
            while (index := string.find(str_number, index)) != -1:
                found_numbers[index] = numbers_to_strings[str_number]
                index += 1

    if len(found_numbers) == 0:
        return 0

    min_index = min(found_numbers.keys())
    max_index = max(found_numbers.keys())

    print(sorted(found_numbers.items()))

    return found_numbers[min_index]*10 + found_numbers[max_index]


def resolve_part2(file):
    sum = 0

    with open(file, 'r') as f:
        for line in f:
            to_add = calculate_line_sum(line.strip())
            sum += to_add
            print(f'{line.strip()} -> {to_add}')

    return sum


if __name__ == '__main__':
    # calculate test file sum
    test_sum = resolve_part2('part2_test.txt')

    # test sum value
    assert test_sum == 281
