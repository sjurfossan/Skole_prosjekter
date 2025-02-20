
#include <Servo.h>

//Free pins: 0

int velocity_R = 0;   
int velocity_L = 0;
int R_stick = 0;         // value of right stick
int L_stick = 0;         // value of left stick
int weapon_wheel = 0;    // Value of weapon wheel
int wheel_set_value = 0; // Value for controlling which set of wheels we want to control
int wheel_drive = 0;
int weapon_dir = 0;
int gap = 17884;

int relay_roof = 4;
int relay_floor_1 = 8;
int relay_floor_2 = 2;

int velocity_R_1 = 0;
int velocity_L_1 = 0;

// Values of the channels
int middle_ch = 18388 - gap;
int max_ch = 18877 - gap;
int min_ch = 17890 - gap;

#define R_S 9         //Channel 2
#define L_S 10        //Channel 3
#define weapon 5      //Channel 5
#define wheel_set_1 11 //Channel 6

int weapon_drive_1 = 12;    // Pin for weapon output
int weapon_drive_2 = 13;    // Pin for weapon output


Servo servo_right; //Right
Servo servo_left; //Left


// For measuring battery voltage
int bms_pin = A0;
float R1 = 19.8; //[kOhms] this is the value we have measured
float R2 = 9.8; //[kOhms] this is the value we have measured
float battery_voltage_start = 12.9;  //We need to actually measure this
float battery_voltage_middle = 12.0; //This is for giving light to the first LED-light
float battery_voltage_end = 11.8;    //This is when we want to turn on the last LED-light, which means stop
int voltage_led_end = 7;           //Pin for last LED-light
float battery_voltage = 0.0;

void setup() {

  
  // Pin setup for led-light
  pinMode(voltage_led_end, OUTPUT);       //Pin 7
  digitalWrite(voltage_led_end, LOW);
  
  
  // Pin setup for servo-motors
  pinMode(R_S, INPUT); // Right stick
  pinMode(L_S, INPUT); // Left stick
  servo_right.attach(3);
  servo_left.attach(6);
  
  // Pin setup for weapon
  pinMode(weapon, INPUT);
  pinMode(weapon_drive_1, OUTPUT);
  pinMode(weapon_drive_2, OUTPUT);

  // Pin setup for switching between floor/roof motors driving
  pinMode(relay_roof, OUTPUT);
  digitalWrite(relay_roof, LOW);

  pinMode(relay_floor_1, OUTPUT);
  pinMode(relay_floor_2, OUTPUT);
  digitalWrite(relay_floor_1, LOW);
  digitalWrite(relay_floor_2, LOW);
}


void loop() {
  R_stick = pulseIn(R_S, LOW) - gap;
  L_stick = pulseIn(L_S, LOW) - gap;
  
  wheel_set_value = pulseIn(wheel_set_1, LOW) - gap;
  
  weapon_wheel = pulseIn(weapon, LOW) - gap;


  // Monitoring battery voltage
  battery_voltage = analogRead(bms_pin)*(0.8*5.0/1023.0)*3.0;
  if(battery_voltage <= battery_voltage_end){
    digitalWrite(voltage_led_end, HIGH);
  }
  else{
    digitalWrite(voltage_led_end, LOW);
  }
  
  

  
  weapon_dir = constrain(map(weapon_wheel, min_ch, max_ch, 1, 9), 1, 9);
  
  velocity_R = constrain((map(R_stick, min_ch, max_ch, 0, 180) + 10), 0, 180);
  velocity_L = constrain((map(L_stick, min_ch, max_ch, 0, 180) + 10), 0, 180);

  
  wheel_drive = constrain(map(wheel_set_value, min_ch, max_ch, 1, 9), 1, 9);
  
  if(wheel_drive <= 3){
    digitalWrite(relay_roof, HIGH);
    digitalWrite(relay_floor_1, LOW);
    digitalWrite(relay_floor_2, LOW);
  }
  else if(wheel_drive >= 7){
    digitalWrite(relay_roof, LOW);
    digitalWrite(relay_floor_1, HIGH);
    digitalWrite(relay_floor_2, HIGH);
  }
  else{
    digitalWrite(relay_roof, LOW);
    digitalWrite(relay_floor_1, LOW);
    digitalWrite(relay_floor_2, LOW);
  }
  

  
  // Make weapon move
  if((weapon_dir <= 3) && (weapon_dir >= 1)){
    digitalWrite(weapon_drive_1, LOW);
    digitalWrite(weapon_drive_2, HIGH);
  }

  else if((weapon_dir <= 6) && (weapon_dir >= 4)){
    digitalWrite(weapon_drive_1, LOW);
    digitalWrite(weapon_drive_2, LOW);
  }

  else if((weapon_dir <= 9) && (weapon_dir >= 7)){
    digitalWrite(weapon_drive_1, HIGH);
    digitalWrite(weapon_drive_2, LOW);
  }

  // Just for safety concerns 
  else{
    digitalWrite(weapon_drive_1, LOW);
    digitalWrite(weapon_drive_2, LOW);
  }
  
  
  // Right servos
  if((velocity_R > 80) && (velocity_R < 100)) {
    servo_right.write(90);
    }
  else if(velocity_R >= 100) {
    velocity_R_1 = constrain(map(velocity_R, 100, 180, 90, 185), 90, 180);
    servo_right.write(180-velocity_R_1);
    }
  else {
    velocity_R_1 = map(velocity_R, 0, 80, 0, 90);
    servo_right.write(180-velocity_R_1);
    }

  // Left servos
  if((velocity_L > 80) && (velocity_L < 100)) {
    servo_left.write(90);
    }
  else if(velocity_L >= 100) {
    velocity_L_1 = map(velocity_L, 100, 180, 90, 180);
    servo_left.write((velocity_L_1));
    }
  else {
    velocity_L_1 = map(velocity_L, 0, 80, 0, 90);
    servo_left.write((velocity_L_1));
    }
}
