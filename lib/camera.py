from typing import Union

import cv2
from PIL import Image

from .logger import get_logger
from .settings import Config
from .utils import singleton

_config = Config()
_log = get_logger(__file__, "CameraLog")


@singleton
class Camera:
    def __init__(self) -> None:
        self.camera = cv2.VideoCapture(_config.camera.cv2_index)
    
    @property
    def get(self) -> Union[None, Image.Image]:
        ret, frame = self.camera.read()
        if not ret:
            _log.info("Failed to read camera")
            return
        
        if _config.camera.translate_colors:
            good_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        else:
            good_frame = frame
        return Image.fromarray(good_frame)
