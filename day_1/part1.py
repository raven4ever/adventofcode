def calculate_line_sum(string):
    first = 0
    last = 0

    for ch in string:
        if ch.isdigit():
            first = int(ch)
            break

    for ch in string[::-1]:
        if ch.isdigit():
            last = int(ch)
            break

    return first*10 + last


def resolve_part1(file_path):
    sum = 0

    with open(file_path, 'r') as f:
        for line in f:
            to_add = calculate_line_sum(line.strip())
            sum += to_add
            print(f'{line.strip()} -> {to_add}')

    return sum


if __name__ == '__main__':
    # calculate test file sum
    test_sum = resolve_part1('part1_test.txt')

    # test sum value
    assert test_sum == 142
