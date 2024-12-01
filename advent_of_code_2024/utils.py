import logging
from functools import wraps
from time import perf_counter


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s%(msecs)d: %(message)s",
        datefmt="%H:%M:%S.",
    )


def timeit(func):
    """Allows to time an execution while still getting the result. With a simple decorator."""

    logger = logging.getLogger(func.__module__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        logger.info(
            "Execution of %s took %.3fms.",
            func.__name__,
            (perf_counter() - start) * 1000,
        )
        logger.info("Result: %s", result)
        return result

    wrapper.func = func
    return wrapper
