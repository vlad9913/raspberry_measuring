


int sign;

long value;

float result;

int x_clockpin = 7;  
int x_datapin = 6;

int y_clockpin = 5;
int y_datapin = 4;

int z_clockpin = 3;
int z_datapin = 2;

int iteration = 0;

int enable = 9;
int switch_b = 8;
unsigned long tempmicros;
 

 

void setup() {

  Serial.begin(9600);

  /*pinMode(x_datapin, OUTPUT);
  pinMode(y_datapin, OUTPUT);
  pinMode(z_datapin, OUTPUT);
  digitalWrite(x_datapin,HIGH);
  digitalWrite(y_datapin,HIGH);
  digitalWrite(z_datapin,HIGH);
  
  delay(50);*/

 
  
  pinMode(x_clockpin, INPUT);

  pinMode(x_datapin, INPUT);
  
  pinMode(y_clockpin, INPUT);

  pinMode(y_datapin, INPUT);
  
  pinMode(z_clockpin, INPUT);

  pinMode(z_datapin, INPUT);

  pinMode(enable, INPUT);

  pinMode(switch_b,INPUT_PULLUP);
  
  digitalWrite(enable,HIGH);

  
  

}



 void loop () {
  

  while (digitalRead(switch_b)==HIGH){}
  for(int i = 0 ; i < 3 ; i++){
    Serial.println("id=");
    Serial.println(iteration);  
    //X COORDS
    signal(x_clockpin,x_datapin,"X=");
    delay(20);
  
    //Y COORDS
    signal(y_clockpin,y_datapin,"Y=");
    delay(20);
    
    //Z COORDS
    signal(z_clockpin,z_datapin,"Z=");
    delay(20);
  }
  iteration+=1;
  
  
}

void signal(int clockpin, int datapin, String coord){
 
  while (digitalRead(clockpin)==LOW) {} //if clock is LOW wait until it turns to HIGH

  tempmicros=micros();

  while (digitalRead(clockpin)==HIGH) {} //wait for the end of the HIGH pulse


  while ((micros()-tempmicros)<=500) {} //if the HIGH pulse was longer than 500 micros we are at the start of a new bit sequence

      decode(clockpin,datapin,coord); //decode the bit sequence
  
  
}
 

void decode(int clockpin, int datapin, String coord) {

  sign=1;

  value=0;


  for (int i=0;i<23;i++) {

    while (digitalRead(clockpin)==HIGH) { } //wait until clock returns to HIGH- the first bit is not needed

    while (digitalRead(clockpin)==LOW) {} //wait until clock returns to LOW

    if (digitalRead(datapin)==LOW) {

      if (i<20) {

        value|= 1<<i;

      }

      if (i==20) {

        sign=-1;

      }

    }

  }

  result=(value*sign)/100.00;    
  Serial.println(coord);
  Serial.println(result,2); //print result with 2 decimals

  

}                             
