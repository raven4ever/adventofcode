from pathlib import Path

import requests


def get_session_id() -> str:
    session_file = Path(".session_id")
    if not session_file.exists():
        raise UserWarning("Session ID not found in file .session_id")

    return session_file.read_text(encoding="utf-8").strip("\n")


def download_input_for_day(day: str, year: str = '2023'):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    day_input_file = Path(f'day_{day}/input.txt')

    if not day_input_file.exists():
        print(f'Downloading input file for day {day}...')

        session_id = get_session_id()

        response = requests.get(
            url, cookies={"session": session_id}, timeout=5)

        if response.status_code == 200:
            day_input_file.write_text(response.text, encoding="utf-8")
            print(f'Input file for day {day} downloaded successfully.')
        else:
            print(f'Error downloading input file for day {day}.')
    else:
        print(f'Input file for day {day} already exists.')


if __name__ == '__main__':
    download_input_for_day('1')
