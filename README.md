Arduino Ultrasonic Radar

A live radar-style scanner: an Arduino sweeps an ultrasonic sensor with a servo and streams readings over serial to a Python + pygame app that renders them as a radar display with range rings, a sweep line, and a fading trail.


How it works
- Firmware (firmware/) — sweeps the servo, takes an ultrasonic reading at each angle, and sends it over serial as a framed {angle,distance} message.
- Protocol — messages are reconstructed character-by-character on the receiving end, with safeguards against malformed messages (wrong comma count) and stuck/incomplete reads (timeout).
- PC app (pc-app/) — reader.py parses the serial stream into readings; main.py drives the main loop; visualizer.py converts angle/distance into screen coordinates and renders the radar display in pygame.


