from jugaad import *
from random import randint as random
kp = 0;
kd = 0;
ki = 0;

error_sum = 10;
prev_error = 10;
prev_time = 10;

def setup():
    global kp, kd, ki, setpoint
    kp = 1
    kd = 0.01
    ki = 0.1
    setpoint = 20
        
def get_correction(result, setpoint):
    
    global prev_time, error_sum, prev_error    #python ke liye karna padaa.
    
    current_time = millis();
  
    dt = current_time - prev_time;
    error = result - setpoint;
    #print('dt', dt, 'error', error)
  
    error_sum += error;
    diff_error = error - prev_error;
  
    correction = kp*error + ki*(error_sum)*dt + kd*(diff_error)/dt;
  
    prev_error = error;
    Serial.print("  previous error : ", error)
    delay(random(200, 500));         #added delay to simulate realtime delay in error reading.
    
    prev_time = current_time;
  
    return correction;

def loop():
    
    result = random(16, 24)                      #getting value from sensor
    correction = get_correction(result, setpoint)
    Serial.println("  correction value : ", correction)
    delay(1000)

setup()
while True : loop()
