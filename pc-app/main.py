import serial
from visualizer import init_display, draw_frame, handle_events
from reader import Reader

def main():
    r = Reader()
    ser = serial.Serial('COM3', 9600)
    previous_reading = None
    running = True
    screen = init_display()

    while running:
        running = handle_events()

        if ser.in_waiting > 0:
            byte = ser.read(1)
            char = byte.decode('utf-8')
            r.handle_char(char)
        if r.latest_reading is not None and r.latest_reading != previous_reading:
            print(r.latest_reading)
            previous_reading = r.latest_reading

        draw_frame(screen, r.latest_reading)


if __name__ == "__main__":
    main()