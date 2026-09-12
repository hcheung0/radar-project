import serial
import time
from visualizer import init_display, draw_frame, handle_events, MAX_AGE
from reader import Reader

def main():
    r = Reader()
    ser = serial.Serial('COM3', 9600)
    previous_reading = None
    running = True
    screen = init_display()
    trail = []

    while running:
        running = handle_events()

        if ser.in_waiting > 0:
            byte = ser.read(1)
            char = byte.decode('utf-8')
            r.handle_char(char)
        if r.latest_reading is not None and r.latest_reading != previous_reading:
            print(r.latest_reading)
            previous_reading = r.latest_reading
            trail.append((r.latest_reading[0], r.latest_reading[1], time.time()))

        trail = [entry for entry in trail if (time.time()-entry[2]< MAX_AGE)]
        draw_frame(screen, r.latest_reading, trail)


if __name__ == "__main__":
    main()