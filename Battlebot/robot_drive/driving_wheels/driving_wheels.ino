int velocity_R = 0;   
int velocity_neg_R = 0;
int velocity_pos_R = 0;
int velocity_L = 0;
int velocity_neg_L = 0;
int velocity_pos_L = 0;
int way_R = 0;           // direction motor 1   1 = forword  2 = backward
int way_L = 0;           // direction motor 2   1 = forword  2 = backward
int enable = 0;          // button for enable
int R_stick = 0;         // value of right stick
int L_stick = 0;         // value of left stick
int gap = 17884;


//value of the channels
int middle_ch = 18388 - gap;
int max_ch = 18877 - gap;
int min_ch = 17890 - gap;

//int middle_ch3 = 18366 - gap;
//int max_ch3 = 18877 - gap;
//int min_ch3 = 17884 - gap;

//int middle_ch5 = 1480 - gap;
//int max_ch5 = 1980 - gap;
//int min_ch5 = 995 - gap;


#define R_S 6
#define L_S 10
#define M_C 11
#define ENABLE_R 3
#define ENABLE_L 6
#define DIR_R 2   
#define DIR_R_B 4
#define DIR_L 7
#define DIR_L_B 8

void setup() {
  // setup pin
  pinMode(R_S, INPUT); // Right stick
  pinMode(L_S,INPUT); // Left stick
  pinMode(M_C,INPUT); // Right upper for turn on the motor
  
  pinMode(ENABLE_R, OUTPUT);
  pinMode(ENABLE_L, OUTPUT);
  pinMode(DIR_R, OUTPUT);
  pinMode(DIR_L, OUTPUT); 
  pinMode(DIR_R_B, OUTPUT);
  pinMode(DIR_L_B, OUTPUT); 
  

  Serial.begin(9600);
  
}

void loop() {

enable = digitalRead(pulseIn(M_C, LOW)) - gap;
R_stick = digitalRead(pulseIn(R_S)) - gap;
L_stick = digitalRead(pulseIn(L_S)) - gap;


Serial.println(R_stick);
//Serial.println(L_stick);
//Serial.println(enable);



    //right motor
    if (R_stick > middle_ch1 + 50) // right motor forward
    {
      analogWrite(ENABLE_R, velocity_R);
      digitalWrite(DIR_R, HIGH);
      digitalWrite(DIR_R_B, LOW);
      velocity_pos_R = R_stick - middle_ch1; // is for report the velocity in the same intervall of the negative velocity
      velocity_R = constrain(velocity_pos_R,0 , 255);
    }
    
    
    // right motor Backward
    else if  (R_stick < (middle_ch1 - 50)) 
    {
      analogWrite(ENABLE_R, velocity_R);
      digitalWrite(DIR_R, LOW);
      digitalWrite(DIR_R_B, HIGH);
      velocity_neg_R = R_stick;
      velocity_R = 255 - constrain(velocity_neg_R,0 , 255);
    }

    else 
    {
      velocity_R = 0;
      analogWrite(ENABLE_R, velocity_R);
    }


 //left motor
    if (L_stick > (middle_ch3 + 50)) // left motor forward
    {
      analogWrite(ENABLE_L, velocity_L); 
      digitalWrite(DIR_L, HIGH);
      digitalWrite(DIR_L_B, LOW);
      velocity_pos_L = L_stick - middle_ch3; // is for report the velocity in the same intervall of the negative velocity
      velocity_L = constrain(velocity_pos_L,0 , 255);
    }

    // left motor Backward
    else if (L_stick < (middle_ch3 - 50)) 
    {
      analogWrite(ENABLE_L, velocity_L); 
      digitalWrite(DIR_L, LOW);
      digitalWrite(DIR_L_B, HIGH);
      velocity_neg_L = L_stick;
      velocity_L = 255 - constrain(velocity_neg_L,0 , 255);
    }

    else 
    {
      velocity_L = 0;
      analogWrite(ENABLE_L, velocity_L); 
     }
  }
