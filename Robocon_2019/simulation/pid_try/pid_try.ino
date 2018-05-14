double kp = 0;
double kd = 0;
double ki = 0;
//
int error_sum = 0;
int prev_error = 0;
int prev_time = 0;
void setup(){
  kp = 1;
  kd = 1;
  ki = 1;
}
int get_correction(int result, int setpoint){
  
  unsigned long current_time = millis();
  
  int dt = current_time - prev_time;
  int error = result - setpoint;
  
  error_sum += error;
  int diff_error = error - prev_error;
  
  int correction = kp*error + ki*(error_sum)*dt + kd*(diff_error)/dt;        //corrected value.
  
  prev_error = error;
  prev_time = current_time;
  
  return correction;
}
void loop(){
  //logic can be written here.
}
