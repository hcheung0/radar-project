#include <Arduino.h>
#include <Servo.h>

Servo myServo;
int trigPin = 7;
int echoPin = 8;
int servoPin = 9;

int angle = 0;
int increment = 2;
int distance = 0; 

int getDistance() {
	digitalWrite(trigPin, LOW);
	digitalWrite(trigPin, HIGH);
	delayMicroseconds(10);
	digitalWrite(trigPin, LOW);
	int distanceCm = pulseIn(echoPin, HIGH, 25000) / 58;
	return distanceCm;
}

void setup() {
	Serial.begin(9600);
	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);
	myServo.attach(servoPin);
}

void loop() {
	myServo.write(angle);

	distance = getDistance();
	
	Serial.print("{");
	Serial.print(angle);
	Serial.print(",");
	Serial.print(distance);
	Serial.print("}");
	
	angle += increment;
	if (angle >= 180 || angle <= 0) {
		increment *= -1;
	}

	delay(50);
}
