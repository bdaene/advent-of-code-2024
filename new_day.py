from datetime import date
from pathlib import Path


def main(day=None):
    if day is None:
        day = date.today().day
    formatted_day = f"day_{day:02d}"

    for path in [
        "advent_of_code_2024/day_00.py",
        "data/inputs/day_00.txt",
        "data/samples/day_00.txt",
        "tests/test_day_00.py",
    ]:
        new_path = path.replace("day_00", formatted_day)
        if Path(new_path).exists():
            continue

        with open(path) as file:
            data = file.read()

        new_data = data.replace("day_00", formatted_day)

        with open(new_path, "w") as new_file:
            new_file.write(new_data)


if __name__ == "__main__":
    main()
