from json import load as js_load

from .utils import singleton

CONFIG_PATH = "config.json"


class _JsToModel:
    def __init__(self, data: dict):
        self.load(data)

    
    def load(self, config: dict):
        for key, value in config.items():
            if isinstance(value, dict):
                gtype = type("Item", (_JsToModel,), {})
                val = gtype(value)
            else:
                val = value
            
            setattr(self, key, val)


class AiConfig:
    model_path: str
    init_image_path: str


class CameraConfig:
    cv2_index: int
    translate_colors: bool


class ModbusConfig:
    port: str
    addres: int
    timeout: float


@singleton
class Config(_JsToModel):
    logs_dir: str
    mainloop_step_delay: float

    ai: AiConfig
    camera: CameraConfig
    modbus: ModbusConfig

    def __init__(self):
        self.load(js_load(open(CONFIG_PATH)))
