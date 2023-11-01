from time import time


class Timer:
    def __init__(self, precision=3):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
        self.precision = precision

    def start(self):
        self.start_time = time()

    def stop(self):
        self.end_time = time()
        if self.start_time is not None and self.end_time is not None:
            self.elapsed_time = round(self.end_time - self.start_time, self.precision)
