import irsdk
import time

class IRacingMonitor:
    class State:
        def __init__(self):
            self.ir_connected = False
            self.last_car_setup_tick = -1

    def __init__(self):
        self.ir = irsdk.IRSDK()
        self.state = self.State()

    def check_iracing(self):
        if self.state.ir_connected and not (self.ir.is_initialized and self.ir.is_connected):
            self.state.ir_connected = False
            self.state.last_car_setup_tick = -1
            self.ir.shutdown()
            print('irsdk disconnected')
        elif not self.state.ir_connected and self.ir.startup() and self.ir.is_initialized and self.ir.is_connected:
            self.state.ir_connected = True
            print('irsdk connected')

    def loop(self):
        self.ir.freeze_var_buffer_latest()

    def run(self):
        try:
            while True:
                self.check_iracing()
                if self.state.ir_connected:
                    self.loop()
                time.sleep(1)
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    monitor = IRacingMonitor()
    monitor.run()