def resolve_part2(file_path):
    sum = 0

    with open(file_path, 'r') as f:
        for line in f:
            game_components = line.strip().split(':')

            # get each draw result, split by ;
            draws = game_components[1].split(';')

            # for each draw, split by ,
            # get the max number for each color
            maximums = {}
            for draw_result in draws:
                part_components = draw_result.split(',')

                for res in part_components:
                    spl = res.strip().split(' ')
                    color = spl[1].strip()
                    number = int(spl[0].strip())

                    # if the color is not in the maximums dict add it
                    if color not in maximums:
                        maximums[color] = number
                    else:
                        # if the number is greater than the one in the dict
                        # replace it
                        if number > maximums[color]:
                            maximums[color] = number

            # add to the sum the product of the maximums
            sum += maximums['blue'] * maximums['green'] * maximums['red']

    return sum


if __name__ == '__main__':
    # calculate test file sum
    test_sum = resolve_part2('test.txt')

    # test sum value
    assert test_sum == 2286
