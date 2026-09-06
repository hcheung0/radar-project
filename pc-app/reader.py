import time

class Reader:
    def __init__(self, timeout=1.0):
        self.buffer = ""
        self.comma_count = 0
        self.start_time = None
        self.timeout = timeout
        self.latest_reading = None

    def handle_char(self, c):
        if c == '{':
            self.comma_count = 0
            self.buffer = ""
            self.start_time = time.time()
        elif c == ',':
            self.comma_count += 1
            self.buffer += c
        elif c == '}':
            parts = self.buffer.split(",")
            try:
                angle = int(parts[0])
                distance = int(parts[1])
                self.latest_reading = (angle, distance)
            except ValueError:
                self.buffer = ""
                self.start_time = None
                return
            self.buffer = ""
            self.start_time = None
        else:
            self.buffer += c

        if (self.start_time is not None and (time.time() - self.start_time) > self.timeout) or self.comma_count > 1:
            self.buffer = ""
            self.comma_count = 0
            self.start_time = None