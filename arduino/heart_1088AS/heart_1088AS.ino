// Arduino Uno + 1088AS
// 每根列线串联一只 2.2kΩ 电阻

// 从上到下，第 1～8 行对应的 Arduino 引脚
const byte rowPins[8] = {
  2, 3, 4, 5, 6, 7, 8, 9
};

// 从左到右，第 1～8 列对应的 Arduino 引脚
const byte colPins[8] = {
  10, 11, 12, 13, A0, A1, A2, A3
};

// 每个二进制数对应一行
// 1 = 亮，0 = 灭
const byte heart[8] = {
  0b00000000,
  0b01100110,
  0b11111111,
  0b11111111,
  0b01111110,
  0b00111100,
  0b00011000,
  0b00000000
};

void setup() {
  // 所有列先关闭：LOW
  for (byte c = 0; c < 8; c++) {
    digitalWrite(colPins[c], LOW);
    pinMode(colPins[c], OUTPUT);
  }

  // 所有行先关闭：HIGH
  for (byte r = 0; r < 8; r++) {
    digitalWrite(rowPins[r], HIGH);
    pinMode(rowPins[r], OUTPUT);
  }
}

// 扫描一遍完整图案
void displayFrame(const byte pattern[8]) {
  for (byte r = 0; r < 8; r++) {
    // 此时所有行都已关闭，可以设置列
    for (byte c = 0; c < 8; c++) {
      bool isOn = (pattern[r] >> (7 - c)) & 1;
      digitalWrite(colPins[c], isOn ? HIGH : LOW);
    }

    // 打开当前行
    digitalWrite(rowPins[r], LOW);
    delayMicroseconds(1000);

    // 关闭当前行，再切换下一行
    digitalWrite(rowPins[r], HIGH);
  }

  // 一帧结束，关闭所有列
  for (byte c = 0; c < 8; c++) {
    digitalWrite(colPins[c], LOW);
  }
}

void loop() {
  // 持续刷新，眼睛看到的就是完整爱心
  displayFrame(heart);
}