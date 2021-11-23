// =============================================================================
// Created By  : Anton Sundqvist
// Created Date: 2021-05-11
/* =============================================================================
    Code for handeling the i2c slave communication and switching of eacg rail 
    switch of the Märklin rail switches.
   =============================================================================*/
// Imports
#include <Wire.h>
// =============================================================================
bool set_flag = true;

void setup() {
  pinMode(A3, INPUT); //DIP switch
  pinMode(A2, INPUT); //DIP switch
  pinMode(A1, INPUT); //DIP switch
  pinMode(A0, INPUT); //DIP switch

  pinMode(13, OUTPUT); //Train switch control
  pinMode(12, OUTPUT); //Train switch control
  pinMode(11, OUTPUT); //Train switch control
  pinMode(10, OUTPUT); //Train switch control
  pinMode(9, OUTPUT); //Train switch control
  pinMode(8, OUTPUT); //Train switch control
  pinMode(7, OUTPUT); //Train switch control
  pinMode(6, OUTPUT); //Train switch control
  pinMode(5, OUTPUT); //Train switch control
  pinMode(4, OUTPUT); //Train switch control
  pinMode(3, OUTPUT); //Train switch control
  pinMode(2, OUTPUT); //Train switch control
  pinMode(1, OUTPUT); //Train switch control
  pinMode(0, OUTPUT); //Train switch control

  Wire.begin(set_adress());
  Wire.onReceive(receiveEvent);
}

void toggle_low(){
  digitalWrite(0, LOW);
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  digitalWrite(13, LOW);
  set_flag = false;
}

//Sets the i2c adress of the decive based on the state of the DIP switch
int set_adress() {

  int adress = 0;
  
  if(digitalRead(A0) == 1){
    bitSet(adress, 0);
  }
  if(digitalRead(A1) == 1){
    bitSet(adress, 1);
  }
  if(digitalRead(A2) == 1){
    bitSet(adress, 2);
  }
  if(digitalRead(A3) == 1){
    bitSet(adress, 3);
  }
  
  return adress;
}

void receiveEvent(int howMany) {
  int number_array[7] = {-1, 0, 1, 2, 3, 4, 5 }; //Array for calulating the correct pin to toggle for switches in the state of 1
  int switch_select[14] = {0, 1, 4, 8, 5, 9, 12, 2, 3, 7, 6, 10, 11, 13}; //Array for arange the output pins to the correct transistor
  //{10, 12, 0, 2, 4, 6, 8, 9, 11, 13, 1, 3, 5, 7} OLD LAYOUT for V1.1
  
  int switch_command = Wire.read();
  int toggle = 0; //Initelize the toggle of the switch
  int switch_number = switch_command  / 10;
  int switch_setting = switch_command  % 10;

  if(switch_setting == 1){
      toggle = switch_number + number_array[switch_number - 1];
      digitalWrite(switch_select[toggle], HIGH);
      set_flag = true;
  }
  else if(switch_setting == 2){ 
      toggle = switch_number * 2 - 1;
      digitalWrite(switch_select[toggle], HIGH);
      set_flag = true;
  }
}

void loop() {
  delay(100);
  if(set_flag == true){
    delay(500);
    toggle_low();
  }
}
