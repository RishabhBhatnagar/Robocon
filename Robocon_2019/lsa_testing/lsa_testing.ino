#define serialEn 2 // initially 14

//conn
void setup() {
  Serial.begin(38400);
  pinMode(serialEn,OUTPUT);
  digitalWrite(serialEn,HIGH);
}

void loop() {
  int lsa_value;
    digitalWrite(serialEn,LOW);
    while(Serial.available() <= 0);
    lsa_value = Serial.read();
    Serial.println(lsa_value); 
}
