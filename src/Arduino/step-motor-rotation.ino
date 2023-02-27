#include <Stepper.h>
const double stepsPerRevolution = 2048; // steps per rev = (360º / 5.625 / (1/64))/2
Stepper stepper(stepsPerRevolution, 8,10,9,11);

void setup() {
  stepper.setSpeed(16);
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  
  if( Serial.available() ) {
    char c = (char) Serial.read();
    if(c == 'c') {
      stepper.step(stepsPerRevolution);
      delay(500);
      Serial.print("Clockwise\n");
    }
    else if(c == 'C') {
      stepper.step(-stepsPerRevolution);
      delay(500);
      Serial.print("Counter-Clockwise\n");
    }
  }

}
