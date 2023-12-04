from functools import wraps
from time import perf_counter
from typing import TypeVar, ParamSpec, Callable
from prettytable import PrettyTable, SINGLE_BORDER

T = TypeVar('T')
P = ParamSpec('P')


def aoc_output(title: str):
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            start_time = perf_counter()
            result = func(*args, **kwargs)
            elapsed_time = perf_counter() - start_time

            table = PrettyTable(
                title=title, encoding='utf-8', 
                align='l', header=False
            )
            table.set_style(SINGLE_BORDER)
            table.add_rows([
                (f"Answer: {result}",),
                (f"Time: {elapsed_time:.6f} seconds",)
            ])
            print(table)

            return result
        return wrapper
    return decorator
