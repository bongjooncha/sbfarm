///// dht 온습도 센서   /////
#include <DHT.h>
#define dht_pin 46
#define dht_type DHT22
DHT dht(dht_pin, dht_type);

///// 릴레이 //////
#define rp1 31
#define rp2 33
#define rl1 35
#define rl2 37

///// 수위 /////
#define water_hight1 A0
#define water_hight2 A1

///// 수온 /////
#include <OneWire.h>
#include <DallasTemperature.h>
#define water_temp1 50
#define water_temp2 52
OneWire onewire1(water_temp1);
OneWire onewire2(water_temp2);
DallasTemperature WT1(&onewire1);
DallasTemperature WT2(&onewire2);


///// 양액 농도 /////
#define plant_food  A5

//// 스텝모터 ////
#define step_moter1
#define step_moter2


void setup() {
  Serial.begin(9600);

  //dht
  dht.begin();
  //릴레이
  pinMode(rp1,OUTPUT);
  pinMode(rp2,OUTPUT);
  pinMode(rl1,OUTPUT);
  pinMode(rl2,OUTPUT);
  //수온
  WT1.begin();
  WT2.begin();

  digitalWrite(rp1,HIGH);
  digitalWrite(rl1,HIGH);
  digitalWrite(rl2,HIGH);
}

void loop() {
  char cmd;

  //dht
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (Serial.available()) {
    cmd = Serial.read();

    /// 릴레이
    if (cmd == 'a') {
      Serial.print("습도: ");
      Serial.print(h);
      Serial.print("%   온도: ");
      Serial.print(t);
      Serial.println("°C");
    }

    /// 릴레이
    else if (cmd == 'b'){
      digitalWrite(rp1,HIGH);
      Serial.println("수류 on");
    }
    else if (cmd == 'c'){
      digitalWrite(rp1,LOW);      
      Serial.println("수류 off");
    }
    else if (cmd == 'd'){
      digitalWrite(rp2,HIGH);
      Serial.println("양액 on");
    }
    else if (cmd == 'e'){
      digitalWrite(rp2,LOW);
      Serial.println("양액 off");
    }    
    else if (cmd == 'f'){
      digitalWrite(rl1,HIGH);
      Serial.println("1층 led on");
    }
    else if (cmd == 'g'){
      digitalWrite(rl1,LOW);
      Serial.println("1층 led off");
    }
    else if (cmd == 'h'){
      digitalWrite(rl2,HIGH);
      Serial.println("2층 led on");
    }
    else if (cmd == 'i'){
      digitalWrite(rl2,LOW);
      Serial.println("2층 led off");
    }

    /// 수위
    else if (cmd == 'j'){
      int level1 = analogRead(water_hight1);
      Serial.println(level1);
    }
    else if (cmd == 'k'){
      int level2 = analogRead(water_hight2);
      Serial.println(level2);
    }

    ///수온
    else if (cmd == 'l'){
      Serial.print(WT1.getTempCByIndex(0));
      Serial.println("°C");
    }
    else if (cmd == 'm'){
      Serial.print(WT2.getTempCByIndex(0));
      Serial.println("°C");
    }
    
    /// 양액
    else if (cmd == 'n'){
      int pf = analogRead(plant_food);
      Serial.println(pf);
    }
  }
}
