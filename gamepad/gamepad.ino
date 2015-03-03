int led1 = 10;


void setup(){
  Serial.begin(9600);
  pinMode(led1, OUTPUT);

}

void loop(){
  char leitura = Serial.read();

  if(leitura == '1'){
    digitalWrite(led1, HIGH);
  }
  else if(leitura == '2'){
    digitalWrite(led1, LOW);
  }
}
