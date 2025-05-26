from math import atan, degrees

from .logger import get_logger

_log = get_logger(__file__,  "MathLog")


class Math:
    @staticmethod
    def get_angle_by_coord(x: float, y: float) -> float:
        if int(x) == 288:
            return 0
        if x < 288:
            rad_res = -atan((288 - x) / y)
        else:
            rad_res = atan((x - 288) / y)

        deg_res = degrees(rad_res)
        _log.info(f"angle {deg_res} for coords: {x=}, {y=}")
        return deg_res
    
    @staticmethod
    def map(x: float) -> int:
        in_min = -90
        in_max = 90
        out_min = -4132
        out_max = 4132
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)