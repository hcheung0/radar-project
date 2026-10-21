# Arduino Ultrasonic Radar

An Arduino Uno sweeps an SG90 servo carrying an HC-SR04 ultrasonic sensor across a 180° arc, taking a distance reading at each angle and streaming it over serial. A Python app parses the stream and renders a live radar display with pygame.

## Hardware

- Arduino Uno
- HC-SR04 ultrasonic sensor
- SG90 servo motor
- Breadboard
- Jumper wires

## How It Works

**Sweeping**
`loop()` moves the servo one step per iteration (not a blocking inner loop), reversing direction at 0°/180°.

**Sensing**
Each step, `getDistance()` triggers the ultrasonic sensor and measures the echo with `pulseIn()`, converting the result to centimeters. The call is bounded with a timeout so an out-of-range reading can't stall the loop.

**Serial protocol**
Readings are sent as framed messages: `{angle,distance}`. On the PC side, the `Reader` class in `reader.py` reconstructs messages character by character, since serial bytes arrive in arbitrary, unaligned chunks. It includes safeguards for malformed messages (wrong comma count) and stuck or incomplete reads (timeout).

**Visualization**
`main.py` reads the serial port non-blocking (`in_waiting`) inside the same loop that drives pygame, feeding parsed readings to `visualizer.py`. The visualizer converts angle/distance to screen coordinates (polar-to-Cartesian) and draws:

- A labeled range grid
- A sweep line
- The current detection
- A fading trail of recent readings

## Build and Upload

### Firmware

Built with PlatformIO (Arduino framework) in VS Code. The `Servo` library is declared in `platformio.ini` via `lib_deps`.

```bash
pio run --target upload
```

### PC App

Set the correct COM port in `main.py` first, then:

```bash
pip install pyserial pygame
python pc-app/main.py
```

## Project Structure

```
firmware/
  src/main.cpp      # servo sweep, sensing, serial output
  platformio.ini
pc-app/
  reader.py         # serial protocol parser (state machine)
  main.py           # serial I/O + main loop
  visualizer.py     # pygame rendering
```

## Known Limitations

- Readings can be noisy due to an imperfect sensor mount.
