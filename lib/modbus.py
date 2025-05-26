from typing import List

from pymodbus.client import ModbusSerialClient as ModbusClient

from .logger import get_logger
from .settings import Config
from .utils import singleton

_config = Config()
_log = get_logger(__file__, "ModbusLog")

PORT = "COM2"
ADDRES = 1
TIMEOUT = .1


@singleton
class MBClient:
    def __init__(self) -> None:
        _log.info(f"init ModbusClient for port {_config.modbus.port} and addres {_config.modbus.addres}")
        self.client = ModbusClient(port=_config.modbus.port, timeout=_config.modbus.timeout)

    def send(self, angle: int):
        resp = self.client.write_registers(address=_config.modbus.addres, values=self.convert(angle), slave=1)
        return resp
    
    def convert(self, angle: int) -> List[int]:
        lst = [0, 0]
        if angle < 0:
            lst[0] = 65535
        lst[1] = self.to_hex(angle)
        return lst
    
    @staticmethod
    def to_hex(val: int, nbits: int = 16) -> int:
        return (val + (1 << nbits)) % (1 << nbits)
