const uint8_t redPin = 10;
const uint8_t bluePin = 9;
const uint8_t greenPin = 8;
const float powerCoef = 0.659;

struct Color {
  uint8_t r = 0;
  uint8_t g = 0;
  uint8_t b = 0;
};

Color cur_color;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  cur_color.r = 255;
  cur_color.g = 255;
  cur_color.b = 255;
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
}

Color getNewColor() {
  String color_str = Serial.readString();
  String values[3];
  int count = 0;
  while (color_str.length() > 0) {
    int index = color_str.indexOf(' ');
    if (index == -1) {
      values[count++] = color_str;
      break;
    }
    else {
      values[count++] = color_str.substring(0, index);
      color_str = color_str.substring(index + 1);
    }
  }
  Color new_color;
  new_color.r = values[0].toInt();
  new_color.g = values[1].toInt();
  new_color.b = values[2].toInt();
  return new_color;
}

void loop() {
  if (Serial.available()) {
    cur_color = getNewColor();
    analogWrite(redPin, cur_color.r * powerCoef);
    analogWrite(greenPin, cur_color.g * powerCoef);
    analogWrite(bluePin, cur_color.b * powerCoef);
  }
}
