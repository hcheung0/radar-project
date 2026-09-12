import serial
from reader import Reader

def main():
    r = Reader()
    ser = serial.Serial('COM3', 9600)
    previous_reading = None
    while True:
        byte = ser.read(1)
        char = byte.decode('utf-8')
        r.handle_char(char)
        if r.latest_reading is not None and r.latest_reading != previous_reading:
            print(r.latest_reading)
            previous_reading = r.latest_reading

if __name__ == "__main__":
    main()