#define m1p1 5
#define m1p2 6
#define pwm1 9

#define m2p1 5
#define m2p2 6
#define pwm2 9

#define m3p1 5
#define m3p2 6
#define pwm3 9

#define m4p1 5
#define m4p2 6
#define pwm4 9

#define motor1_base_speed 70
#define motor2_base_speed 70
#define motor3_base_speed 70
#define motor4_base_speed 70

void setup(){
  Serial.begin(9600);
  
  pinMode(m1p1, OUTPUT);
  pinMode(m1p2, OUTPUT);
  pinMode(pwm1, OUTPUT);
}

void motorOn(int mp1, int mp2, int pwm, int pwm_value, bool forward){
  if(forward){
    digitalWrite(mp1, HIGH);
    digitalWrite(mp2, LOW);
    }
  else{
    digitalWrite(mp1, HIGH);
    digitalWrite(mp2, LOW);
    }
    analogWrite(pwm, pwm_value);
  }
void motorOff(int mp1, int mp2, int pwm){
  digitalWrite(mp1, HIGH);
  digitalWrite(mp2, LOW);
  analogWrite(pwm, 0);
  }
  /* Motor config:

                 2
               ______

              
         |               |
       1 |               | 3
         |               |  
          
               ______
                 4
     Assuming all the motors rotate in clockwise manner wrt center of the box.
*/
void left(int left_pwm, int right_pwm){
  //left and right wrt motor1
  motorOff(m1p1, m1p2, pwm1);
  motorOff(m3p1, m3p2, pwm3);

  motorOn(m2p1, m2p2, pwm2, right_pwm, false);
  motorOn(m4p1, m4p2, pwm4, left_pwm, true);
}

void right(int left_pwm, int right_pwm){
  motorOff(m1p1, m1p2, pwm1);
  motorOff(m3p1, m3p2, pwm3);

  motorOn(m2p1, m2p2, pwm2, right_pwm, true);
  motorOn(m4p1, m2p2, pwm2, left_pwm, false);
}

void down(int left_pwm, int right_pwm){
  //left and right wrt motor 2.
  motorOff(m2p1, m2p2, pwm2);
  motorOff(m4p1, m4p2, pwm4);

  motorOn(m1p1, m1p2, pwm1, left_pwm, false);
  motorOn(m3p1, m3p2, pwm3, right_pwm, true);
}

void up(int left_pwm, int right_pwm){
  motorOff(m2p1, m2p2, pwm2);
  motorOff(m4p1, m4p2, pwm4);

  motorOn(m1p1, m1p2, pwm1, left_pwm, true);
  motorOn(m3p1, m3p2, pwm3, right_pwm, false);
}

void pid_tuning(int current_position, int set_point, int kp, int kd, int previous_error){
  int error = current_position - set_point;
  int speed_change = kp*error + kd*(error - previous_error);
  return speed_change;
}
void loop(){
    //PID for lsa08 connected on side1 ie forward.
    //left motor is 4 and right motor is 2.
}
