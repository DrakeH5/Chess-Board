#include <Stepper.h>

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

int incomingByte = 0;
 
void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(60);
  // initialize the serial port:
  Serial.begin(9600);
}

void loop() {

  if(Serial.available() > 0) {
    String input = Serial.readString();
    int x1 = input[0];
    int y1 = input[2]; 
    int x2 = input[4]; 
    int y2 = input[6];
    if(input[0] > 47){
      x1 -= 48;
      y1 -= 48;
      x2 -= 48;
      y2 -= 48;
    } 
    /*Serial.println(x1);
    Serial.println(y1);
    Serial.println(x2);
    Serial.println(y2);*/
    CalculateRotations(x1, y1, x2, y2);
  } else {
    //err
    //Serial.println("No Serial Connection");
  }

}




void CalculateRotations(int x1, int y1, int x2, int y2) {
  if(y1<4){
    myStepper.step(stepsPerRevolution);
  } else {
    myStepper.step(-stepsPerRevolution);
  }
}
