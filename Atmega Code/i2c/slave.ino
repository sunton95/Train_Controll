// =============================================================================
// Created By  : Anton Sundqvist
// Created Date: 2021-05-11
/* =============================================================================
    Code for handeling the i2c slave communication and switching of eacg rail 
    switch of the Märklin rail switches.
   =============================================================================*/
// Imports

// =============================================================================

void setup() {
  pinMode(5, OUTPUT); //Train switch control
  pinMode(4, OUTPUT); //Train switch control
}


void loop() {
    delay(1000);
    digitalWrite(9, HIGH);
    delay(1000);
    digitalWrite(9, LOW);

    delay(1000);
    digitalWrite(10, HIGH);
    delay(1000);
    digitalWrite(10, LOW);

}
