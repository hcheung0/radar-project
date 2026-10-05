Arduino Ultrasonic Radar

An Arduino Uno sweeps an SG90 servo carrying an HC-SR04 ultrasonic sensor across a 180° arc, taking a distance reading at each angle and streaming it over serial. A Python app parses the stream and renders a live radar display with pygame.

Hardware
- Arduino Uno
- HC-SR04 ultrasonic sensor
- SG90 servo motor
- Breadboard
- Jumper wires

How it works
- Sweeping: `loop()` moves the servo one step per iteration (not a blocking inner loop), reversing direction at 0°/180°.
- Sensing: each step, `getDistance()` triggers the ultrasonic sensor and measures the echo with `pulseIn()` (bounded with a timeout so an out-of-range reading can't stall the loop), converting the result to centimeters.
- Serial protocol: readings are sent as framed messages, `{angle,distance}`. On the PC side, `reader.py`'s `Reader` class reconstructs messages character-by-character, since serial bytes arrive in arbitrary, unaligned chunks — with safeguards for malformed messages (wrong comma count) and stuck/incomplete reads (timeout).
- Visualization: `main.py` reads the serial port non-blocking (`in_waiting`) inside the same loop that drives pygame, feeding parsed readings to `visualizer.py`, which converts angle/distance to screen coordinates (polar-to-Cartesian) and draws a labeled range grid, a sweep line, the current detection, and a fading trail of recent readings.

Build and upload
- Firmware built with PlatformIO (Arduino framework) in VS Code.
- Dependency: `Servo` (declared in `platformio.ini` via `lib_deps`).
```
pio run --target upload
```
- PC app:
```
pip install pyserial pygame
python pc-app/main.py
```
(set the correct COM port in `main.py` first)

Project structure
```
firmware/
  src/main.cpp     # servo sweep, sensing, serial output
  platformio.ini
pc-app/
  reader.py        # serial protocol parser (state machine)
  main.py          # serial I/O + main loop
  visualizer.py     # pygame rendering
```

## Known limitations
Readings can suck due to a scuffed mount setup.
