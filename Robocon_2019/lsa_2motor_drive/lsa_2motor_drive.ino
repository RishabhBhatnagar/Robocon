#define m1p1 5
#define m1p2 6
#define pwm1 9

#define m2p1 5
#define m2p2 6
#define pwm2 9

#define motor1_base_speed 70
#define motor2_base_speed 70

int previous_error = 0;

void setup() {
  // put your setup code here, to run once:
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


void loop() {
  // put your main code here, to run repeatedly:
  motorOn(m1p1, m1p2, )
}
