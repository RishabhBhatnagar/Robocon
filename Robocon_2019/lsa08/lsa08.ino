const int Kp = 1;   // Kp value that you have to change
const int Kd = 0;   // Kd value that you have to change
const int setPoint = 35;    // Middle point of sensor array
const int baseSpeed = 50;    // Base speed for your motors
const int maxSpeed = 100;   // Maximum speed for your motors

const byte rx = 0;    // Defining pin 0 as Rx
const byte tx = 1;    // Defining pin 1 as Tx
const byte serialEn = 2;    // Connect UART output enable of LSA08 to pin 2
const byte junctionPulse = 4;   // Connect JPULSE of LSA08 to pin 4

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
#define m1p1 44
#define m1p2 45
#define pwm1 6

#define m2p1 52
#define m2p2 53
#define pwm2 3

#define m3p1 49
#define m3p2 48
#define pwm3 5

#define m4p1 41
#define m4p2 40
#define pwm4 4

#define motor1_base_speed 30
#define motor2_base_speed 30
#define motor3_base_speed 30
#define motor4_base_speed 35

void setup(){
  Serial.begin(9600);
  
  pinMode(m1p1, OUTPUT);
  pinMode(m1p2, OUTPUT);
  pinMode(pwm1, OUTPUT);

  pinMode(m2p1, OUTPUT);
  pinMode(m2p2, OUTPUT);
  pinMode(pwm2, OUTPUT);
  
  pinMode(m3p1, OUTPUT);
  pinMode(m3p2, OUTPUT);
  pinMode(pwm3, OUTPUT);
  
  pinMode(m4p1, OUTPUT);
  pinMode(m4p2, OUTPUT);
  pinMode(pwm4, OUTPUT);

  pinMode(serialEn,OUTPUT);   // Setting serialEn as digital output pin
  pinMode(junctionPulse,INPUT);   // Setting junctionPulse as digital input pin
  digitalWrite(serialEn,HIGH);
}

void motorOn(int mp1, int mp2, int pwm, int pwm_value, bool forward){
  if(forward){
    digitalWrite(mp1, HIGH);
    digitalWrite(mp2, LOW);
    }
  else{
    digitalWrite(mp1, LOW);
    digitalWrite(mp2, HIGH);
    }
    analogWrite(pwm, pwm_value);
  }
void motorOff(int mp1, int mp2, int pwm){
  digitalWrite(mp1, LOW);
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

  motorOn(m2p1, m2p2, pwm2, right_pwm, true);
  motorOn(m4p1, m4p2, pwm4, left_pwm, true);
}

void right(int left_pwm, int right_pwm){
  motorOff(m1p1, m1p2, pwm1);
  motorOff(m3p1, m3p2, pwm3);

  motorOn(m2p1, m2p2, pwm2, right_pwm, false);
  motorOn(m4p1, m4p2, pwm4, left_pwm, false);
}

void down(int left_pwm, int right_pwm){
  //left and right wrt motor 2.
  motorOff(m2p1, m2p2, pwm2);
  motorOff(m4p1, m4p2, pwm4);

  motorOn(m1p1, m1p2, pwm1, left_pwm, false);
  motorOn(m3p1, m3p2, pwm3, right_pwm, false);
}

void up(int left_pwm, int right_pwm){
  motorOff(m2p1, m2p2, pwm2);
  motorOff(m4p1, m4p2, pwm4);

  motorOn(m1p1, m1p2, pwm1, left_pwm, true);
  motorOn(m3p1, m3p2, pwm3, right_pwm, true);
}

void pid_tuning(int current_position, int set_point, int kp, int kd, int previous_error){
  int error = current_position - set_point;
  int speed_change = kp*error + kd*(error - previous_error);
  return speed_change;
}

int lastError = 0; // Declare a variable to store previous error

void loop(){
    //PID for lsa08 connected on side1 ie forward.
    //left motor is 4 and right motor is 2.
    
    digitalWrite(serialEn,LOW);   // Set serialEN to LOW to request UART data

    while(Serial.available() >=0)   // Wait for data to be available
    {Serial.println("waiting");}
    int positionVal = Serial.read();    // Read incoming data and store in variable positionVal
    digitalWrite(serialEn,HIGH); // Stop requesting for UART data

    if(positionVal == 255) {
    motorOff(m1p1, m1p2, pwm1);
    motorOff(m3p1, m3p2, pwm3);
    }
    else {
    Serial.println(positionVal);
    int error = positionVal - setPoint;   // Calculate the deviation from position to the set point
    int motorSpeed = Kp * error + Kd * (error - lastError);   // Applying formula of PID
    lastError = error;    // Store current error as previous error for next iteration use

    // Adjust the motor speed based on calculated value
    // You might need to interchange the + and - sign if your robot move in opposite direction
    int rightMotorSpeed = baseSpeed - motorSpeed;
    int leftMotorSpeed = baseSpeed + motorSpeed;

    // If the speed of motor exceed max speed, set the speed to max speed
    if(rightMotorSpeed > maxSpeed) rightMotorSpeed = maxSpeed;
    if(leftMotorSpeed > maxSpeed) leftMotorSpeed = maxSpeed;

    // If the speed of motor is negative, set it to 0
    if(rightMotorSpeed < 0) rightMotorSpeed = 0;
    if(leftMotorSpeed < 0) leftMotorSpeed = 0;

    // Writing the motor speed value as output to hardware motor
    
    //analogWrite(pwm1,rightMotorSpeed);
    //analogWrite(pwm2,leftMotorSpeed);

    Serial.println(leftMotorSpeed);
    Serial.print(rightMotorSpeed);
    
    up(leftMotorSpeed, rightMotorSpeed);
    
  }

    /*
    motorOn(m1p1, m1p2, pwm1, motor1_base_speed, true);
    motorOn(m2p1, m2p2, pwm2, motor2_base_speed, true);
    motorOn(m3p1, m3p2, pwm3, motor3_base_speed, true);
    motorOn(m4p1, m4p2, pwm4, motor4_base_speed, true);
    */
}
