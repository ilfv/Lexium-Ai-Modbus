from time import sleep

from lib import Ai, Camera, Math, MBClient, Config, get_logger, get_coords

_config = Config()
_log = get_logger(__file__, "MainLogger")


def main():
    _log.info("starting main loop")
    while True:
        sleep(_config.mainloop_step_delay)
        _log.debug("Read camera")
        dat = Camera().get

        if not bool(dat):
            _log.info("Empty camera output")
            continue

        _log.debug("Send image to ai")
        result = Ai().get_best_result(Ai().predict(dat))

        if not result:
            continue

        angle = Math.get_angle_by_coord(*get_coords(result))
        modbus_angle = Math.map(angle)
        _log.info(f"Modbus angle: {modbus_angle}")
        MBClient().send(modbus_angle)


if __name__ == "__main__":
    main()
