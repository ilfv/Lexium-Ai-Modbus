from typing import Tuple, Union, List

from ultralytics.engine.results import Results


def singleton(cls):
    instances = {}
    def inner(*args, **kwargs):
        if not instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]
    return inner

def get_coords(inp: Union[Results, List[float]]) -> Tuple[float, float]:
    if isinstance(inp, Results):
        x, y, x1, y1 = inp.boxes.xyxy
    else:
        x, y, x1, y1 = inp
    return float((x + x1) / 2), float((y + y1) / 2)
