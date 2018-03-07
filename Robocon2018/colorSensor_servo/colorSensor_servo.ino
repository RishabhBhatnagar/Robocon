#include <Servo.h>
#define pin0 0
#define pin1 1
#define pin2 2
#define pin3 3
#define pin12 12
#define pin13 13

#define S0 4
#define S1 5
#define S3 6
#define S2 7
#define sensorOut 11


Servo myservo;  // create servo object to control a servo


int a;
int servoPin = 10;
bool written = false;
int prevVal = 0;


int frequency = 0;
int r = 0, g = 0, b = 0;
void setup() {

  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);
  
  // Setting frequency-scaling to 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);



  pinMode(pin0, OUTPUT);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  pinMode(pin12, OUTPUT);
  pinMode(pin13, OUTPUT);
  Serial.begin(9600);




  
  Serial.begin(9600);
}
  
void printRGB(int r, int g, int b, int frequency){
  
    //Serial.println("I don't know");
    
    Serial.print("frequency=");
    Serial.print(frequency);
    Serial.print("   R=");
    Serial.print(r);
    Serial.print("   G=");
    Serial.print(g);
    Serial.print("   B=");
    Serial.print(b);
    Serial.println("");
  }

bool inRange(int val,int low,int high){
  if(val>=low && val<=high) return true;
  return false;
  }

void loop() {



  int val = 0;
  if(digitalRead(pin2) || digitalRead(pin3) || digitalRead(pin12) || digitalRead(pin13) ){val = 1;}
  if(val != prevVal){
    written = false;
  }
  prevVal = val;
  
  if(val){ 
    if(!written) {myservo.attach(servoPin);myservo.write(50);delay(50);}
    written = true;
    myservo.detach();
  }
  else {    
    if(!written) {myservo.attach(servoPin);for(int j = 200;j< 300; j = j + 10 ){myservo.write(j);delay(15);}}
      written = true;
    myservo.detach();
   }



frequency = pulseIn(sensorOut, LOW);
int f = frequency; 
  // Setting red filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  r = pulseIn(sensorOut, LOW);//printing RED color frequency 
  delay(100);
  
  // Setting Green filtered photodiodes to be read
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  g = pulseIn(sensorOut, LOW);
  delay(100);
 
  // Setting Blue filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  b = pulseIn(sensorOut, LOW);

  if(0){//inRange(b, 620, 760) && inRange(f, 620, 760) && b<r and b<g){
    Serial.println("Blue");
    } 
  else if(0){//inRange(f, 380, 400) && inRange(g, 400, 460) && inRange(b, 360, 600) && r<g && r<b){
    Serial.println("Golden");
    }
  else if(0){//inRange(r, 350, 490) && r<g and r<b){
    Serial.println("Red");
    }
  else{
    printRGB(r,g,b,f);
  }
delay(100);
}
