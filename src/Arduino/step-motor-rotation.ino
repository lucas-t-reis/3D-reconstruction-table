#include <Stepper.h>

const int stepsPerRevolution = 2048;
Stepper tableStepper(stepsPerRevolution, 8, 10, 9, 11);
Stepper cameraStepper(stepsPerRevolution, 3, 5, 4, 6);

// Added variables to control stepper speed and ramp up
int cameraSpeed = 0;
const int MAX_SPEED = 14;
const int rampPortions = 20; // Number of portions per full rotation around the table
const int rotationsRatio = 6; // Ratio of structure diameter to cog diameter

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char c = (char) Serial.read();

    if (c == 'c' || c == 'C') {
      // Reset camera speed
      cameraSpeed = 0;

      int direction = (c == 'c') ? 1 : -1;
      int stepsPerPortion = rotationsRatio * stepsPerRevolution / rampPortions;

      // Continue rotating and increasing speed until max speed is reached
      for (int i = 0; i < rampPortions && cameraSpeed < MAX_SPEED; i++) {
        cameraSpeed++;
        cameraStepper.setSpeed(cameraSpeed);
        cameraStepper.step(direction * stepsPerPortion);

      }

      // tableStepper.setSpeed(15);
      // tableStepper.step(stepsPerRevolution / rotationsRatio);

      Serial.print((direction == 1) ? "Clockwise\n" : "Counter-Clockwise\n");
    }
  }
}
