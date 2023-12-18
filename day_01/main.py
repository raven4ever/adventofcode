from part1 import resolve_part1
from part2 import resolve_part2

if __name__ == '__main__':
    # run part 1
    input_sum = resolve_part1('input.txt')

    print(f'Sum of all of the calibration values: {input_sum}')

    assert input_sum == 54630, f'Expected 54630 but got {input_sum}'

    # run part 2
    input_sum = resolve_part2('input.txt')

    print(f'Sum of all of the calibration values: {input_sum}')

    assert input_sum == 54770, f'Expected 54770 but got {input_sum}'
