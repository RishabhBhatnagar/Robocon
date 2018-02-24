void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  pinMode(A2, INPUT);
  pinMode(A2, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int r, g, b;
  r = analogRead(A0);
  g = analogRead(A1);
  b = analogRead(A2);
  if (r>500) Serial.println("Red");
  else if (b>500) Serial.println("Blue");
  else if (g>500) Serial.println("Goldenq");
}
