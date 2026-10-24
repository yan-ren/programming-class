// HC-SR04 + 红黄绿交通灯模块
// 适用于 Arduino Uno R3 / 5V 兼容板

const byte TRIG_PIN = 9;
const byte ECHO_PIN = 10;

const byte GREEN_PIN  = 2;
const byte YELLOW_PIN = 3;
const byte RED_PIN    = 4;

// 在这里修改远近分界，单位：厘米
const float THRESHOLD_CM = 20.0;

// 每次只亮一个灯
void showLight(byte lightPin) {
  digitalWrite(RED_PIN, LOW);
  digitalWrite(YELLOW_PIN, LOW);
  digitalWrite(GREEN_PIN, LOW);

  digitalWrite(lightPin, HIGH);
}

// 返回距离（厘米）
// 返回 -1 表示没有收到回声或超出有效测距范围
float readDistanceCm() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // 等待 Echo 高电平脉冲，最多等待 30 毫秒
  unsigned long duration =
      pulseIn(ECHO_PIN, HIGH, 30000UL);

  if (duration == 0) {
    return -1;
  }

  // 回声时间包含往返，因此除以 2
  float distance = duration * 0.0343 / 2.0;

  if (distance < 2.0 || distance > 400.0) {
    return -1;
  }

  return distance;
}

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(RED_PIN, OUTPUT);
  pinMode(YELLOW_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);

  digitalWrite(TRIG_PIN, LOW);

  Serial.begin(9600);

  // 开机先显示黄灯，等待第一次测距
  showLight(YELLOW_PIN);
}

void loop() {
  float distance = readDistanceCm();

  if (distance < 0) {
    showLight(YELLOW_PIN);
    Serial.println("No valid reading");
  }
  else {
    Serial.print("Distance: ");
    Serial.print(distance, 1);
    Serial.println(" cm");

    if (distance <= THRESHOLD_CM) {
      showLight(RED_PIN);
    }
    else {
      showLight(GREEN_PIN);
    }
  }

  delay(100);
}