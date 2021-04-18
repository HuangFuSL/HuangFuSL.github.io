from typing import Callable


def wrap(inner: Callable, outer: Callable) -> Callable:

    def ret(*args, **kwargs):
        return outer(inner(*args, **kwargs))

    return ret
