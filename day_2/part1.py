limits = {
    'blue': 14,
    'green': 13,
    'red': 12
}


def get_game_id(string: str) -> int:
    return int(string.replace('Game ', ''))


def resolve_part1(file_path):
    sum = 0

    with open(file_path, 'r') as f:
        for line in f:
            game_components = line.strip().split(':')

            game_id = get_game_id(game_components[0])

            # get each draw result, split by ;
            draws = game_components[1].split(';')

            # for each draw, split by ,
            # get the color and the number
            draw_results_validity = []
            for draw_result in draws:
                part_components = draw_result.split(',')

                for res in part_components:
                    spl = res.strip().split(' ')
                    color = spl[1].strip()
                    number = int(spl[0].strip())

                    if number <= limits[color]:
                        draw_results_validity.append(True)
                    else:
                        draw_results_validity.append(False)

            # if all the draws are true
            # add the game id to the sum
            if all(draw_results_validity):
                sum += game_id

    return sum


if __name__ == '__main__':
    # calculate test file sum
    test_sum = resolve_part1('test.txt')

    # test sum value
    assert test_sum == 8
