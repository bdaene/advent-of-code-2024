import logging
from importlib import import_module
from importlib.resources import files

from utils import timeit

_LOGGER = logging.getLogger(__name__)


def get_all_days():
    all_files = [file.name for file in files("advent_of_code_2024").iterdir()]
    all_days = [file.removesuffix(".py") for file in all_files if file.startswith("day_")]
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
