// C Preprocessor Macros (Saves RAM on embedded chips)
#define TRIG_PIN 9
#define ECHO_PIN 10

void setup() {
  // Initialize the Serial hardware UART interface
  Serial.begin(9600);
  
  // Configure data direction registers for the pins
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  // Local variables declared at the top of the function scope (Standard C style)
  long duration;
  int distance_cm;

  // 1. Ensure the trigger line is clear
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  
  // 2. Generate a precise 10-microsecond square wave trigger pulse
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  // 3. Capture the Time-of-Flight (ToF) echo pulse width in microseconds
  duration = pulseIn(ECHO_PIN, HIGH);
  
  // 4. Compute physical distance in centimeters
  // Conversion derived from the speed of sound: (343 m/s)
  distance_cm = (int)(duration / 58.2);
  
  // 5. Stream the raw integer values to the serial transmit buffer
  if (distance_cm > 0 && distance_cm < 400) {
    Serial.println(distance_cm);
  }
  
  // 100ms sampling interval delay
  delay(100);
}