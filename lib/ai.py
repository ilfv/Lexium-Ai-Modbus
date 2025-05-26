from uuid import uuid4
from io import BytesIO
from typing import List, Union

import numpy as np
from ultralytics import YOLO
from ultralytics.engine.results import Results
from onnxruntime import InferenceSession
from PIL import Image

from .logger import get_logger
from .settings import Config
from .utils import singleton

_config = Config()
_log = get_logger(__file__, "AiLog")


@singleton
class Ai:
    def __init__(self) -> None:
        _log.info("Checking model input image size")
        self.imgsz: int = InferenceSession(_config.ai.model_path).get_inputs()[0].shape[-1]
        _log.info("Load model")
        self.model = YOLO(_config.ai.model_path)
        _log.info("initialze predict")
        self.model.predict(source=_config.ai.init_image_path, imgsz=self.imgsz)
    
    def predict(self, data: Union[BytesIO, bytes, np.ndarray, Image.Image], **kwargs) -> List[Results]:
        img = None
        if isinstance(data, (bytes, BytesIO)):
            if isinstance(data, bytes):
                data = BytesIO(data)
            img = Image.open(data)
        elif isinstance(data, np.ndarray):
            img = Image.fromarray(data)
        elif isinstance(data, Image.Image):
            img = data
        buff = BytesIO()
        imgs = img.convert("RGB")
        imgs.save(buff, format="jpeg")
        buff.seek(0)
        return self.model.predict(source=Image.open(buff), imgsz=self.imgsz, **kwargs)

    def get_best_result(self, data: List[Results]) -> Union[List[float], bool]:
        saved = False
        res = data[0]
        conf = [float(i) for i in res.boxes.conf]
        if not len(conf):
            return False
        if not any([i > .6 for i in conf]):
            res.save("tm/" + str(uuid4()) + ".jpeg")
            saved = True
            return False
        arr = [*conf]
        ind = arr.index(max(arr))
        if len(conf) == 1:
            coords = [*res.boxes.xyxy[0]]
        else:
            if not saved:
                res.save("tm/" + str(uuid4()) + ".jpeg")
            coords = [*res.boxes.xyxy[ind]]
        _log.info(f"ball detected at " + " ".join([f'{sym}={round(float(val), 2)}' for sym, val in (("x1", coords[0]), ("y1", coords[1]), ("x2", coords[2]), ("y2", coords[3]))]))
        return coords
