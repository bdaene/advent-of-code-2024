import logging
from importlib import import_module
from importlib.resources import contents

from utils import timeit

_LOGGER = logging.getLogger(__name__)


def get_all_days():
    all_days = [file.removesuffix(".py") for file in contents("advent_of_code_2024") if file.startswith("day_")]
    return {day: import_module(day, "advent_of_code_2024") for day in all_days}


@timeit
def run_all(days):
    for day, module in days.items():
        _LOGGER.info(f"-------- {day} --------")
        module.main()


def main():
    days = get_all_days()
    run_all(days)


if __name__ == "__main__":
    main()
